from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class Student_details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variable
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()

        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # GUI first image
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
        img2 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\students3.jpeg")
        img2 =img2.resize((500,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl=Label(self.root,image=self.photoimg2)
        first_lbl.place(x=1000,y=0,width=500,height=230)

        
        # bg image        
        bgimg =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\img7.jpeg")
        bgimg =bgimg.resize((1530,610),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=230,width=1530,height=610)


        title_lbl=Label(bg_img,text="Student Details",font=("Asap Condensed",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=12,y=50,width=1500,height=500)
        # left Label Frame
        left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("Playfair Display",15,"bold"))
        left_frame.place(x=25,y=10,width=700,height=470)
        #  CURRENT course name 
        current_course_frame=LabelFrame(left_frame,bd=5,relief=RIDGE,text="Course Information",font=("Playfair Display",15,"bold"))
        current_course_frame.place(x=22,y=5,width=650,height=130)

        # department Label
        dept_lbl=Label(current_course_frame,text="Department",font=("Playfair Display",10,"bold"))
        dept_lbl.grid(row=0,column=0,padx=5,pady=15)
      # department combobox
        dept_combbox=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("Playfair Display",10,"bold"),state="readonly")
        dept_combbox['values']=("Select Department","Bachelors of Science","Bachelors of Science(IT)","Bachelors of Science(CS)")
        dept_combbox.current(0)
        dept_combbox.grid(row=0,column=1,padx=5,pady=3)
        # Course label
        course_lbl=Label(current_course_frame,text="Course",font=("Playfair Display",10,"bold"))
        course_lbl.grid(row=0,column=3,padx=5,pady=3,sticky=W)

        # Course combobox
        course_combbox=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Playfair Display",10,"bold"),state="readonly")
        course_combbox['values']=("Select Course","Bachelors of Science","Bachelors of Science(IT)","Bachelors of Science(CS)")
        course_combbox.current(0)
        course_combbox.grid(row=0,column=4,padx=5,pady=3,sticky=W)


         # Year label
        year_lbl=Label(current_course_frame,text="Year",font=("Playfair Display",10,"bold"))
        year_lbl.grid(row=1,column=0)

        # Year combobox
        year_combbox=ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("Playfair Display",10,"bold"),state="readonly")
        year_combbox['values']=("Select Year","2022-23","2024-25","2025-26")
        year_combbox.current(0)
        year_combbox.grid(row=1,column=1,padx=5,pady=3)


        # semester label
        semester_lbl=Label(current_course_frame,text="Semester",font=("Playfair Display",10,"bold"))
        semester_lbl.grid(row=1,column=3)

         # semseter combobox
        semester_combbox=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Playfair Display",10,"bold"),state="readonly")
        semester_combbox['values']=("Select Semester","1","2","3","4","5","6")
        semester_combbox.current(0)
        semester_combbox.grid(row=1,column=4,padx=5,pady=5)


         # Student details
        student_Details_frame=LabelFrame(left_frame,bd=5,relief=RIDGE,text="Student Details",font=("Playfair Display",15,"bold"))
        student_Details_frame.place(x=22,y=140,width=650,height=280)

         #StudentID details Label
        studentID_frame_lbl=Label( student_Details_frame,text="StudentID",font=("Playfair Display",10,"bold"))
        studentID_frame_lbl.grid(row=0,column=0,padx=10,pady=3,sticky=W)
        
        studentID_entry=ttk.Entry( student_Details_frame,textvariable=self.var_id,width=20,font=("Playfair Display",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=3,sticky=W)

         #Student_name details Label
        student_name_frame_lbl=Label( student_Details_frame,text="Student Name",font=("Playfair Display",10,"bold"))
        student_name_frame_lbl.grid(row=0,column=3,padx=10,pady=3,sticky=W)
      
        student_name_entry=ttk.Entry( student_Details_frame,textvariable=self.var_name,width=20,font=("Playfair Display",10,"bold"))
        student_name_entry.grid(row=0,column=4,padx=10,pady=3,sticky=W)

         #division details Label
        division_frame_lbl=Label( student_Details_frame,text="Division",font=("Playfair Display",10,"bold"))
        division_frame_lbl.grid(row=1,column=0,padx=10,pady=3,sticky=W)

      #   division_entry=ttk.Entry( student_Details_frame,textvariable=self.var_div,width=20,font=("Playfair Display",10,"bold"))
      #   division_entry.grid(row=1,column=1,padx=10,pady=3,sticky=W)
        division_combbox=ttk.Combobox(student_Details_frame,textvariable=self.var_div,width=17,font=("Playfair Display",10,"bold"),state="readonly")
        division_combbox['values']=("Select Division","A","B","C","D","E","F")
        division_combbox.current(0)
        division_combbox.grid(row=1,column=1,padx=10,pady=3)

         #roll no. details Label
        rollno_frame_lbl=Label( student_Details_frame,text="Roll no.",font=("Playfair Display",10,"bold"))
        rollno_frame_lbl.grid(row=1,column=3,padx=10,pady=3,sticky=W)

        rollno_entry=ttk.Entry( student_Details_frame,textvariable=self.var_rollno,width=20,font=("Playfair Display",10,"bold"))
        rollno_entry.grid(row=1,column=4,padx=10,pady=3,sticky=W)

         #gender details Label
        gender_frame_lbl=Label( student_Details_frame,text="Gender",font=("Playfair Display",10,"bold"))
        gender_frame_lbl.grid(row=2,column=0,padx=10,pady=0,sticky=W)

      #   gender_entry=ttk.Entry( student_Details_frame,textvariable=self.var_gender,width=20,font=("Playfair Display",10,"bold"))
      #   gender_entry.grid(row=2,column=1,padx=10,pady=3,sticky=W)
        gender_combbox=ttk.Combobox(student_Details_frame,textvariable=self.var_gender,width=17,font=("Playfair Display",10,"bold"),state="readonly")
        gender_combbox['values']=("Select Gender","Male","Female")
        gender_combbox.current(0)
        gender_combbox.grid(row=2,column=1,padx=10,pady=3)

         #DOB details Label
        DOB_frame_lbl=Label( student_Details_frame,text="DOB",font=("Playfair Display",10,"bold"))
        DOB_frame_lbl.grid(row=2,column=3,padx=10,pady=3,sticky=W)

        DOB_entry=ttk.Entry( student_Details_frame,textvariable=self.var_dob,width=20,font=("Playfair Display",10,"bold"))
        DOB_entry.grid(row=2,column=4,padx=10,pady=3,sticky=W)

         #Email details Label
        Email_frame_lbl=Label( student_Details_frame,text="Email",font=("Playfair Display",10,"bold"))
        Email_frame_lbl.grid(row=3,column=0,padx=10,pady=3,sticky=W)

        
        Email_entry=ttk.Entry( student_Details_frame,textvariable=self.var_email,width=20,font=("Playfair Display",10,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=3,sticky=W)

        #Phone details Label
        Phone_frame_lbl=Label( student_Details_frame,text="Phone no.",font=("Playfair Display",10,"bold"))
        Phone_frame_lbl.grid(row=3,column=3,padx=10,pady=3,sticky=W)
 
        Phoneno_entry=ttk.Entry( student_Details_frame,textvariable=self.var_phone,width=20,font=("Playfair Display",10,"bold"))
        Phoneno_entry.grid(row=3,column=4,padx=10,pady=3,sticky=W)

        #address details Label
        address_frame_lbl=Label( student_Details_frame,text="Address",font=("Playfair Display",10,"bold"))
        address_frame_lbl.grid(row=4,column=0,padx=10,pady=3,sticky=W)

        address_entry=ttk.Entry( student_Details_frame,textvariable=self.var_address,width=20,font=("Playfair Display",10,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=3,sticky=W)

        
        #teacher details Label
        teacher_frame_lbl=Label( student_Details_frame,text="Teacher",font=("Playfair Display",10,"bold"))
        teacher_frame_lbl.grid(row=4,column=3,padx=10,pady=3,sticky=W)

        teacher_entry=ttk.Entry( student_Details_frame,textvariable=self.var_teacher,width=20,font=("Playfair Display",10,"bold"))
        teacher_entry.grid(row=4,column=4,padx=10,pady=3,sticky=W)

        # Radiobuttons
        self.var_rd1=StringVar()
        radio_btn1=ttk.Radiobutton(student_Details_frame, variable=self.var_rd1, text="Take Sample Photo",value=YES)
        radio_btn1.grid(row=5,column=0,padx=10,pady=3,sticky=W)
        radio_btn2=ttk.Radiobutton(student_Details_frame,variable=self.var_rd1,text="No Sample Photo",value=NO)
        radio_btn2.grid(row=5,column=1,padx=10,pady=3,sticky=W)

        # Buttons
        btn_save=Button(student_Details_frame,text="Save",command=self.add_data,bd=5,width=10,bg="light blue")
        btn_save.grid(row=6,column=0,padx=10,pady=2,sticky=W)
        
        btn_update=Button(student_Details_frame,text="Update",command=self.update_data,bd=5,width=10,bg="light blue")
        btn_update.grid(row=6,column=1,padx=10,pady=2,sticky=W)
        
        btn_delete=Button(student_Details_frame,text="Delete",command=self.delete_data,bd=5,width=10,bg="light blue")
        btn_delete.grid(row=6,column=3,padx=2,pady=2,sticky=W)
        
        btn_reset=Button(student_Details_frame,text="Reset",command=self.reset_data,bd=5,width=10,bg="light blue")
        btn_reset.grid(row=6,column=4,padx=20,pady=2,sticky=W)

        btn_take_photo=Button(student_Details_frame,text="Take Photo",command=self.photoSam_data,bd=5,width=10,bg="light blue")
        btn_take_photo.grid(row=7,column=0,padx=10,pady=2,sticky=W)
        
        btn_update_photo=Button(student_Details_frame,text="Update Photo ",bd=5,width=10,bg="light blue")
        btn_update_photo.grid(row=7,column=1,padx=10,pady=2,sticky=W)

        # btn_no_photo=Button(student_Details_frame,text="No Photo",bd=5,width=10,bg="light blue")
        # btn_no_photo.grid(row=6,column=4,padx=25,pady=2,sticky=W)




          # right Label Frame
        right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("Roboto Mono",15,"bold"))
        right_frame.place(x=750,y=10,width=700,height=470)
        # Search bar
        search_frame=LabelFrame(right_frame,bd=5,relief=RIDGE,text="Student Details",font=("Playfair Display",15,"bold"))
        search_frame.place(x=25,y=10,width=650,height=80)

        search_label=Label(search_frame,text="Search by:",bg="light blue",font=("Playfair Display",12,"bold"))
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combbox=ttk.Combobox(search_frame,font=("Playfair Display",10,"bold"),state="readonly")
        search_combbox['values']=("Select","Roll no.","Phone no.")
        search_combbox.current(0)
        search_combbox.grid(row=0,column=1,padx=5,pady=5)

        btn_search=Button(search_frame,text="Search",bd=5,width=10,bg="light blue")
        btn_search.grid(row=0,column=2,padx=10,pady=2,sticky=W)

        btn_Showall=Button(search_frame,text="ShowAll",bd=5,width=10,bg="light blue")
        btn_Showall.grid(row=0,column=3,padx=15,pady=2,sticky=W)

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=27,y=100,width=647,height=320)

        # Scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("dept","course","year","Sem","Id","name","div","roll_no","gender","dOB","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="Id")

        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Div")
        self.student_table.heading("roll_no",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dOB",text="DOB")

        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo_Sample")
        
        self.student_table["show"]="headings"
        
           
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)

        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dOB",width=100)

        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100) 
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    def add_data(self):
        if self.var_dept.get()=="Select department" or self.var_course.get()=="Select Course" :
           messagebox.showerror("Error","All Fields required")
      
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Krishna@7103",database="new info")
                my_curs=conn.cursor()
                my_curs.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_course.get(),
                    self.var_dept.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_rollno.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_rd1.get()                                                                            
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
   #   fetched data from database        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Krishna@7103",database="new info")
        my_curs=conn.cursor()
        my_curs.execute("Select * from  students")
        data=my_curs.fetchall()
        
        if len(data)!=0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
              self.student_table.insert("",END,values=i)
              conn.commit()
        conn.close()
        
        # get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3])
        self.var_id.set(data[4]),                                                                             
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_rd1.set(data[14])
            
            
           
           
         # update function
     
    def update_data(self):
        if self.var_id.get()=="" :
            messagebox.showerror("Error","Student id must be requiured",parent=self.root)
        else:
            try:
                Upadated=messagebox.askyesno("Updated Data","Do you really want to update this data",parent = self.root)
                if Upadated>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Krishna@7103",database="new info")
                    my_curs=conn.cursor()
                    my_curs.execute("update students set dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Teacher=%s,Address=%s,Photo_Sample=%s where id=%s",(
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_rollno.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_rd1.get(),
                        self.var_id.get()         
                    ))
                else:
                    if not Upadated:
                        return  
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                conn.close()
                self.fetch_data()
            except Exception  as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
                  
            
         
         
         # Delete function
    def delete_data(self) :
        if self.var_id.get()=="" :
            messagebox.showerror("Error","Student id must be requiured",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you really wants to delete the data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Krishna@7103",database="new info")
                    my_curs=conn.cursor()
                    sql="delete From students where id=%s"
                    val=(self.var_id.get(),)
                    my_curs.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successfully", "Record deleted Successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"{str(es)}", parent=self.root)
               
              #  Reset data
              
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_id.set("")      
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),

        self.var_name.set(""),
        self.var_div.set("Select Division"),
        self.var_rollno.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_rd1.set(""),
    




      #   =========PhotoSample========
    def photoSam_data(self):
        if self.var_id.get()=="":
             messagebox.showerror("Error","Student id must be requiured",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Krishna@7103",database="new info")
                my_curs=conn.cursor()
                my_curs.execute("select * from students")
                my_result=my_curs.fetchall()
                ID=0
                for x in my_result:
                    ID+=1
                my_curs.execute("UPDATE students set dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Teacher=%s,Address=%s,Photo_Sample=%s where id=%s",(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),

                    self.var_div.get(),
                    self.var_rollno.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),

                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_rd1.get(),
                    self.var_id.get()==ID+1  #########   
                                                                                   
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                 
               #   frontal Face detector from opencv
                face_finder=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropper(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_finder.detectMultiScale(gray,1.3,5)
                 #   1.3=scale factor and 5 is the min number  of neigbours(it will increase and decrease according to img quality)
                 
                    for (x,y,w,h) in faces:
                       face_cropper=img[y:y+h,x:x+w]
                       return face_cropper

                cap=cv2.VideoCapture(0)
                img_id=0
                # ret,frame =cap.read()
                while True:              
                    ret,cam_frame=cap.read()
                    if face_cropper(cam_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropper(cam_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        img_path_folder=r"data/user." + str(ID)+"."+str(img_id)+".jpg"
                        cv2.imwrite(img_path_folder,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Face Cropped",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
        # If no face is detected, wait for a while before trying again           
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Your data has been generated")
            except Exception as es:
                messagebox.showerror("Error", f"{str(es)}", parent=self.root)




    

if __name__== "__main__":
    root=Tk()
    obj=Student_details(root)
    root.mainloop()

       
            
    