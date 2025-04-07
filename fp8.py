import sqlite3
import tkinter as tk
from tkinter import ttk
import os

# Database setup
database_file = "customer_info.db"

def create_database():
    # Print where the file is being created (for debug)
    print("Creating or opening DB at:", os.path.abspath(database_file))

    # Create database file and table if not exists
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birthday TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        contact_method TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Call the function to set up the DB
create_database()

# GUI Application
class CustomerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Information Form")

        # Name
        tk.Label(root, text="Name:").pack(anchor="w", padx=20)
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(pady=5)

        # Birthday
        tk.Label(root, text="Birthday (YYYY-MM-DD):").pack(anchor="w", padx=20)
        self.birthday_entry = tk.Entry(root, width=50)
        self.birthday_entry.pack(pady=5)

        # Email
        tk.Label(root, text="Email:").pack(anchor="w", padx=20)
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack(pady=5)

        # Phone
        tk.Label(root, text="Phone:").pack(anchor="w", padx=20)
        self.phone_entry = tk.Entry(root, width=50)
        self.phone_entry.pack(pady=5)

        # Address
        tk.Label(root, text="Address:").pack(anchor="w", padx=20)
        self.address_entry = tk.Entry(root, width=50)
        self.address_entry.pack(pady=5)

        # Preferred Contact Method
        tk.Label(root, text="Preferred Contact Method:").pack(anchor="w", padx=20)
        self.contact_method = ttk.Combobox(root, values=["Email", "Phone", "Mail"], state="readonly")
        self.contact_method.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_info)
        self.submit_button.pack(pady=10)

    def submit_info(self):
        # Get values from the form
        name = self.name_entry.get()
        birthday = self.birthday_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        contact_method = self.contact_method.get()

        # Save to database
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customers (name, birthday, email, phone, address, contact_method)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, birthday, email, phone, address, contact_method))
        conn.commit()
        conn.close()

        # Console feedback (optional)
        print("Customer information saved.")

        # Clear the form
        self.name_entry.delete(0, "end")
        self.birthday_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.contact_method.set("")

# Launch GUI
root = tk.Tk()
app = CustomerApp(root)
root.mainloop()