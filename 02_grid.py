from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Will the real Slim Shady")
myLabel3 = Label(root, text="Please stand up?")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=5, column=5)

# or
# myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
# myLabel2 = Label(root, text="Will the real Slim Shady").grid(row=1, column=1)
# myLabel3 = Label(root, text="Please stand up?").grid(row=5, column=5)

root.mainloop()
