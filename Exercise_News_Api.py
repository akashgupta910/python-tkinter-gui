from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("900x600")
root.title("All India News - NewsApi.org")
now = datetime.now()


Label(text="Entry your Api from NewsApi.org: ", font="comicsansms 10").grid(row=1, column=1)
api_value = StringVar()
api_entry = Entry(root, textvariable=api_value).grid(row=1, column=2)

f1 = Frame(root)
Label(f1, text="All India News - NewsApi.org", font="comicsansms 20 bold", bg="black", fg="white", pady=13).pack(fill=X)
Label(f1, text=now.strftime("%d %B, %Y"), font="comicsansms 11 bold", bg="grey", fg="white", pady=4).pack(fill=X)
f1.pack(fill=X)


root.mainloop()
