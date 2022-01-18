from tkinter import *
root=Tk()
root.title("Frame")


frame=LabelFrame(root, text="This is frame", padx=5, pady=5)
frame.pack(padx=100,pady=100)

b= Button(frame, text="Nothing here")
b2= Button(frame, text="Nothing here too")
b.grid(row=0,column=0) #notice how grid is allowed inside the frame though frame itself is pack()
b2.grid(row=1,column=1)


root.mainloop()