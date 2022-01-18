#importing the tkinter library
from tkinter import *

#creating the root widget the screen
root=Tk()

#creating a label widget with text "hello world"
label=Label(root,text="helloworld")

#inserting the label widget into the screen
label.pack()

#starting the mainloop
root.mainloop()