from tkinter import *

root = Tk()
root.geometry("1200x900")
root.minsize(1200,900)
root.title("PyCharm")

f1 = Frame(root, bg="grey", borderwidth=7)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

f3 = Frame(root, bg="white", borderwidth=7)
f3.pack(side=TOP, fill=X,)

f4 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
f4.pack(side=BOTTOM, fill=X)

l1 = Label(f1, text="Tkinter Projects", font="comicsansms 9 bold")
l1.pack(pady=10, padx=12)

l2 = Label(f2, text="Sublime Text 3", font="comicsansms 9 bold")
l2.pack(pady=10, padx=12)

l3 = Label(f3, text="Write your text here....")
l3.pack(pady=250)

l4 = Label(f4, text="Console")
l4.pack(pady=110)

root.mainloop()

