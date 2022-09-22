import qrcode
from tkinter import *
root=Tk()

root.title("QR Code Generator")
content=StringVar()
filename=StringVar()
def exitt():
    root.destroy()

def create():
    userwish=content.get()
    myfile=filename.get()
    img=qrcode.make(userwish)
    img.save(myfile+".jpg")

Label(root,text="Create a QR for your Purpose").grid(row=0,column=0)
Label(root,text="QR Description Here:--").grid(row=1,column=0)
a=Entry(root,textvariable=content,width=40).grid(row=1,column=1)
Label(root).grid(row=2,column=0)
Label(root,text="File Name:--").grid(row=3,column=0)
b=Entry(root,textvariable=filename,width=40).grid(row=3,column=1)
x=Button(root,text="Exit",command=exitt).grid(row=4,column=0)
y=Button(root,text="OK",command=create).grid(row=4,column=1)

root.mainloop()













# userwish=input("Write the content:  ")
# filename=input("Input File name:  ")
# img=qrcode.make(userwish)
# img.save(filename+".jpg")
