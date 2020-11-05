from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("Notepad")
root.wm_iconbitmap("file/notepad.ico")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()

root.mainloop()
