from tkinter import *

root = Tk()
root.geometry("900x600")

root.title("PyCharm")

def fun():
    print("Hello")

# Not Dropdown Menu
# menu = Menu(root)
# menu.add_command(label="File", command=fun)
# menu.add_command(label="Exit", command=quit)
# root.config(menu=menu)

# Dropdown Menu

mymenu = Menu(root)
m1 = Menu(mymenu, tearoff=0)
m1.add_command(label="New Project", command=fun)
m1.add_command(label="Open", command=fun)
m1.add_separator()
m1.add_command(label="Save", command=fun)
m1.add_command(label="Save As", command=fun)
m1.add_command(label="Settings", command=fun)
mymenu.add_cascade(label="File", menu=m1)

m2 = Menu(mymenu, tearoff=0)
m2.add_command(label="Cut", command=fun)
m2.add_command(label="Copy", command=fun)
m2.add_command(label="Paste", command=fun)
m2.add_separator()
m2.add_command(label="Delete", command=fun)
m2.add_command(label="Find", command=fun)
mymenu.add_cascade(label="Edit", menu=m2)

root.config(menu=mymenu)


root.mainloop()

