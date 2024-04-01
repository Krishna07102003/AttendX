from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import numpy as np
import os


class Train_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Trained Data",font=("Asap Condensed",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\students1.jpeg")
        img =img.resize((500,230),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=500,height=230)

        # GUI second image
        img1 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\students2.jpeg")
        img1 =img1.resize((500,230),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=500,y=0,width=500,height=230)

    #    GUI third image
        img2 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\img8.jpeg")
        img2 =img2.resize((550,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl=Label(self.root,image=self.photoimg2)
        first_lbl.place(x=1000,y=0,width=550,height=230)

# Button
        b1_1=Button(self.root,text="Train Data",cursor="hand2",command=self.train_data,font=("Asap Condensed",15,"bold"),bg="dark green",fg="white")
        b1_1.place(x=0,y=230,width=1530,height=60)


        bgimg =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\main_img.png")
        bgimg =bgimg.resize((1530,610),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=290,width=1530,height=610)


    def train_data(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Data",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Completed")




if __name__== "__main__":
    root=Tk()
    obj=Train_Data(root)
    root.mainloop()