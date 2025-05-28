import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template
import json
from flask import request, jsonify


app = Flask(__name__,
            template_folder='app/templates',
            static_folder='static')

DATA_FILE = 'app/data/items.json'


def load_data():
    """Încarcă datele din fișierul JSON"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(data):
    """Salvează datele în fișierul JSON"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_next_id(data):
    """Generează următorul ID disponibil"""
    if not data:
        return 1
    return max(item['id'] for item in data) + 1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/items', methods=['GET'])
def get_all_items():
    """Read toate înregistrările"""
    data = load_data()
    return jsonify(data), 200


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Read o înregistrare"""
    data = load_data()
    item = next((item for item in data if item['id'] == item_id), None)

    if item:
        return jsonify(item), 200
    return jsonify({'error': 'Item not found'}), 404


@app.route('/items', methods=['POST'])
def create_item():
    """Create o nouă înregistrare"""
    try:
        new_item = request.get_json()

        if not new_item or 'title' not in new_item or 'author' not in new_item:
            return jsonify({'error': 'Title and author are required'}), 400

        data = load_data()
        new_item['id'] = get_next_id(data)

        new_item.setdefault('year', '')
        new_item.setdefault('genre', '')

        data.append(new_item)
        save_data(data)

        return jsonify(new_item), 201
    except Exception as e:
        return jsonify({'error': 'Invalid JSON data'}), 400


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update o înregistrare"""
    try:
        updated_data = request.get_json()

        if not updated_data:
            return jsonify({'error': 'No data provided'}), 400

        data = load_data()
        item_index = next((i for i, item in enumerate(data) if item['id'] == item_id), None)

        if item_index is None:
            return jsonify({'error': 'Item not found'}), 404

        updated_data['id'] = item_id
        data[item_index] = updated_data
        save_data(data)

        return jsonify(updated_data), 200
    except Exception as e:
        return jsonify({'error': 'Invalid JSON data'}), 400


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete o înregistrare"""
    data = load_data()
    item_index = next((i for i, item in enumerate(data) if item['id'] == item_id), None)

    if item_index is None:
        return jsonify({'error': 'Item not found'}), 404

    deleted_item = data.pop(item_index)
    save_data(data)

    return jsonify({'message': f'Item "{deleted_item["title"]}" deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)