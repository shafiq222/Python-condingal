from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("main")

def topwin() :
    top = Toplevel()
    top.geometry("190x100")
    top.title("toplevel")
    l2 = Label(top, text="This is my leveling screen")
    l2.pack()

    top.mainloop()

l = Label(root, text="This is a root window not like that of a plant")
btn=Button(root, text="Click and open a new window", command=topwin)

l.pack()
btn.pack()

root.mainloop()