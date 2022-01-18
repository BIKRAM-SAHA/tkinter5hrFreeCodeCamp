from tkinter import *
root=Tk()
root.title("Simple Calculator App")

e=Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def ButtonClick(val):
    try:
        if(e.get()=="Invalid Expression"):
            e.delete(0,END)
        if(val=="clear"):
            e.delete(0, END)
        elif(val=="add"):
            e.insert(END,"+")
        elif(val=="subtract"):
            e.insert(END,"-")
        elif(val=="multiply"):
            e.insert(END,"*")
        elif(val=="divide"):
            e.insert(END,"/")
        elif(val=="equal"):
            result=eval(e.get())
            e.delete(0, END)
            e.insert(0,result)
        else:
            if(e.get()=="0"):
                e.delete(0,END)
            e.insert(END, val)
    except:
        e.delete(0,END)
        e.insert(0,"Invalid Expression")

button_0=Button(root, text="0", padx=40, pady=20, command=lambda: ButtonClick(0))
button_1=Button(root, text="1", padx=40, pady=20, command=lambda: ButtonClick(1))
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: ButtonClick(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: ButtonClick(3))
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: ButtonClick(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: ButtonClick(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: ButtonClick(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: ButtonClick(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: ButtonClick(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: ButtonClick(9))
button_add=Button(root, text="+", padx=40, pady=20, command=lambda: ButtonClick("add"))
button_equal=Button(root, text="=", padx=40, pady=20, command=lambda: ButtonClick("equal"))
button_clear=Button(root, text="CE", padx=36, pady=20, command=lambda: ButtonClick("clear"))
button_multiply=Button(root, text="*", padx=40, pady=20, command=lambda: ButtonClick("multiply"))
button_divide=Button(root, text="/", padx=40, pady=20, command=lambda: ButtonClick("divide"))
button_subtract=Button(root, text="-", padx=40, pady=20, command=lambda: ButtonClick("subtract"))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4,column=1)

button_add.grid(row=1,column=3)
button_clear.grid(row=4,column=0)
button_equal.grid(row=4,column=2)
button_multiply.grid(row=2,column=3)
button_divide.grid(row=3,column=3)
button_subtract.grid(row=4,column=3)

root.mainloop()