import sys
from tkinter import *
from tkinter import messagebox
import time
from playsound import playsound


root = Tk()
root.title('Alarm Clock')
root.geometry("600x400")

def update():
    my_label.config(text="New Text")

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    my_label.config(text = hour + ":" + minute + ":" + second+" "+am_pm)
    my_label.after(1000, clock)
    my_label12.config(text = day)



my_label = Label(root, text = "",font = ("meaw.ttf" , 48), fg="white", bg="blue")
my_label.pack(pady=20)

my_label12 = Label(root, text =(""),font=("meaw.ttf", 14))
my_label12.pack(pady = 10)

clock()
#my_label.after(5000,update)




 

root.mainloop()