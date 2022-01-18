from tkinter import *
root=Tk()
root.title("Icons Images and ExitButton")



root.iconbitmap("./icon.ico")

exitButton= Button(root, text="Exit", command=root.quit)
exitButton.pack()

from PIL import ImageTk,Image
img= ImageTk.PhotoImage(Image.open("./image.jpg"))
label= Label(image=img)
label.pack()



root.mainloop()