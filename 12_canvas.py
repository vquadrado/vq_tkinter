from tkinter import *

root = Tk()
root.title("Canvas")

frame = LabelFrame(root, text="My Canvas")
frame.pack()

my_canvas = Canvas(frame, width=300, height=200, bg="white")
my_canvas.pack()

x1, y1 = 0, 100
x2, y2 = 300, 100
my_canvas.create_line(x1, y1, x2, y2, fill="red")
my_canvas.create_line(y1, x1, y2, x2, fill="red")

#my_canvas.create_rectangle()

root.mainloop()
