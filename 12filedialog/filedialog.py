from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("Files")

def openfile():
    global file
    file=filedialog.askopenfilename(title="Choose",initialdir="./",filetypes=[("jpg files","*.jpg"),("All files","*.*")])
    Label(root,text=f"choosen File is {file}").pack()

btn=Button(root,text="Add file", command=openfile).pack()


root.mainloop()
