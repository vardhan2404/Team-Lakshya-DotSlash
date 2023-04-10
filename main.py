from pymongo import MongoClient
import tkinter as tk
from tkinter import filedialog

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Create a GUI window
window = tk.Tk()
window.title("File Uploader")


# Define a function to handle file selection and upload
def upload_file():
    # Show file dialog
    file_path = filedialog.askopenfilename()
    if file_path:
        # Open and read the file
        with open(file_path, 'rb') as f:
            file_data = f.read()

        # Create a document and insert it into the collection
        doc = {'filename': file_path, 'data': file_data}
        collection.insert_one(doc)

        # Show success message
        tk.messagebox.showinfo("Success", "File uploaded successfully!")
    else:
        # Show error message
        tk.messagebox.showerror("Error", "No file selected.")


# Create a button to trigger file selection and upload
upload_button = tk.Button(window, text="Upload File", command=upload_file)
upload_button.pack(padx=10, pady=10)

# Run the GUI window
window.mainloop()
