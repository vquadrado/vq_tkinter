from tkinter import *
from PIL import ImageTk, Image
import glob
import itertools

root = Tk()
root.title('Capenga - Image Viewer')
root.iconbitmap('earth.ico')

pil_obj_list = []
img_list = glob.glob('**/*.jpeg', recursive=True)
for i in img_list:
    pil_obj = ImageTk.PhotoImage(Image.open(i))
    pil_obj_list.append(pil_obj)

image_index = 0
it = itertools.cycle(range(len(pil_obj_list)))


def index_up_down(b):
    global image_index
    global image_label
    global status_label
    if b:
        image_index = next(it)
    elif not b:
        if image_index <= 0:
            image_index = len(pil_obj_list) - 1
        else:
            image_index -= 1

    image_label.grid_forget()
    image_label = Label(image=pil_obj_list[image_index])
    image_label.grid(row=0, column=0, columnspan=3)

    status_label.grid_forget()
    status_label = Label(root, text="Image " + str(image_index + 1) + " of " + str(len(pil_obj_list)))
    status_label.grid(row=2, column=0, columnspan=3)

    print(image_index)


button_back = Button(root, text="<<", command=lambda: index_up_down(False))
button_exit = Button(root, text="EXIT", command=root.quit)
button_fwrd = Button(root, text=">>", command=lambda: index_up_down(True))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_fwrd.grid(row=1, column=2)
image_label = Label(image=pil_obj_list[image_index])
image_label.grid(row=0, column=0, columnspan=3)

status_label = Label(root, text="Image " + str(image_index + 1) + " of " + str(len(pil_obj_list)))
status_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
