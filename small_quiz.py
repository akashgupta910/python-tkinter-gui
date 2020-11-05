from tkinter import *

root = Tk()

def getvalue():
    print("Value Submitted")

root.geometry("600x400")

Label(text="Username: ", font="comicsansms 10 bold", pady=2).grid(row=1, column=1)
Label(text="Password: ", font="comicsansms 10 bold", pady=13).grid(row=2, column=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue).grid(row=1, column=2)
passentry = Entry(root, textvariable=passvalue).grid(row=2, column=2)

Button(text="Submit", font="comicsansms 10 bold", command=getvalue).grid(row=3, column=2)

root.mainloop()