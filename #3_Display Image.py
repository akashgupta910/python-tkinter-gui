from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("1000x600")

photo = PhotoImage(file="img.png")
label = Label(image=photo)
label.pack()

# For Jpg image

# image = Image.open("img.jpg")
# img = ImageTk.PhotoImage(image)
# label_img = Label(image=img)
# label_img.pack()



root.mainloop()