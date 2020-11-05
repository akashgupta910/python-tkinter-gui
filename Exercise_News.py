from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i % 100 == 0 and i != 0:
            final_text += "\n"
    return final_text

root = Tk()
now = datetime.now()
root.geometry("1000x700")
root.title("News India")
Label(text="News India", font="comicsansms 25 bold").pack()
Label(text=now.strftime("%d %B, %Y"), font="comicsansms 11 bold").pack()

content = []
photo = []
# n = int(input("How many files you have: "))
for i in range(0,2):
    with open(f"{i+1}.txt") as file:
        text = file.read()
        content.append(every_100(text))
        file.close()

    image = Image.open(f"{i+1}.jpg")
    image = image.resize((350, 300), Image.ANTIALIAS)
    photo.append(ImageTk.PhotoImage(image))

for i in range(0,2):
    f1 = Frame(root, width=800, height=200, pady=15)
    Label(f1, text=content[i], pady=20, padx=10).pack(side="left")
    Label(f1, image=photo[i], anchor="e").pack()
    f1.pack(anchor="w")

root.mainloop()