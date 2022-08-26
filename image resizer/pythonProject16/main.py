from tkinter import*
from PIL import ImageTk, Image

root= Tk()
root.title("Image Resizer")
root.geometry("500x500")
root.iconbitmap("84576.png")

my_pic = Image.open("mow.png")

resized = my_pic.resize((50, 50), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)


my_label = Label(root, image=new_pic)
my_label.pack(pady=20)


root.mainloop()