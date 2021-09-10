from pprint import pprint
from tkinter import *
import numpy as np

root = Tk()
root.title("Wafer Test")

frame = LabelFrame(root, text='Wafer Status', padx=5, pady=5)
frame.pack(padx=5, pady=5)

matrix = np.matrix([[1, 0, 1, 0],
                    [0, 1, 0, 0],
                    [1, 0, 1, 0]])
print(matrix.shape)

with open('mymap.map') as f:
    result = [list(line.rstrip()) for line in f]

matrix = np.matrix(result)

cell_size = 4
canvas_width = cell_size * matrix.shape[0]
canvas_height = cell_size * matrix.shape[1]
my_canvas = Canvas(frame, width=canvas_width, height=canvas_height, bg="white")
my_canvas.pack()

matrix_iterator = np.nditer(matrix, flags=['multi_index'])
for x in matrix_iterator:
    index = matrix_iterator.multi_index
    # print(x, index)

    # top left anchor
    x1 = index[0] * cell_size
    y1 = index[1] * cell_size
    # bottom left anchor
    x2 = (index[0] + 1) * cell_size
    y2 = (index[1] + 1) * cell_size

    if x == '0':
        my_canvas.create_rectangle(x1, y1, x2, y2, fill="red")
    elif x == '1':
        my_canvas.create_rectangle(x1, y1, x2, y2, fill="green")
    elif x == '2':
        my_canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
    elif x == '3':
        my_canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
    else:
        my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")

root.mainloop()