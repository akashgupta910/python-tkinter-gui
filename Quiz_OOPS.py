# Functions:-
# 1. favicon(ico_filename)
# 2. menu(menu_names)
# 3. heading(text)
# 4. radiobuttons(radio_names)
# 5. button(text)
# 6. statusbar(text)

from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")

    def favicon(self, filename):
        self.wm_iconbitmap(filename)

    def menu(self, *args):
            menu = Menu(self)
            for menu_name in args:
                menu.add_command(label=f"{menu_name}")
            self.config(menu=menu)

    def heading(self, text):
        Label(self, text=text, bg="grey", fg="white", font="lucida 18 bold", pady=8).pack(side=TOP, fill=X)


    def radiobuttons(self, *args):
        var = StringVar()
        var.set("r")
        for radio in args:
            Radiobutton(self, text=f"{radio}", variable=var, value=f"{radio}", font="lucida 9").pack()

    def button(self, text):
        Button(self, text=text, bg="grey", fg="white", pady=5, padx=5).pack()

    def statusbar(self, text):
        var = StringVar()
        var.set(text)
        Label(self, textvariable=var, relief=SUNKEN, pady=10, font="lucida 12", bg="grey", fg="white").pack(side=BOTTOM, fill=X)

if __name__ == '__main__':
    window = GUI()
    window.favicon("file/notepad.ico")
    window.title("Notepad")
    window.menu("File", "Edit", "Code", "Help")
    window.heading("Connecting to the World")
    window.radiobuttons("chowmin", "Chilli", "Kurkure")
    window.button("Click")
    window.statusbar("Ready")
    window.mainloop()


