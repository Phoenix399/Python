import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissor") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissor" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    user_label.config(text=f"You chose: {choice}")
    comp_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

# Window setup
root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("300x250")

tk.Label(root, text="Choose an option:", font=("Arial", 12)).pack(pady=5)

# Buttons
tk.Button(root, text="Rock", width=12, command=lambda: play("Rock")).pack(pady=3)
tk.Button(root, text="Paper", width=12, command=lambda: play("Paper")).pack(pady=3)
tk.Button(root, text="Scissor", width=12, command=lambda: play("Scissor")).pack(pady=3)

# Output labels
user_label = tk.Label(root, text="", font=("Arial", 10))
user_label.pack(pady=5)

comp_label = tk.Label(root, text="", font=("Arial", 10))
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
