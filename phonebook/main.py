from tkinter import*
from datetime import date, datetime
import datetime
from mypeople import MyPeople
date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self,master):
        self.master = master

        self.top = Frame(master, height=150, bg='#a7a7c2')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=550, bg='white')
        self.bottom.pack(fill=X)

        self.heading= Label(self.top, text ="Phonebook", font='helvetica 15 bold', foreground='green')
        self.heading.pack()

        self.date = Label(self.top, text="Date"+date, font='helvetica 11 bold', foreground='#886e8a')
        self.date.pack()

        self.mypeople = Button(self.bottom, text ="Phonebook", font='helvetica 12 bold', width=12, foreground='#886e8a', command=self.my_people)
        self.mypeople.place(x=20,y=70)

        self.addpeople = Button(self.bottom, text="Add People", font='helvetica 12 bold', width=12, foreground='#886e8a')
        self.addpeople.place(x=20, y=110)

        self.about = Button(self.bottom, text="About", font='helvetica 12 bold', width=12, foreground='#886e8a')
        self.about.place(x=20, y=150)



    def my_people(self):
        people = MyPeople()



def main():
    root = Tk()
    app = Application(root)
    root.title('Phone book')
    root.geometry("500x500")
    root.mainloop()


if __name__ == '__main__':
    main()