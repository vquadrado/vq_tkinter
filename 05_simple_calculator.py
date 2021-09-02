import tkinter as tk
from tkinter.font import Font
from tkinter import *

root = tk.Tk()
text = tk.Text(root)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def evaluate():
    x = eval(e.get())
    e.delete(0, END)
    e.insert(0, str(x))


def add_button_content(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_button_content(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_button_content(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_button_content(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_button_content(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_button_content(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_button_content(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_button_content(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_button_content(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_button_content(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_button_content(0))
button_add = Button(root, text="+", padx=30, pady=20, command=lambda: add_button_content("+"))
button_min = Button(root, text="-", padx=30, pady=20, command=lambda: add_button_content("-"))
button_div = Button(root, text="/", padx=30, pady=20, command=lambda: add_button_content("/"))
button_tim = Button(root, text="*", padx=30, pady=20, command=lambda: add_button_content("*"))
button_equal = Button(root, text="=", padx=40, pady=20, command=evaluate)
button_clear = Button(root, text="C", padx=40, pady=20, command=button_clear)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button_clear.grid(row=4, column=0)
button0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_add.grid(row=5, column=0)
button_min.grid(row=5, column=1)
button_tim.grid(row=5, column=2)
button_div.grid(row=5, column=3)

root.mainloop()
