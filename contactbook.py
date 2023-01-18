import tkinter as tk

# Define an empty list to store the contacts
contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    result_label.config(text='Contact added!')

def view_contacts():
    result_label.config(text='')
    for contact in contacts:
        result_label.config(text=result_label.cget("text") + contact['name'] + ' ' + contact['phone'] + ' ' + contact['email']+'\n')

def search_contacts():
    name = search_entry.get()
    result_label.config(text='')
    for contact in contacts:
        if contact['name'] == name:
            result_label.config(text=contact['name'] + ' ' + contact['phone'] + ' ' + contact['email'])
            return
    result_label.config(text='Contact not found.')

root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")

name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, pady=10)

phone_label = tk.Label(root, text="Phone")
phone_label.grid(row=1, column=0, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, pady=10)

email_label = tk.Label(root, text="Email")
email_label.grid(row=2, column=0, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, pady=10)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=1, pady=10)

search_label = tk.Label(root, text="Search by name")
search_label.grid(row=4, column=0, pady=10)
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1, pady=10)
search_button = tk.Button(root, text="Search", command=search_contacts)
search_button.grid(row=5, column=1, pady=10)

view_button = tk.Button(root, text
