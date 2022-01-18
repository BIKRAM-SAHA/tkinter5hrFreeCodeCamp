from tkinter import *
root=Tk()

def onClick():
    label=Label(root,text="You clicked the button")
    label.pack()

# button=Button(root,text="Click Button", state=DISABLED)
# button=Button(root,text="Click Button", padx=49, pady=9)
# button=Button(root,text="Click Button", foreground="blue",background="yellow")
# button=Button(root,text="Click Button", fg="blue",bg="yellow")

button=Button(root,text="Click Button", command=onClick)

button.pack()

root.mainloop()