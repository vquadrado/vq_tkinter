from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Another frame in the wall")
root.iconbitmap('earth.ico')

frame = LabelFrame(root, text="Don't look here", padx=5, pady=5)
frame.pack(padx=5, pady=5)

b1 = Button(frame, text="Don't click here!", command=root.quit)
b2 = Button(frame, text="or here!", command=root.quit)

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
root.mainloop()
