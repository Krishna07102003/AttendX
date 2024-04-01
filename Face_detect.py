from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recog:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition",font=("Asap Condensed",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    #   FIRST image
        img_left =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\Face_detect1.png")
        img_left =img_left.resize((650,700),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_lbl=Label(self.root,image=self.photoimg_left)
        first_lbl.place(x=0,y=55,width=650,height=700)

        img_right=Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\Face_detect2.png")
        img_right=img_right.resize((950,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img_right)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=650,y=55,width=950,height=700)

        
        b1_1=Button(first_lbl,text="Face Recognition",cursor="hand2",command=self.Face_Recognite,font=("Asap Condensed",15,"bold"),bg="dark green",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)


#     def train_classifier(self):
#         (images, labels, names, id) = train_classifier()
#         # create a list of sample images for each person in the dataset

# # create a face recognition model and train it on the dataset
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.train(images, np.array(labels))

# # save the trained model to a file
#         clf.write("trainer.xml")
# Face Recognition
    def mark_atten(self,i,r,name,d):
        with open("Face.csv","r+",newline="\n") as f:
            my_data=f.readlines()
            name_list=[]
            for line in my_data:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (name not in name_list) and (i not in name_list)):
                now=datetime.now()
                date_1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S") 
                f.writelines(f"\n{i},{r},{name},{d},{dtString},{date_1},Present")

    def Face_Recognite(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):  
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                ids,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Krishna@7103",database="new info")
                my_curs=conn.cursor()

                my_curs.execute("select Name from students where id="+str(ids))
                name=my_curs.fetchone()
                name = "+".join(name)
                

                my_curs.execute("select Roll_No from students where id=" + str(ids))
                r = my_curs.fetchone()
                r = "+".join(r)

                my_curs.execute("select dep from students where id=" + str(ids))
                d = my_curs.fetchone()
                d = "+".join(d)

                my_curs.execute("select id from students where id=" + str(ids))
                i = my_curs.fetchone()
                i = "+".join(i)
                   

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{name}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_atten(i,r,name,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap = cv2.VideoCapture(0)

        while True:
            ret,img=cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recogntion",img)

            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()


        





if __name__== "__main__":
    root=Tk()
    obj=Face_Recog(root)
    root.mainloop()