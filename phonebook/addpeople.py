from tkinter import *
from tkinter import messagebox
import pymysql

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x550")
        self.title("Add new")

        self.top = Frame(self, height=150, bg="#a7a7c2")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="#a7a7c2")
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text="Add New", font='helvetica 15 bold', foreground='#7a6e80')
        self.heading.pack()
#_______________________________________________________

        self.label_name = Label(self.bottom, text="Name", font='helvetica 12 bold', foreground='black', width=7)
        self.label_name.place(x=49,y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0,"enter name")
        self.entry_name.place(x=164,y=40)
# _______________________________________________________

        self.label_email = Label(self.bottom, text="Email", font='helvetica 12 bold', foreground='black',width=7)
        self.label_email.place(x=49, y=98)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "enter email")
        self.entry_email.place(x=164, y=98)
# _______________________________________________________

        self.label_phone = Label(self.bottom, text="Phone", font='helvetica 12 bold', foreground='black', width=7)
        self.label_phone.place(x=49, y=147)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, "enter phone")
        self.entry_phone.place(x=164, y=147)

# _______________________________________________________

        self.label_address = Label(self.bottom, text="Address", font='helvetica 12 bold', foreground='black', width=7)
        self.label_address.place(x=49, y=196)

        self.entry_address = Entry(self.bottom, width=30, bd=4)
        self.entry_address.insert(0, "enter name")
        self.entry_address.place(x=164, y=196)


        button = Button(self.bottom, text="Done", command=self.add_people)
        button.grid( padx=240, pady=400, sticky=N)

    def add_people(self):
        person_name = self.entry_name.get()
        person_email = self.entry_email.get()
        person_phone = self.entry_phone.get()
        person_address = self.entry_address.get()

        if person_name=="" or person_email=="" or person_phone=="" or person_address=="":
            messagebox.showinfo("fill all")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", db="phoneaddressbook1")
            cur = con.cursor()
            cur.execute(
                "insert into addressbook values('"+ person_name +"','"+ person_email +"','"+ person_phone +"','"+ person_address +"')"
            )
            messagebox.showinfo("Done")
            cur.execute("commit")
            cur.close()

