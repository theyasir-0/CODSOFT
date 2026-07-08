import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter a valid length")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        result.config(text=password)

    except:
        messagebox.showerror("Error", "Enter numbers only")

# GUI Window
root = tk.Tk()
root.title("Pas sword Generator")
root.geometry("400x250")
root.resizable(False, False)

title = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

tk.Label(root, text="Enter Password Length").pack()

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=350)
result.pack(pady=10)

root.mainloop()