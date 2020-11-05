from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, pady=9, font="lucida 13", bg="black", fg="white")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def create_button(self, inptext):
        Button(self, text=inptext, padx=6, pady=6, bg="grey", fg="white").pack()

if __name__ == '__main__':
    window = GUI()
    window.create_button("Click Me")
    window.status()
    window.mainloop()