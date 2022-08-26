from tkinter import *
import pygame
from tkinter import filedialog
root = Tk()
root.geometry('1000x500')
root.title('Play Music')
root.configure(bg='#7caac4')

def createwidgets():
    TrackLabel = Label(root, text='Select Audio Track : ', bg='#7caac4')
    TrackLabel.pack()
    TrackLabelEntry = Entry(root)
    TrackLabelEntry.pack()

createwidgets()

pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title='choose a song', filetypes=(("mp3 Files", "*.mp3"),))
    print(song)

song_box = Listbox(root, bg='white',width=60)
song_box.pack(pady=20)

pause_btn = PhotoImage(file='pause122.png')
play_btn = PhotoImage(file='button12.png')
stop_btn = PhotoImage(file='stop122.png')

controls_frame = Frame(root)
controls_frame.pack()


pause_button = Button(controls_frame, image=pause_btn, borderwidth=0)
play_button = Button(controls_frame, image=play_btn, borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn, borderwidth=0)

play_button.grid(row=0, column=1)
pause_button.grid(row=0, column=0)
stop_button.grid(row=0, column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(Label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(Label="Add songs", command=add_song)




root.mainloop()