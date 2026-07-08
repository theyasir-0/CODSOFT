from tkinter import *

# Window
root = Tk()
root.title("Calculator")
root.geometry("300x350")

# Display
e = Entry(root, width=20, font=("Arial", 18))
e.grid(row=0, column=0, columnspan=4)

# Functions
def press(x):
    e.insert(END, x)

def clear():
    e.delete(0, END)

def equal():
    ans = eval(e.get())
    e.delete(0, END)
    e.insert(0, ans)

# Row 1
Button(root, text="7", width=5, height=2, command=lambda: press("7")).grid(row=1, column=0)
Button(root, text="8", width=5, height=2, command=lambda: press("8")).grid(row=1, column=1)
Button(root, text="9", width=5, height=2, command=lambda: press("9")).grid(row=1, column=2)
Button(root, text="+", width=5, height=2, command=lambda: press("+")).grid(row=1, column=3)

# Row 2
Button(root, text="4", width=5, height=2, command=lambda: press("4")).grid(row=2, column=0)
Button(root, text="5", width=5, height=2, command=lambda: press("5")).grid(row=2, column=1)
Button(root, text="6", width=5, height=2, command=lambda: press("6")).grid(row=2, column=2)
Button(root, text="-", width=5, height=2, command=lambda: press("-")).grid(row=2, column=3)

# Row 3
Button(root, text="1", width=5, height=2, command=lambda: press("1")).grid(row=3, column=0)
Button(root, text="2", width=5, height=2, command=lambda: press("2")).grid(row=3, column=1)
Button(root, text="3", width=5, height=2, command=lambda: press("3")).grid(row=3, column=2)
Button(root, text="*", width=5, height=2, command=lambda: press("*")).grid(row=3, column=3)

# Row 4
Button(root, text="C", width=5, height=2, command=clear).grid(row=4, column=0)
Button(root, text="0", width=5, height=2, command=lambda: press("0")).grid(row=4, column=1)
Button(root, text="=", width=5, height=2, command=equal).grid(row=4, column=2)
Button(root, text="/", width=5, height=2, command=lambda: press("/")).grid(row=4, column=3)

root.mainloop()