from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

root = Tk()
root.title("Message in the bottle")
root.iconbitmap('earth.ico')


def popup():
    response = messagebox.showinfo("this is my popup", "hello world!")  # ok <class 'str'>
    # response = messagebox.showwarning("this is my popup", "hello world!")  # ok <class 'str'>
    # response = messagebox.showerror("this is my popup", "hello world!")  #  ok <class 'str'>
    # response = messagebox.askquestion("this is my popup", "hello world!") # no <class 'str'> yes <class 'str'>
    # response = messagebox.askokcancel("this is my popup", "hello world!")  # False <class 'bool'> True <class 'bool'>
    # response = messagebox.askyesno("this is my popup", "hello world!")  # False <class 'bool'> True <class 'bool'>

    print(response, type(response))

    if response == 1:
        Label(root, text="Yeeeeeet").pack()
    else:
        Label(root, text="Sheeeesh").pack()


b_popup = Button(root, text='Popup', command=popup)
b_popup.pack()

mainloop()
