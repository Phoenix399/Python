import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    output_entry.delete(0, tk.END)
    output_entry.insert(0, password)

# Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x150")

# Length label + entry
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

# Output field
tk.Label(root, text="Generated Password:").pack()
output_entry = tk.Entry(root, width=40)
output_entry.pack()

root.mainloop()
