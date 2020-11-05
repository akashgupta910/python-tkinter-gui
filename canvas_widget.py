from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 500

root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

canvas_widget.create_line(0, 0 , 800, 500, fill="grey")
canvas_widget.create_line(0, 500 , 800, 0, fill="grey")

canvas_widget.create_rectangle(50, 100 , 500, 350, fill="grey")

canvas_widget.create_text(400, 400, text="Python")

canvas_widget.create_oval(50, 100 , 500, 350, fill="red")

root.mainloop()
