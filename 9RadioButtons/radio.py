from tkinter import *
root=Tk()
root.title("radio")

var=IntVar()
var.set("2")
RadioBtn1= Radiobutton(root, text="option1", variable=var, value=1) #command argument is also avialable like Button()
RadioBtn2= Radiobutton(root, text="option2", variable=var, value=2)
RadioBtn3= Radiobutton(root, text="option3", variable=var, value=3)


RadioBtn1.pack()
RadioBtn2.pack()
RadioBtn3.pack()


def click():
    label=Label(root, text=var.get())
    label.pack()
getVar=Button(root, text="get Var", command=click)
getVar.pack()
root.mainloop()