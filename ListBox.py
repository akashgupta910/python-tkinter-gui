from tkinter import *

i = 0
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1

root = Tk()
root.geometry("600x400")
root.title("ListBox in Tkinter")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First Item of our ListBox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()
