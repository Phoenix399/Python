import random
import tkinter as tk
from tkinter import messagebox

# Function to get computer choice
def computer_choice():
    return random.choice(["Rock", "Paper", "Scissor"])

# Function to decide the winner
def play(user_pick):
    comp = computer_choice()

    if user_pick == comp:
        result = "It's a Tie!"
    elif (user_pick == "Rock" and comp == "Scissor") or \
         (user_pick == "Paper" and comp == "Rock") or \
         (user_pick == "Scissor" and comp == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    messagebox.showinfo("Result", f"You chose: {user_pick}\nComputer chose: {comp}\n\n{result}")

# Tkinter Window
root = tk.Tk()
root.title("Rock Paper Scissor")

label = tk.Label(root, text="Choose one:")
label.pack(pady=10)

# Buttons
tk.Button(root, text="Rock", command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissor", command=lambda: play("Scissor")).pack(pady=5)

root.mainloop()
