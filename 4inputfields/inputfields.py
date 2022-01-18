import tkinter
root=tkinter.Tk()


entrywidget = tkinter.Entry(root, width=50, bg="yellow", borderwidth=5)
# entrywidget.insert(0,"automatically added text")
entrywidget.pack()
# entrywidget.grid(row=0, column=0, columnspan=3)


def handleClick():
    value=entrywidget.get()
    label=tkinter.Label(root,text=value)
    label.pack()
button=tkinter.Button(root,text="Enter Text",command=handleClick)
button.pack()
root.mainloop()