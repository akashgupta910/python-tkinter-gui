from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("Code of GUI")
title_label = Label(text='''Grand Theft Auto V is an action-adventure video game developed by Rockstar North and published \n by Rockstar Games. It was released in September 2013 for PlayStation 3 and Xbox 360, in November 2014 for PlayStation \n 4 and Xbox One, and in April 2015 for Microsoft Windows. It is the first main entry in the Grand Theft Auto \nseries since 2008's Grand Theft Auto IV. Set within the fictional state of San Andreas, based on Southern Cal\nifornia, the single-player story follows three criminals and their efforts to commit heists while under pressure f\nrom a government agency. The open-world design lets players freely roam San Andreas' open countryside and the \nfictional city of Los Santos, based on Los Angeles.'''
                    ,bg="red", fg="white", padx = 33, pady = 35, font="comicsansms 11 bold", borderwidth=3, relief=SUNKEN)
# title_label.pack(side="bottom", fill=X)
title_label.pack(side="left", fill=Y, padx=14, pady=16)
root.mainloop()


"""
# Important Label Options :

text - add the text
bg  - background
fg  - foreground
font  - sets of font
        1. font=("comicsansms", 11, "bold")
        2. font="comicsansms 11 bold"
        
padx  - x padding
pady  - y padding
relief  - border styling - SUNKEN, RAISED, GROOVE, RIDGE 

# Important Packs :

anchor = "ne", "nw", "se", "sw"
side = top, bottom, left, right - default:top
fill
padx
pady
    
"""

