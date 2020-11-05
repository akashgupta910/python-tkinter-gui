from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)

        with open(file, "r") as f:
            textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file

    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")

    else:
        with open(file, "w") as f:
            f.write(textarea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("About Notepad", "It is a Simple Text Editor for Computer and a basic text-editing program which enables computer users to create documents.")

if __name__ == '__main__':

    root = Tk()
    root.geometry("900x600")
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("file/notepad.ico")

    # Menu
    mymenu = Menu(root)
    menu_1 = Menu(mymenu, tearoff=0)
    menu_1.add_command(label="New", command=newFile)
    menu_1.add_command(label="Open", command=openFile)
    menu_1.add_command(label="Save", command=saveFile)
    menu_1.add_separator()
    menu_1.add_command(label="Exit", command=quitApp)
    mymenu.add_cascade(label="File", menu=menu_1)

    menu_2 = Menu(mymenu, tearoff=0)
    menu_2.add_command(label="Cut", command=cut)
    menu_2.add_command(label="Copy", command=copy)
    menu_2.add_command(label="Paste", command=paste)
    mymenu.add_cascade(label="Edit", menu=menu_2)

    menu_3 = Menu(mymenu, tearoff=0)
    menu_3.add_command(label="About", command=about)
    mymenu.add_cascade(label="Help", menu=menu_3)

    root.config(menu=mymenu)

    # Textarea
    textarea = Text(root, font="lucida 10")
    textarea.pack(fill=BOTH, expand=True)
    file = None

    # ScrollBar
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

    root.mainloop()
