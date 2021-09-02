from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Another frame in the wall")
root.iconbitmap('earth.ico')


# r = IntVar()
# r.set(1)  # set default value, optional
# r = StringVar()

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


toppings = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]
pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
