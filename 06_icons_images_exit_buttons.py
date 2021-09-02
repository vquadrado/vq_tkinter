from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('my title here')
root.iconbitmap('earth.ico')

pokeBall = Image.open("pokeball.png")
my_img = ImageTk.PhotoImage(pokeBall)

my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
