from  tkinter import *
from  tkinter import messagebox

root = Tk()
root.geometry("400x400")

def msg():
    messagebox.showwarning("bewere","Stop! now! virus is detected")

button = Button(root, text="Scan virus pls", command=msg)
button.place(x=40, y=80)


root.mainloop()