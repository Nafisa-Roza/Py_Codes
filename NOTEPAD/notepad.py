from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("600x700")
root.title("Roza's NOTEPAD")

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*txt')])
    if file is not None:
        content=file.read()
        entry.insert(INSERT,CONTENT)
def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def clear():
    entry.delete(1.0,END)

b1 = Button(root,text="open_file",command=open_file)
b1.place(x=10,y=10)

b2 = Button(root,text="clear",command=clear)
b2.place(x=100,y=10)

b3 = Button(root,text="save file",command=save_file)
b3.place(x=170,y=10)

entry=Text(root,height=35,width=72,wrap=WORD)
entry.place(x=10,y=110)


root.mainloop()
