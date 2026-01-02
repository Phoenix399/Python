import tkinter as tk
from tkinter import messagebox

# Create library object
books = Library(
    ['Python Crash Course', 'Clean Code', 'Atomic Habits', 'Cosmos', 'The Hobbit'],
    "Phoenix Library"
)

# Main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("500x400")

# User name
tk.Label(root, text="Your Name:").pack()
user_entry = tk.Entry(root)
user_entry.pack()

# Book name
tk.Label(root, text="Book Name:").pack()
book_entry = tk.Entry(root)
book_entry.pack()

# Book list
book_listbox = tk.Listbox(root, width=60)
book_listbox.pack(pady=10)

def refresh_books():
    book_listbox.delete(0, tk.END)
    for book in books.displayBooks():
        book_listbox.insert(tk.END, book)

refresh_books()

# Button functions
def lend_book():
    user = user_entry.get()
    book = book_entry.get()
    result = books.lendBook(user, book)
    messagebox.showinfo("Lend Book", result)

def add_book():
    book = book_entry.get()
    result = books.addBook(book)
    refresh_books()
    messagebox.showinfo("Add Book", result)

def return_book():
    book = book_entry.get()
    result = books.returnBook(book)
    messagebox.showinfo("Return Book", result)

# Buttons
tk.Button(root, text="Lend Book", command=lend_book).pack(pady=2)
tk.Button(root, text="Add Book", command=add_book).pack(pady=2)
tk.Button(root, text="Return Book", command=return_book).pack(pady=2)

root.mainloop()
