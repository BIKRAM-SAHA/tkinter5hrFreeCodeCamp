from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Window")

def openWin():
    top= Toplevel()
    top.title("New_Window")

btn=Button(root,text="Click to open win", command=openWin)
btn.pack()

root.mainloop()
