from tkinter import *

root = Tk()

# entry = Entry(root, width=50, bg="#000000", fg="#ffffff", borderwidth=10).pack()
entry = Entry(root)
entry.pack()
entry.insert(0, "enter text")


def my_click():
    text = "input is: " + entry.get()
    myLabel = Label(root, text=text)
    myLabel.pack()


myButton = Button(root, text="Click me!", command=my_click, bg="#000000", fg="#ffffff")
myButton.pack()

root.mainloop()
