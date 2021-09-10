from tkinter import *
import tkinter as tk
import numpy as np


class MainFrame:
    def __init__(self, tk_root: tk.Tk, np_matrix: np.ndarray):
        tk_root.title("Wafer Test")
        frame = LabelFrame(tk_root, text='Wafer Status', padx=5, pady=5)
        # frame.pack(padx=5, pady=5)
        frame.grid(column=0, row=0)

        self.cell_size = 50
        self.canvas_width = self.cell_size * np_matrix.shape[0]
        self.canvas_height = self.cell_size * np_matrix.shape[1]

        self.my_canvas = Canvas(frame, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.my_canvas2 = Canvas(frame, width=self.canvas_width, height=self.canvas_height, bg="white")

        self.my_canvas.grid(column=0, row=0)
        self.my_canvas2.grid(column=1, row=1)

        self.matrix_iterator = np.nditer(np_matrix, flags=['multi_index'])
        for x in self.matrix_iterator:
            index = self.matrix_iterator.multi_index
            # top left anchor
            x1 = index[0] * self.cell_size
            y1 = index[1] * self.cell_size
            # bottom left anchor
            x2 = (index[0] + 1) * self.cell_size
            y2 = (index[1] + 1) * self.cell_size

            if x == 0:
                self.my_canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            elif x == 1:
                self.my_canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            elif x == 2:
                self.my_canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
            elif x == 3:
                self.my_canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
            else:
                self.my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")


root = Tk()
matrix = np.diag([1, 2, 3])

MainFrame(root, np_matrix=matrix)

root.mainloop()
