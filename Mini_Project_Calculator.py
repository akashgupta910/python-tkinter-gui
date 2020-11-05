from tkinter import *

def click(event):
    global var
    text = event.widget.cget("text")

    if text == "=":
        if var.get().isdigit():
            value1 = int(var.get())
        try:
            value1 = eval(value.get())
        except Exception as e:
            print(e)
            var.set("Invalid Input")
            value.update()

        var.set(value1)
        value.update()

    elif text == "C":
        var.set("")
        value.update()
    else:
        var.set(var.get() + text)
        value.update()

root = Tk()
root.geometry("500x700")
root.title("Calculator")
# root.wm_iconbitmap("file/calculator.ico")

var = StringVar()
var.set("")

value = Entry(root, textvariable=var, font="lucida 40 bold")
value.pack(side=TOP, fill=X, pady=15, padx=15)

n = 9
for i in range(0, 3):
    frame = Frame(root)
    button = Button(frame, text=str(n), font="lucida 35 bold", padx=30, bg="grey", fg="white")
    button.pack(side=LEFT)
    button.bind("<Button-1>", click)

    button = Button(frame, text=str(n-1), font="lucida 35 bold", padx=30, bg="grey", fg="white")
    button.pack(side=LEFT)
    button.bind("<Button-1>", click)

    button = Button(frame, text=str(n-2), font="lucida 35 bold", padx=30, bg="grey", fg="white")
    button.pack(side=LEFT)
    button.bind("<Button-1>", click)

    n -= 3
    frame.pack()

frame = Frame(root)
button = Button(frame, text=".", font="lucida 35 bold", padx=40, bg="gainsboro", fg="black")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame, text="0", font="lucida 35 bold", padx=30, bg="grey", fg="white")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame, text="C", font="lucida 35 bold", padx=30, bg="gainsboro", fg="black")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(root)
button = Button(frame, text="/", font="lucida 35 bold", padx=40, bg="SkyBlue3", fg="white")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame, text="*", font="lucida 35 bold", padx=33, bg="SkyBlue3", fg="white")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame, text="-", font="lucida 35 bold", padx=40, bg="SkyBlue3", fg="white")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(root)
button = Button(frame, text="+", font="lucida 35 bold", padx=35, bg="SkyBlue3", fg="white")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame, text="=", font="lucida 35 bold", padx=30, bg="gainsboro", fg="black")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button = Button(frame, text="%", font="lucida 35 bold", padx=30, bg="SkyBlue3", fg="white")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()


root.mainloop()

