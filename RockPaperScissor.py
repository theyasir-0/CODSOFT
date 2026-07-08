import tkinter as tk
import random

user_score = 0
computer_score = 0

def play(user):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)

    if user == computer:
        result = "Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    user_choice.config(text="Your Choice: " + user)
    comp_choice.config(text="Computer: " + computer)
    result_label.config(text=result)
    score.config(text=f"You: {user_score}   Computer: {computer_score}")

def play_again():
    user_choice.config(text="")
    comp_choice.config(text="")
    result_label.config(text="Choose Again")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")

tk.Label(root, text="Rock Paper Scissors Game",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="Rock", width=12,
          command=lambda: play("Rock")).pack(pady=5)

tk.Button(root, text="Paper", width=12,
          command=lambda: play("Paper")).pack(pady=5)

tk.Button(root, text="Scissors", width=12,
          command=lambda: play("Scissors")).pack(pady=5)

user_choice = tk.Label(root, text="")
user_choice.pack()

comp_choice = tk.Label(root, text="")
comp_choice.pack()

result_label = tk.Label(root, text="Choose One",
                        font=("Arial", 12, "bold"))
result_label.pack(pady=10)

score = tk.Label(root, text="You: 0   Computer: 0")
score.pack()

tk.Button(root, text="Play Again",
          command=play_again).pack(pady=10)

root.mainloop()