from tkinter import *
from PIL import ImageTk,Image
root=Tk()

img1=ImageTk.PhotoImage(Image.open('img1.jpg').resize((600,600)))
img2=ImageTk.PhotoImage(Image.open('img2.jpg').resize((600,600)))
img3=ImageTk.PhotoImage(Image.open('img3.jpg').resize((600,600)))
img4=ImageTk.PhotoImage(Image.open('img4.jpg').resize((600,600)))
img5=ImageTk.PhotoImage(Image.open('img5.jpg').resize((600,600)))

img_list=[img1,img2,img3,img4,img5]


imgPos=[0]
label=Label(root, image=img_list[imgPos[0]])
label.grid(row=0, column=0, columnspan=3)

def showStatus():
    status=Label(root,text=f"Image {imgPos[0]+1} of {len(img_list)}", bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back():
    if(imgPos[0]>0):
        imgPos[0]=imgPos[0]-1
        label.configure(image=img_list[imgPos[0]])
    if(imgPos[0]==0):
        backButton["state"]=DISABLED
    if(forwardButton["state"]==DISABLED and imgPos[0]!=len(img_list)-1):
        forwardButton["state"]=NORMAL
    showStatus()


def forward():
    if(imgPos[0]<len(img_list)-1):
        imgPos[0]=imgPos[0]+1
        label.configure(image=img_list[imgPos[0]])
    if(imgPos[0]==len(img_list)-1):
        forwardButton["state"]=DISABLED
    if(backButton["state"]==DISABLED and imgPos[0]!=0):
        backButton["state"]=NORMAL
    showStatus()
    

backButton=Button(root,text="<<",command=lambda: back())
exitButton=Button(root,text="EXIT",command=root.quit)
forwardButton=Button(root,text=">>", command=lambda: forward())
showStatus()

if(imgPos[0]==0):
        backButton["state"]=DISABLED
if(imgPos[0]==len(img_list)-1):
        forwardButton["state"]=DISABLED


backButton.grid(row=1,column=0)
exitButton.grid(row=1,column=1)
forwardButton.grid(row=1,column=2,pady=10)


root.mainloop()