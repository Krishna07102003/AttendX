from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Studentdetails import Student_details
from Face_detect import Face_Recog
from Training_data import Train_Data
from attendance import Attendance
from help import help_desk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # GUI first image
        img =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\img0.jpeg")
        img =img.resize((500,230),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=500,height=230)

        # GUI second image
        img1 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\img4.jpeg")
        img1 =img1.resize((500,230),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=500,y=2,width=500,height=230)

    #    GUI third image
        img2 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\AttendX_logo.jpg")
        img2 =img2.resize((500,230),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img2)

        first_lbl=Label(self.root,image=self.photoimg9)
        first_lbl.place(x=1000,y=0,width=500,height=230)

        # bg image        
        bgimg =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\main_img.png")
        bgimg =bgimg.resize((1530,610),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=230,width=1530,height=610)


        title_lbl=Label(bg_img,text="AttendX",font=("Asap Condensed",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        # for button 1

        img3 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\img7.jpeg")
        img3 =img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg4,command=self.Student_detail,cursor="hand2")
        b1.place(x=100,y=120,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.Student_detail,cursor="hand2",font=("Asap Condensed",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=100,y=320,width=220,height=35)
        
        # for face detector

        img_face =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\Face_detect2.png")
        img_face =img_face.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img_face)

        b2=Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b2.place(x=350,y=120,width=220,height=220)

        b2_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data,font=("Asap Condensed",15,"bold"),bg="white",fg="navy blue")
        b2_1.place(x=350,y=320,width=220,height=35)


        # for attendance

        img_a =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\attendance_img.jpg")
        img_a =img_a.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img_a)

        b3_1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Attendance_data,)
        b3_1.place(x=600,y=120,width=220,height=220)

        b3_1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance_data,font=("Asap Condensed",15,"bold"),bg="white",fg="navy blue")
        b3_1_1.place(x=600,y=320,width=220,height=35)
    # for train data
        img_train =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\img9.jpeg")
        img_train =img_train.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img_train)

        b3_1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Train_data)
        b3_1.place(x=850,y=120,width=220,height=220)

        b3_1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.Train_data,font=("Asap Condensed",15,"bold"),bg="white",fg="navy blue")
        b3_1_1.place(x=850,y=320,width=220,height=35)


        # for help desk

        img4 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\help_img.jpg")
        img4 =img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.helpl)
        b1.place(x=1100,y=120,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.helpl,font=("Asap Condensed",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=1100,y=320,width=220,height=35)

        # Functions for directing Student_details Page
    def Student_detail(self):
         self.new_window=Toplevel(self.root)
         self.app=Student_details(self.new_window)

    def  Train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train_Data(self.new_window)


    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recog(self.new_window)

    def Attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def helpl(self):
        self.new_window=Toplevel(self.root)
        self.app=help_desk(self.new_window)
            


if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()