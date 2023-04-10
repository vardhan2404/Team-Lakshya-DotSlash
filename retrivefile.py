from pymongo import MongoClient
import tkinter as tk
import os
from tkinter import ttk, messagebox, filedialog

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']


def display_file():
    filename = listbox.get(tk.ACTIVE)

    doc = collection.find_one({'filename': filename})

    if doc:
        text.delete('1.0', tk.END)
        text.insert(tk.END, doc['data'])
        messagebox.showinfo("Success", f"File '{filename}' displayed successfully.")
    else:
        messagebox.showerror("Error", f"File '{filename}' not found in collection.")


def retrieve_file():
    filename = listbox.get(tk.ACTIVE)

    doc = collection.find_one({'filename': filename})

    if doc:
        save_file_path = filedialog.asksaveasfilename(initialfile=filename, defaultextension=".pdf")

        if save_file_path:
            with open(save_file_path, 'wb') as f:
                f.write(doc['data'])

            messagebox.showinfo("Success", f"File '{filename}' retrieved successfully.")
    else:
        messagebox.showerror("Error", f"File '{filename}' not found in collection.")


def insert_file():
    filename = filedialog.askopenfilename()

    if filename:
        with open(filename, 'rb') as f:
            pdf_bytes = bytes(f.read())

        collection.insert_one({'filename': os.path.basename(filename), 'data': pdf_bytes})
        listbox.insert(tk.END, os.path.basename(filename))


window = tk.Tk()
window.title("PDF File Manager")
window.geometry("500x400")

# Create style for buttons
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)

# Create listbox to display file names
listbox_frame = ttk.Frame(window, padding=10)
listbox_frame.pack(fill=tk.BOTH, expand=True)

listbox = tk.Listbox(listbox_frame, font=('Helvetica', 12))
listbox.pack(fill=tk.BOTH, expand=True)

for doc in collection.find():
    listbox.insert(tk.END, doc['filename'])

# Create buttons to display and retrieve files
button_frame = ttk.Frame(window, padding=10)
button_frame.pack(fill=tk.X)

display_button = ttk.Button(button_frame, text="Display File", command=display_file)
display_button.pack(side=tk.LEFT)

retrieve_button = ttk.Button(button_frame, text="Retrieve File", command=retrieve_file)
retrieve_button.pack(side=tk.LEFT, padx=10)

insert_button = ttk.Button(button_frame, text="Insert File", command=insert_file)
insert_button.pack(side=tk.RIGHT)

# Create text box to display file content
text_frame = ttk.Frame(window, padding=10)
text_frame.pack(fill=tk.BOTH, expand=True)

text = tk.Text(text_frame, font=('Helvetica', 12), wrap=tk.WORD)
text.pack(fill=tk.BOTH, expand=True)

window.mainloop()
