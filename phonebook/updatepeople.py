from tkinter import *
import pymysql

from tkinter import messagebox
con = pymysql.connect(host="localhost", user="root", password="", db="phoneaddressbook1")
cur = con.cursor()

class Update(Toplevel):
    def __init__(self,person_name):
        Toplevel.__init__(self)
        self.geometry("500x500")
        self.title("Update")

        self.top = Frame(self, height=250, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="#71808a")
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text="Update person", font='helvetica 15 bold', foreground='#71808a')
        self.heading.pack()

        #______________________________________________________________

        self.label_name = Label(self.bottom, text="Name", font='helvetica 12 bold', foreground='black', width=7)
        self.label_name.place(x=49, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=164, y=40)
        # _______________________________________________________

        self.label_email = Label(self.bottom, text="Email", font='helvetica 12 bold', foreground='black', width=7)
        self.label_email.place(x=49, y=98)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=164, y=98)
        # _______________________________________________________

        self.label_phone = Label(self.bottom, text="Phone", font='helvetica 12 bold', foreground='black', width=7)
        self.label_phone.place(x=49, y=147)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.place(x=164, y=147)

        # _______________________________________________________

        self.label_address = Label(self.bottom, text="Address", font='helvetica 12 bold', foreground='black', width=7)
        self.label_address.place(x=49, y=196)

        self.entry_address = Entry(self.bottom, width=30, bd=4)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.place(x=164, y=196)

        button = Button(self.bottom, text="Done")
        button.grid(padx=240, pady=400, sticky=N)

        print("person name", person_name)

        query = cur.execute("select * from addressbook where person_name='"+person_name+"'")


        result = cur.fetchone()
        self.person_name = person_name

        person_email = result[1]
        person_phone = result[2]
        person_address = result[3]

        print("person email"+person_email)



