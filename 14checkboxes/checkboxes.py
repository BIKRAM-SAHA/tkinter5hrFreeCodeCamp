from tkinter import *
root=Tk()
root.title("checkboxes")


var= StringVar()
var.set('none')
chkbx1= Checkbutton(root, text="python", variable= var, onvalue="python", offvalue="none") #bydeafult the onValue=1, offvlaue=0
chkbx1.pack()
chkbx2= Checkbutton(root, text="C", variable= var, onvalue="C", offvalue="none")
chkbx2.pack()



def Click():
    Label(root, text= var.get()).pack()
Button(root, text="Click", command=Click).pack()
root.mainloop()