#pip install pyttxs3
#pip install pywin32

from tkinter import*
import pyttsx3

root=Tk()
root.title("heyyyyy")
root.geometry("500x500")

def talk():
    engine = pyttsx3.init()
    engine.say(my_entry.get())
    engine.runAndWait()

my_entry = Entry(root, font=("Arial",28),bd=8)
my_entry.pack(pady=20)

my_button=Button(root, text="Speak", fg="blue", bd=8, bg="powder blue", command=talk)
my_button.pack()



root.mainloop()