from tkinter import *

def lan():
    print("Hindi, English...")

def ml():
    print("HTML")

def pl():
    print("Python, Java...")

def sl():
    print("Javascript, PHP...")

root = Tk()


root.geometry("900x600")
f1 = Frame(root, borderwidth=6)
f1.pack(anchor="nw", side=LEFT)

b1 = Button(f1, text="Language", padx=6, pady=6, bg="red", fg="white", font="comicsansms 11 bold", command=lan)
b1.pack(side=LEFT, padx=6)

b2 = Button(f1, text="Markup Language", padx=6, pady=6, bg="red", fg="white", font="comicsansms 11 bold", command=ml)
b2.pack(side=LEFT, padx=6)

b3 = Button(f1, text="Programming Language", padx=6, pady=6, bg="red", fg="white", font="comicsansms 11 bold", command=pl)
b3.pack(side=LEFT, padx=6)

b4 = Button(f1, text="Scripting Language", padx=6, pady=6, bg="red", fg="white", font="comicsansms 11 bold", command=sl)
b4.pack(side=LEFT, padx=6)


root.mainloop()

