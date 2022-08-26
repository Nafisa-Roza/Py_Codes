from tkinter import *
import pymysql
from addpeople import AddPeople

from tkinter import messagebox
from updatepeople import Update

con = pymysql.connect(host="localhost", user="root", password="", db="phoneaddressbook1")
cur = con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500")
        self.title("My people")

        self.top = Frame(self, height=150, bg="White")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="#7a6e80")
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text="my people", font='helvetica 15 bold', foreground='#7a6e80')
        self.heading.pack()

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        self.listBox = Listbox(self.bottom, width=45, height=27)
        self.listBox.grid(row=0, column=40, padx=(0,0))

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        cur.execute("select * from addressbook")
        persons = cur.fetchall()
        count = 0

        for person in persons:
            self.listBox.insert(count,str(person[0]))
            count +=1



        self.scroll.grid(row=0, column=1, sticky=N + S)

        btnadd = Button(self.bottom, text="Add", width=12, font='helvetica 12 bold', foreground='#886e8a', command=self.add_people)
        btnadd.grid(row=0, column=0, padx=20, pady=10, sticky=N)

        btnupdate = Button(self.bottom, text="update", width=12, font='helvetica 12 bold', foreground='#886e8a', command=self.update_people)
        btnupdate.grid(row=0, column=0, padx=20, pady=50, sticky=N)

        btndisplay = Button(self.bottom, text="Display", width=12, font='helvetica 12 bold', foreground='#886e8a')
        btndisplay.grid(row=0, column=0, padx=20, pady=90, sticky=N)

        btndelete = Button(self.bottom, text="Delete", width=12, font='helvetica 12 bold', foreground='red')
        btndelete.grid(row=0, column=0, padx=20, pady=130, sticky=N)

    def add_people(self):
        add_page = AddPeople()

    def update_people(self):
        select_item = self.listBox.curselection()
        person = self.listBox.get(select_item)
        person_name = person.split(".")[0]

        updatepage = Update(person_name)