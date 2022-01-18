from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("messagebox")

def infoBtnCLick():
    messagebox.showinfo("This is the header", "this is the info part")
def warningBtnCLick():
    messagebox.showwarning("This is the header", "This is the warning!!")
def errorBtnCLick():
    messagebox.showerror("This is the header", "This is the error")
def askquestionBtnCLick():
    res1=messagebox.askquestion("This is the header", "This is the askquestion")
    label1=Label(root,text=res1)
    label1.pack()
def askokcancelBtnCLick():
    res2=messagebox.askokcancel("This is the header", "This is the ok cancel question")
    label2=Label(root,text=res2)
    label2.pack()
def askyesnoBtnCLick():
    res3=messagebox.askyesno("This is the header", "This is the askyesno question")
    label3=Label(root,text=res3)
    label3.pack()


infoBtn=Button(root,text="Show Info",command=infoBtnCLick)
infoBtn.pack()
warningBtn=Button(root,text="Show Warning",command=warningBtnCLick)
warningBtn.pack()
errorBtn=Button(root,text="Show error",command=errorBtnCLick)
errorBtn.pack()
askquestionBtn=Button(root,text="Show askquestion",command=askquestionBtnCLick)
askquestionBtn.pack()
askokcancelBtn=Button(root,text="Show askokcancel",command=askokcancelBtnCLick)
askokcancelBtn.pack()
askyesnoBtn=Button(root,text="Show askyesno",command=askyesnoBtnCLick)
askyesnoBtn.pack()

root.mainloop()