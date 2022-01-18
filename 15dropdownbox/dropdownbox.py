from tkinter import *
root=Tk()
root.title("dropboxes")

var=StringVar()
var.set("none")
drop= OptionMenu(root, var, "Monday", "Tuesday", "Wednesday")
drop.pack()

var2=StringVar()
var2.set("none")
options=["Thursday", "Friday", "Saturday", "Sunday"]
drop2= OptionMenu(root, var2, *options)
drop2.pack()



def Click():
    Label(root, text="var= "+var.get()).pack()
    Label(root, text="var2= "+var2.get()).pack()

btn=Button(root,text="get Value", command=Click)
btn.pack()
root.mainloop()