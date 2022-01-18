from tkinter import *
root=Tk()

label1=Label(root,text="|this is label 1.just to make it longer|")
label2=Label(root,text="|this is label 2|")
label3=Label(root,text="|this is label 3|")


label1.grid(row=0, column=0)
label3.grid(row=1,column=1)
label2.grid(row=2, column=1)


root.mainloop()