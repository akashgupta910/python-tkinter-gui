from tkinter import *

def upload():
    statusvar.set("Uploading...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Uploaded.")

root = Tk()
root.geometry("900x600")
root.title("Status Bar in Tkinter")

statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, pady=10, font="lucida 12")
sbar.pack(side=BOTTOM, fill=X)

Button(text="upload", command=upload).pack()

root.mainloop()

