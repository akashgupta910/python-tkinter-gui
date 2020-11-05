from tkinter import *

def submit():
    file = open("dance.txt", "a")
    file.write(f"\n<---------------------------> \n\nStudent name: {name_value.get()}\nAddress: {address_value.get()}\nPhone Number: {phone_no_value.get()}\nAge: {age_value.get()}\nEmail: {email_value.get()}\nMother's Name: {mother_name_value.get()}\nFather's Name: {father_name_value.get()}\n\n<--------------------------->")
    file.close()

root = Tk()
root.geometry("600x400")

Label(root, text="Student Name: ", font="comicsansms 11 bold").grid(row=0)
Label(root, text="Address: ", font="comicsansms 11 bold").grid(row=1)
Label(root, text="Phone no: ", font="comicsansms 11 bold").grid(row=2)
Label(root, text="Age: ", font="comicsansms 11 bold").grid(row=3)
Label(root, text="Email Address: ", font="comicsansms 11 bold").grid(row=4)
Label(root, text="Mother's name: ", font="comicsansms 11 bold").grid(row=5)
Label(root, text="Father's name: ", font="comicsansms 11 bold").grid(row=6)

name_value = StringVar()
address_value = StringVar()
phone_no_value = IntVar()
age_value = IntVar()
email_value = StringVar()
mother_name_value = StringVar()
father_name_value = StringVar()

name_entry = Entry(root, textvariable=name_value).grid(row=0, column=1)
address_entry = Entry(root, textvariable=address_value).grid(row=1, column=1)
phone_no_entry = Entry(root, textvariable=phone_no_value).grid(row=2, column=1)
age_entry = Entry(root, textvariable=age_value).grid(row=3, column=1)
email_entry = Entry(root, textvariable=email_value).grid(row=4, column=1)
mother_name_entry = Entry(root, textvariable=mother_name_value).grid(row=5, column=1)
father_name_entry = Entry(root, textvariable=father_name_value).grid(row=6, column=1)

Button(text="submit", font="comicsansms 11 bold", padx=15, bg="red", fg="white", command=submit).grid(row=7, column=1)

root.mainloop()