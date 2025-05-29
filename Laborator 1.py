import csv
import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size  #Se calculeaza in ce casuta sa pun cnp-ul

    def insert(self, key, value):  #Pune numele si cnp-ul in casuta potrivita
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):   #Se cauta cnp-ul
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

def generate_cnp():
    cnp = "".join(str(random.randint(0, 9)) for _ in range(13))
    return cnp

def generate_name():
    first_names = ["Ion", "Maria", "Mihai", "Elena", "Ana"]
    last_names = ["Popescu", "Ionescu", "Stan", "Dumitrescu", "Paun"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

with open('cnp_names.csv', mode='w', newline='') as file:  #Se creeaza fisierul cu un mil de cnp-uri
    writer = csv.writer(file)
    writer.writerow(['CNP', 'Nume'])
    for _ in range(1000000):
        writer.writerow([generate_cnp(), generate_name()])
print("Generare CSV finalizata.")

table_size = 1000000  # Se pun toate datele in hushtable
hash_table = HashTable(table_size)

with open('cnp_names.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        hash_table.insert(row[0], row[1])
print("Populare Hash Table finalizata.")

random_cnp_list = [generate_cnp() for _ in range(1000)]
total_iterations = 0

for cnp in random_cnp_list:
    iterations = 0
    result = hash_table.search(cnp)
    if result is not None:
        iterations += 1
    total_iterations += iterations

average_iterations = total_iterations / len(random_cnp_list)
print(f"Numarul mediu de iteratii pentru cautare: {average_iterations}")