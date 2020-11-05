from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("600x400")

def save_as():
    msg.askyesno("Confirm Save As","File Already Exists. Do you want to replace it?" )

def update():
    msg.askretrycancel("Connection Failed", "Please check your Internet Connection and Try Again.")


menu = Menu(root)
m1 = Menu(menu, tearoff=0)
m1.add_command(label="Save As", command=save_as)
m1.add_command(label="Check for Update", command=update)
menu.add_cascade(label="File", menu=m1)


root.config(menu=menu)


root.mainloop()
