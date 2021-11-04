import tkinter as tk
import numpy as np


class MainWindow:
    def __init__(self, tk_root, name: str):
        tk_root.title(name)


class MyFrame(tk.LabelFrame):
    def __init__(self, tk_root, name: str, position_index: tuple, padding: tuple):
        super(MyFrame, self).__init__()
        self.frame = tk.LabelFrame(tk_root, text=name, padx=padding[0], pady=padding[1])
        self.frame.grid(column=position_index[0], row=position_index[1])

    # ToDo: need to inherit tk.Button methods
    def create_button(self, button_text: str, position_index: tuple):
        button = tk.Button(self.frame, text=button_text)
        button.grid(column=position_index[0], row=position_index[1])

    # ToDo: need to inherit tk.Canvas methods
    def create_canvas(self, canvas_size: tuple, background_color, position_index: tuple):
        canvas = tk.Canvas(self.frame, width=canvas_size[0], height=canvas_size[1], bg=background_color)
        canvas.grid(column=position_index[0], row=position_index[1])
        return canvas

    def create_rectangle(self):
        pass


def build(root):
    buttons_frame = MyFrame(root, 'a frame full of buttons', (0, 0), (5, 5))
    for i in range(4):
        for j in range(4):
            buttons_frame.create_button(button_text=f"button({i},{j})", position_index=(i, j))

    with open('mymap.map') as f:
        matrix = np.matrix([list(line.rstrip()) for line in f])

    cell_size = 4
    canvas_width = cell_size * matrix.shape[0]
    canvas_height = cell_size * matrix.shape[1]

    canvas_frame = MyFrame(root, 'wafer test results', (1, 0), (5, 5))
    canvas_rect_map = canvas_frame.create_canvas(canvas_size=(canvas_width, canvas_height), background_color="white",
                               position_index=(0, 0))

    matrix_iterator = np.nditer(matrix, flags=['multi_index'])
    for x in matrix_iterator:
        index = matrix_iterator.multi_index

        # top left anchor
        x1 = index[0] * cell_size
        y1 = index[1] * cell_size
        # bottom left anchor
        x2 = (index[0] + 1) * cell_size
        y2 = (index[1] + 1) * cell_size

        canvas_rect_map.create_rectangle(x1, y1, x2, y2)

        # if x == '0':
        #     canvas_frame.create_rectangle(x1, y1, x2, y2, fill="red")
        # elif x == '1':
        #     my_canvas.create_rectangle(x1, y1, x2, y2, fill="green")
        # elif x == '2':
        #     my_canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
        # elif x == '3':
        #     my_canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
        # else:
        #     my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")


def main():
    root = tk.Tk()
    build(root)
    MainWindow(root, "My GUI")
    root.mainloop()


if __name__ == '__main__':
    main()
