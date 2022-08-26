from tkinter import*
import random
root = Tk()
root.title("Number Guessing")
root.geometry('500x200')

attempts = 3
answer = random.randint(1,9)

def check_answer():
    global attempts
    global text

    attempts -=1
    guess = int(entry_window.get())

    if answer == guess:
        text.set("you win!")
        btn_check.pack_forget()

    elif attempts == 0:
        text.set("You are out of attempts!")
        btn_check.pack_forget()

    elif guess<answer:
        text.set("Incorrect! you have "+str(attempts)+" attempts remaining!")

    elif guess>answer:
        text.set("Incorrect! you have " + str(attempts) + " attempts remaining!")

    else:
        text.set("You Lose!")


    return

label= Label(root, text="Guess the number between 1-9")
label.pack()

entry_window = Entry(root, width=40, borderwidth=4 )
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer, foreground='blue')
btn_check.pack()

btn_quit = Button(root, text="Quit", command= root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 3 attempts!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()
