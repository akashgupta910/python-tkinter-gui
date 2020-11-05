from tkinter import *

def getvalue():
    print(f"The uservalue is {uservalue.get()}")
    print(f"The uservalue is {passvalue.get()}")

root = Tk()
root.geometry("900x600")
Label(root, text="Username").grid()
Label(root, text="Password").grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue).grid(row=0, column=1)
passentry = Entry(root, textvariable=passvalue).grid(row=1, column=1)

Button(text="submit", command=getvalue).grid()


root.mainloop()

# Variable Classes in Tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
