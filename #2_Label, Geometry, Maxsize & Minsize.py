from tkinter import *

root = Tk()

# Width x Height
root.geometry("600x400")

# Width, Height
root.minsize(200,100)

# Width, Height
root.maxsize(900, 700)

# User do not intract with Lable
label = Label(text="I am Programmer")
label.pack()

root.mainloop()


# Small Exercise
root = Tk()
root.geometry("733x434")
root.minsize(733,434)
root.maxsize(733,434)
label = Label(text="Welcome to PyCharm")
label.pack()
root.mainloop()
