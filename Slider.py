from tkinter import *
import tkinter.messagebox as msg


root = Tk()
root.geometry("900x600")
root.title("Slider in Tkinter")

# Scale(root, from_=0, to=600).pack()

def getdollar():
    print(f"You have credited {slider.get()} Dollar.")
    msg.showinfo("Account Credited", f"You have credited {slider.get()} Dollars.")

Label(text="How many Dollars you want to credit?", font="lucida 14", bg="grey", fg="white", pady=10).pack(fill=X)
slider = Scale(root, from_=0, to=200, orient=HORIZONTAL, tickinterval=100)
# slider.set(40)
slider.pack()
Button(text="Get Dollars", command=getdollar).pack()

root.mainloop()
