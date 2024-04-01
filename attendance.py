from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
mydata.clear()
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Sheet")

        self.var_std_id=StringVar()
        self.var_roll=StringVar()
        self.var_dept=StringVar()
        self.var_name=StringVar()
        self.var_date=StringVar()

        
        # GUI first image
        img =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\students1.jpeg")
        img =img.resize((800,230),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=800,height=230)

        # GUI second image
        img1 =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\students2.jpeg")
        img1 =img1.resize((800,230),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=800,y=0,width=800,height=230)

         # bg image        
        bgimg =Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\Face_detect2.png")
        bgimg =bgimg.resize((1530,610),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=230,width=1530,height=610)

        title_lbl=Label(bg_img,text="Attendance",font=("Asap Condensed",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=12,y=50,width=1500,height=500)

          # left Label Frame
        left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Attendance Details",font=("Playfair Display",15,"bold"))
        left_frame.place(x=25,y=10,width=700,height=470)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=20,y=15,width=650,height=300)

        Attendance_ID_frame_lbl=Label(left_inside_frame,text="StudentID", bg="white",font=("Playfair Display",10,"bold"))
        Attendance_ID_frame_lbl.grid(row=0,column=0,padx=35,pady=28,sticky=W)
        
        Attendance_ID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_std_id,font=("Playfair Display",10,"bold"))
        Attendance_ID_entry.grid(row=0,column=1,padx=3,pady=28,sticky=W)

        Attendance_name_frame_lbl=Label(left_inside_frame,text="Student Name",bg="white",font=("Playfair Display",10,"bold"))
        Attendance_name_frame_lbl.grid(row=0,column=3,padx=10,pady=3,sticky=W)
      
        Attendance_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("Playfair Display",10,"bold"))
        Attendance_name_entry.grid(row=0,column=4,padx=10,pady=3,sticky=W)

        Attendance_dept_frame_lbl=Label(left_inside_frame,text="Department",bg="white",font=("Playfair Display",10,"bold"))
        Attendance_dept_frame_lbl.grid(row=1,column=0,padx=35,pady=3,sticky=W)

        Attendance_dept_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dept,font=("Playfair Display",10,"bold"))
        Attendance_dept_entry.grid(row=1,column=1,padx=3,pady=3,sticky=W)

        Attendance_rollno_frame_lbl=Label(left_inside_frame,text="Roll no",bg="white",font=("Playfair Display",10,"bold"))
        Attendance_rollno_frame_lbl.grid(row=1,column=3,padx=10,pady=3,sticky=W)

        Attendance_rollno_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_roll,font=("Playfair Display",10,"bold"))
        Attendance_rollno_entry.grid(row=1,column=4,padx=10,pady=3,sticky=W)

        date_frame_lbl=Label(left_inside_frame,text="Date",bg="white",font=("Playfair Display",10,"bold"))
        date_frame_lbl.grid(row=2,column=0,padx=35,pady=30,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("Playfair Display",10,"bold"))
        date_entry.grid(row=2,column=1,padx=3,pady=3,sticky=W)

        btn_import=Button(left_inside_frame,text="Import csv",command=self.impcsv,bd=5,width=10,bg="light blue")
        btn_import.grid(row=6,column=0,padx=30,pady=2,sticky=W)
        
        btn_export=Button(left_inside_frame,text="Export csv",command=self.exportcsv,bd=5,width=10,bg="light blue")
        btn_export.grid(row=6,column=1,padx=10,pady=2,sticky=W)
        
        btn_reset=Button(left_inside_frame,text="Reset",bd=5,command=self.reset_data,width=10,bg="light blue")
        btn_reset.grid(row=6,column=3,padx=2,pady=2,sticky=W)
        
        # btn_reset=Button(left_inside_frame,text="Reset",bd=5,width=10,bg="light blue")
        # btn_reset.grid(row=6,column=4,padx=20,pady=2,sticky=W)
    #   right frame
        right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Attendance Details",font=("Playfair Display",15,"bold"))
        right_frame.place(x=750,y=10,width=720,height=470)

        right_inside_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        right_inside_frame.place(x=30,y=15,width=650,height=400)
#   Scrollbar
        scroll_x=ttk.Scrollbar(right_inside_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_inside_frame,orient=VERTICAL)

        self.attendanceReportTable=ttk.Treeview(right_inside_frame,columns=("StudentID","Roll no","Student Name","Department","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("StudentID",text="StudentID")
        self.attendanceReportTable.heading("Student Name",text="Student Name")
        self.attendanceReportTable.heading("Department",text="Department")
        self.attendanceReportTable.heading("Roll no",text="Roll no")
        self.attendanceReportTable.heading("Date",text="Date")

        self.attendanceReportTable["show"]="headings"

        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # fetch_data

    def fetchdata(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children()) 
        for i in rows:
            self.attendanceReportTable.insert("", END,values=i)
# import csv
    def impcsv(self):
        global mydata
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV FIle","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    # export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data found","Not have data to export",parent=self.root)
                return False
            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV FIle","*.csv"),("All File","*.*")),parent=self.root)
            with open(file_name,mode= 'w',newline='')as myfile:
                exp_write=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo('Success','Data has been successfully Exported to'+os.path.basename(file_name)+ "Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}" ,parent=self.root)

    def get_cursor(self,event=""):
        curs_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(curs_row)
        rows=content["values"]
        self.var_std_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dept.set(rows[3])
        self.var_date.set(rows[4])
        

    def reset_data(self):
        self.var_std_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_date.set("")









if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()