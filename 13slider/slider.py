from tkinter import *
root=Tk()
root.title("Slider")
root.geometry("500x500")



vertical=Scale(root, from_=0, to=500)
vertical.pack()


horizontal=Scale(root, from_=0, to=500, orient=HORIZONTAL)
horizontal.pack()



def resize():
    root.geometry(f"{horizontal.get()}x{vertical.get()}")
Button(root, text="Click to resize", command=resize).pack()
root.mainloop()