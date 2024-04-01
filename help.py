from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os

class help_desk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")


        img_right=Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\Face_detect2.png")
        img_right=img_right.resize((1530,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img_right)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=0,y=55,width=1530,height=800)

        email_lbl=Label(first_lbl,text="krishnagupta7103@gmail.com",font=('times new roman',20,'bold'),fg="blue")
        email_lbl.place(x=600,y=220)


if __name__== "__main__":
    root=Tk()
    obj=help_desk(root)
    root.mainloop()