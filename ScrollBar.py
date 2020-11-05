from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("Scroll Bar in Tkinter")

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# listbox.pack(fill=BOTH, padx=20)
#
# for i in range(200):
#     listbox.insert(END, f"Item {i}")
#
# scrollbar.config(command=listbox.yview)

# text = Text(root, yscrollcommand = scrollbar.set, height=1000)
# text.pack(fill=BOTH)
# scrollbar.config(command=text.yview)

with open("file/1.txt", "r") as f:
    file = f.read()


txt = Label(root, text=f"{file}", yscrollcommand = scrollbar.set)
txt.pack()
scrollbar.config(command=txt.yview)

root.mainloop()

