import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestiune Contacte")
        self.root.geometry("700x500")

        self.contacts_file = "contacte.json"
        self.contacts = self.load_contacts()

        self.create_main_window()

    def load_contacts(self):
        if os.path.exists(self.contacts_file):
            try:
                with open(self.contacts_file, "r") as file:
                    return json.load(file)
            except:
                return []
        else:
            return []

    def save_contacts(self):
        with open(self.contacts_file, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def create_main_window(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10, padx=10, fill="x")

        tk.Button(control_frame, text="Adauga Contact", width=15,
                  command=self.open_add_contact_window).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Editeaza Contact", width=15,
                  command=self.open_edit_contact_window).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Sterge Contact", width=15,
                  command=self.delete_contact).pack(side=tk.LEFT, padx=5)

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=5, padx=10, fill="x")

        tk.Label(search_frame, text="Cauta:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_var.trace("w", self.filter_contacts)

        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)

        columns = ("nume", "telefon", "email", "adresa")
        self.contact_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.contact_tree.heading("nume", text="Nume")
        self.contact_tree.heading("telefon", text="Telefon")
        self.contact_tree.heading("email", text="Email")
        self.contact_tree.heading("adresa", text="Adresa")

        self.contact_tree.column("nume", width=150)
        self.contact_tree.column("telefon", width=100)
        self.contact_tree.column("email", width=150)
        self.contact_tree.column("adresa", width=250)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.contact_tree.yview)
        self.contact_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.contact_tree.pack(fill="both", expand=True)

        self.populate_contacts()

    def populate_contacts(self):
        self.contact_tree.delete(*self.contact_tree.get_children())
        search_term = self.search_var.get().lower()

        for contact in self.contacts:
            if (search_term == "" or
                    search_term in contact["nume"].lower() or
                    search_term in contact["telefon"].lower() or
                    search_term in contact["email"].lower()):
                self.contact_tree.insert("", "end", values=(
                    contact["nume"],
                    contact["telefon"],
                    contact["email"],
                    contact["adresa"]))

    def filter_contacts(self, *args):
        self.populate_contacts()

    def open_add_contact_window(self):
        self.contact_window = tk.Toplevel(self.root)
        self.contact_window.title("Adauga Contact")
        self.contact_window.geometry("400x300")
        self.contact_window.grab_set()  

        self.create_contact_form()

        tk.Button(self.contact_window, text="Salveaza",
                  command=self.add_contact).pack(pady=10)

    def open_edit_contact_window(self):
        selected_item = self.contact_tree.selection()
        if not selected_item:
            messagebox.showwarning("Atentie", "Selectati un contact pentru editare!")
            return

        selected_index = self.contact_tree.index(selected_item[0])
        selected_contact = self.contacts[selected_index]

        self.contact_window = tk.Toplevel(self.root)
        self.contact_window.title("Editeaza Contact")
        self.contact_window.geometry("400x300")
        self.contact_window.grab_set()

        self.create_contact_form()

        self.nume_var.set(selected_contact["nume"])
        self.telefon_var.set(selected_contact["telefon"])
        self.email_var.set(selected_contact["email"])
        self.adresa_var.set(selected_contact["adresa"])

        tk.Button(self.contact_window, text="Actualizeaza",
                  command=lambda: self.update_contact(selected_index)).pack(pady=10)

    def create_contact_form(self):
        form_frame = tk.Frame(self.contact_window)
        form_frame.pack(padx=20, pady=20, fill="both")

        self.nume_var = tk.StringVar()
        self.telefon_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.adresa_var = tk.StringVar()

        tk.Label(form_frame, text="Nume:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.nume_var, width=30).grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Telefon:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.telefon_var, width=30).grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.email_var, width=30).grid(row=2, column=1, pady=5)

        tk.Label(form_frame, text="Adresa:").grid(row=3, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.adresa_var, width=30).grid(row=3, column=1, pady=5)

    def validate_contact(self):
        nume = self.nume_var.get().strip()
        telefon = self.telefon_var.get().strip()

        if not nume:
            messagebox.showerror("Eroare", "Numele este obligatoriu!")
            return False

        if not telefon:
            messagebox.showerror("Eroare", "Telefonul este obligatoriu!")
            return False

        return True

    def add_contact(self):
        if not self.validate_contact():
            return

        new_contact = {
            "nume": self.nume_var.get().strip(),
            "telefon": self.telefon_var.get().strip(),
            "email": self.email_var.get().strip(),
            "adresa": self.adresa_var.get().strip()
        }

        self.contacts.append(new_contact)
        self.save_contacts()
        self.populate_contacts()
        self.contact_window.destroy()
        messagebox.showinfo("Succes", "Contact adaugat cu succes!")

    def update_contact(self, index):
        if not self.validate_contact():
            return

        updated_contact = {
            "nume": self.nume_var.get().strip(),
            "telefon": self.telefon_var.get().strip(),
            "email": self.email_var.get().strip(),
            "adresa": self.adresa_var.get().strip()
        }

        self.contacts[index] = updated_contact
        self.save_contacts()
        self.populate_contacts()
        self.contact_window.destroy()
        messagebox.showinfo("Succes", "Contact actualizat cu succes!")

    def delete_contact(self):
        selected_item = self.contact_tree.selection()
        if not selected_item:
            messagebox.showwarning("Atentie", "Selectati un contact pentru stergere!")
            return

        result = messagebox.askyesno("Confirmare", "Sunteti sigur ca doriti sa stergeti acest contact?")
        if result:
            selected_index = self.contact_tree.index(selected_item[0])
            del self.contacts[selected_index]
            self.save_contacts()
            self.populate_contacts()
            messagebox.showinfo("Succes", "Contact sters cu succes!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()