try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

from functools import partial
from tkinter import*
import tkinter

Keyboard_App = tkinter.Tk()
Keyboard_App.title("Onscreen Keyboard")
Keyboard_App ['bg'] = '#bcd4cd'
Keyboard_App.resizable(0,0)

def select(value):
    if value == " Space ":
        entry.insert(tkinter.END, ' ')
    else:
        entry.insert(tkinter.END, value)


Label1 = Label(Keyboard_App, text="Onscreen Keyboard", font=('arial', 30, 'bold'), bg='#bcd4cd', fg="black").grid(row =0, columnspan = 40)
entry = Text(Keyboard_App, width=138, font=('arial', 10, 'bold'))
entry.grid(row =1, columnspan = 40)


buttons = ['!','q','w','e','r','t','y','u','i','o','p',
           'a','s','d','f','g','h','j','k','l',
           'z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9',
           '0','+','_','*','/','Shift',' Space ','=','Delete']

varRow = 2
varColumn = 0


for button in buttons:
    command = lambda x= button: select(x)
    if button != " Space ":
        tkinter.Button(Keyboard_App, text= button, width=5, padx=3, pady=3, bd=12, bg="#bcd4cd", activebackground="white", activeforeground="#000990", relief='raised', font=('arial', 12, 'bold'), command = command).grid(row=varRow, column=varColumn)

    if button == " Space ":
        tkinter.Button(Keyboard_App, text=button, width=118, padx=3, pady=3, bd=12, bg="#bcd4cd",  activebackground="white", activeforeground="#000990", relief='raised', font=('arial', 12, 'bold'), command=command).grid(row=6, columnspan=16)

    varColumn +=1
    if varColumn > 14 and varRow == 2:
        varColumn = 0
        varRow +=1
    if varColumn > 14 and varRow == 3:
        varColumn = 0
        varRow +=1



Keyboard_App.mainloop()