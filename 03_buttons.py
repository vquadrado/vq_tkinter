from tkinter import *

root = Tk()


def my_click():
    myLabel = Label(root, text="Lool! I clicked the clicky thing")
    myLabel.pack()


myButton = Button(root, text="Click me!", command=my_click, bg="#000000", fg="#ffffff")
myButton.pack()

root.mainloop()
