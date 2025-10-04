import tkinter as tk

def generate_story():
    noun = noun_entry.get()
    verb = verb_entry.get()
    adjective = adjective_entry.get()
    story = f"Once upon a time, there was a {adjective} {noun} that  loved to {verb}."

    result_label.config(text=story)

# Create GUI window
window = tk.Tk()
window.title("Mad Libs Game")

# Input labels and fields
tk.Label(window, text="Noun:").pack()
noun_entry = tk.Entry(window)
noun_entry.pack()

tk.Label(window, text="Verb:").pack()
verb_entry = tk.Entry(window)
verb_entry.pack()

tk.Label(window, text="Adjective:").pack()
adjective_entry = tk.Entry(window)
adjective_entry.pack()

# Button
tk.Button(window, text="Create Story", command=generate_story).pack()

# Output label
result_label = tk.Label(window, text="", wraplength=3000)
result_label.pack(pady=10)

window.mainloop()
