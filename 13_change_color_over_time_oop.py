import tkinter as tk
import numpy as np


class MainWindow:
    def __init__(self, tk_root, name: str):
        super(MainWindow, self).__init__()
        tk_root.title(name)


class MyFrame(tk.LabelFrame):
    def __init__(self, tk_root, name: str, position_index: tuple, padding: tuple):
        super(MyFrame, self).__init__(tk_root)
        self.frame = tk.LabelFrame(tk_root, text=name, padx=padding[0], pady=padding[1])
        self.frame.grid(column=position_index[0], row=position_index[1])

        self.tk_root = tk_root
        self.contador = -1
        self.rectangle_dict = {}

    def create_canvas(self, canvas_size: tuple, background_color, position_index: tuple):
        self.canvas = tk.Canvas(self.frame, width=canvas_size[0], height=canvas_size[1], bg=background_color)
        self.canvas.grid(column=position_index[0], row=position_index[1])
        return self.canvas

    def change_color(self):

        # global counter, rectangle_dict, my_canvas, root
        color_list = ['Yellow', 'Blue', 'Teal', 'Brown', 'Orange', 'Gold', 'Tan', 'Purple', 'Olive', 'Aqua']
        self.contador += 1
        rectangles_values = list(self.rectangle_dict.values())

        color_index = int(rectangles_values[self.contador]) % 10

        self.canvas.itemconfig(rectangles_values[self.contador], fill=color_list[color_index])

        if self.contador < (len(rectangles_values) - 1):
            self.tk_root.after(1, self.change_color)


def build(root):
    with open('mymap.map') as f:
        result = [list(line.rstrip()) for line in f]

    matrix = np.matrix(result)

    matrix_iterator = np.nditer(matrix, flags=['multi_index'])

    cell_size = 4
    canvas_width = cell_size * matrix.shape[0]
    canvas_height = cell_size * matrix.shape[1]

    canvas_frame = MyFrame(root, 'wafer test results', (1, 0), (5, 5))
    canvas_rect_obj = canvas_frame.create_canvas(canvas_size=(canvas_width, canvas_height), background_color="white",
                                                 position_index=(0, 0))

    rectangles = {}
    for x in matrix_iterator:
        index = matrix_iterator.multi_index

        # top left anchor
        x1 = index[0] * cell_size
        y1 = index[1] * cell_size
        # bottom left anchor
        x2 = (index[0] + 1) * cell_size
        y2 = (index[1] + 1) * cell_size

        rectangles["rectangle({},{},{},{})".format(x1, y1, x2, y2)] = (
            canvas_rect_obj.create_rectangle(x1, y1, x2, y2, fill="white"))

    canvas_frame.rectangle_dict = rectangles

    return (rectangles, canvas_frame, canvas_rect_obj)


def main():
    root = tk.Tk()

    rectangle_dict, canvas_frame, canvas_rect_obj = build(root)  # <--- rectangle_dict e canvas_rect_obj sem uso

    canvas_frame.change_color()

    MainWindow(root, "My GUI")
    root.mainloop()


if __name__ == '__main__':
    main()
