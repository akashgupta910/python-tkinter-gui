from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("600x400")
Label(text="You ordered food from here, what has been your expierence?", font="lucida 14").pack()
Label(text="Please Rate us.", font="lucida 10").pack()

def getValue():
    with open("rate.txt", "a") as f:
        f.write(f"<-------> \nName: {name_value.get()}\n Rating: {slider.get()} \n<-------> \n")
        f.close()
    msg.showinfo("Rate us", "Thanks for your Rating Us.")

frame1 = Frame(root, pady=10)
name_value = StringVar()
Label(frame1, text="Enter your Name:", font="lucida 11").pack()
name_entry = Entry(frame1, textvariable=name_value, width=30).pack()
frame1.pack()

slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, tickinterval=1, width=20)
slider.set(8)
slider.pack(fill='both')

frame2 = Frame(root, pady=10)
button = Button(frame2, text="Rate us", pady=5, padx=5, command=getValue).pack()
frame2.pack()

root.mainloop()