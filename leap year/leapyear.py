from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("600x400")
root.title("Leap year")


def check ():
    entry_2.delete(0.0, 'end')
    year = int(entry_1.get())
    if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        s = "{} is a Leap Year . ".format(year)
    else:
        s = "{} is not a Leap Year . ".format(year)
    entry_2.insert(0.0, s)
    
b1 = Button(root,text="Give year")
b1.place(x=10,y=10)

b2 = Button(root,text="Check",command=check)
b2.place(x=10, y=200)

entry_1=Entry(root,width=40)
entry_1.place(x=10,y=110)

entry_2=Text(root,height=5,width=40,wrap=WORD)
entry_2.place(x=10,y=250)

root.mainloop()