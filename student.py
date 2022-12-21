from cmath import exp
from fileinput import close
import imp
from logging import root
from re import L
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from turtle import update, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System ")
# -------------------------------------------------------Variable 
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
# image 1
        img=Image.open(r"C:\Users\hp\Documents\vscode's\.vscode\criminal face recognation system\college_images\bg1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
# image 2
        img1=Image.open(r"C:\Users\hp\Documents\vscode's\.vscode\criminal face recognation system\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
# image 3
        img2=Image.open(r"C:\Users\hp\Documents\vscode's\.vscode\criminal face recognation system\college_images\bg1.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
# background image 
        img3=Image.open(r"C:\Users\hp\Documents\vscode's\.vscode\criminal face recognation system\college_images\dev.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="CRIMINAL FACE DETECTION SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1355,height=510)
        # left label
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Detail",font=("time new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=670,height=480)
        # image 1in
        img_left=Image.open(r"C:\Users\hp\Documents\vscode's\.vscode\criminal face recognation system\college_images\facialrecognition.png")
        img_left=img_left.resize((650,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=8,y=0,width=650,height=80)

        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Case ",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=80,width=650,height=100)
        # department
        dep_label=Label(current_course_frame,text="Type of crime",font=("time new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",10,"bold"),state="readonly",width=17)
        dep_combo["values"]=("select crime","Murder","narcotics","robbery","digital")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # # course
        course_label=Label(current_course_frame,text="Case Type",font=("time new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",10,"bold"),state="readonly",width=17)
        course_combo["values"]=("select Case Type","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        # # year
        year_label=Label(current_course_frame,text="Year",font=("time new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",10,"bold"),state="readonly",width=17)
        year_combo["values"]=("select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)
        # # semester
        sem_label=Label(current_course_frame,text="Area",font=("time new roman",10,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=2,sticky=W)
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("time new roman",10,"bold"),state="readonly",width=17)
        sem_combo["values"]=("select Area","up","Delhi","uk","Mp")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=2,sticky=W)

        # class student infor
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Criminal info",font=("time new roman",12,"bold"))
        class_student_frame.place(x=5,y=180,width=650,height=270)
        # id label
        id=Label(class_student_frame,text="ID Number ",font=("time new roman",10,"bold"),bg="white")
        id.grid(row=0,column=0,padx=10,sticky=W)
        # Id entry
        id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("time new roman",13,"bold"))
        id_entry.grid(row=0,column=1,padx=10,sticky=W)
        # id name
        Name=Label(class_student_frame,text="Enter Name ",font=("time new roman",10,"bold"),bg="white")
        Name.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        # Id name entry
        Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("time new roman",13,"bold"))
        Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        # class divion
        class_div_label=Label(class_student_frame,text="Cell Division",font=("time new roman",10,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        # Id name entry
        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("time new roman",13,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("time new roman",10,"bold"),state="readonly",width=20)
        div_combo["values"]=("1","2","3")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         #Roll no
        roll_no_label=Label(class_student_frame,text="Cell number",font=("time new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        #Roll no entry
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("time new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #Gender label
        gender_label=Label(class_student_frame,text="Gender",font=("time new roman",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        #gender entry
        # gender_label=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("time new roman",13,"bold"))
        # gender_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gen_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("time new roman",10,"bold"),state="readonly",width=20)
        gen_combo["values"]=("Male","female","other")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB label
        dob_label=Label(class_student_frame,text="DOB",font=("time new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        #dob entry
        dob_label=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("time new roman",13,"bold"))
        dob_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        # email
        email_label=Label(class_student_frame,text="identification Mark",font=("time new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        #email entry
        email_label=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("time new roman",13,"bold"))
        email_label.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #Phone
        Phone_label=Label(class_student_frame,text="Phone :",font=("time new roman",10,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        #phone entry
        Phone_label=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("time new roman",13,"bold"))
        Phone_label.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #Address
        Address_label=Label(class_student_frame,text="Last Spotted",font=("time new roman",10,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        #address entry
        Address_label=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("time new roman",13,"bold"))
        Address_label.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        #Teacher 
        teacher_label=Label(class_student_frame,text="Officer Name",font=("time new roman",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        # Teacher entry
        teacher_label=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("time new roman",13,"bold"))
        teacher_label.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample ",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample ",value="no")
        radiobtn1.grid(row=6,column=1)
        # button frame
        btn_frame= Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=645,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=10)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=10)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=10)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10)

        take_photo_btn=Button(btn_frame,text="Take photo",command=self.generate_dataset,width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4,padx=10)

        update_btn=Button(btn_frame,text="update Photo",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=5,padx=10)
        # right label
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Ciminal Detail",font=("time new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=670,height=480)
        # image right
        img_right=Image.open(r"C:\Users\hp\Documents\vscode's\.vscode\criminal face recognation system\college_images\facialrecognition.png")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=8,y=0,width=650,height=80)
# ---------------------search system------------------------
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="search system",font=("time new roman",12,"bold"))
        search_frame.place(x=5,y=80,width=650,height=70)
# label
        search_label=Label(search_frame,text="Search by:",font=("time new roman",10,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        sem_label=Label(current_course_frame,text="Area",font=("time new roman",10,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=2,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("time new roman",10,"bold"),state="readonly",width=15)
        search_combo["values"]=("select sem","roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1 ,padx=2,pady=2,sticky=W)
        # entry
        search_label=ttk.Entry(search_frame,width=15,font=("time new roman",13,"bold"))
        search_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        # btn
        search_btn=Button(search_frame,text="Search",width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10)
        # showall
        showall_btn=Button(search_frame,text="Show all",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=10)
# table frame--------------------------------------------------
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=150,width=650,height=300)
        # sroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Type of crime")
        self.student_table.heading("course",text="Case Type")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Case Type")
        self.student_table.heading("id",text="CriminalId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Identification Mark")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Last spotted")
        self.student_table.heading("teacher",text="Officer Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
# 
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor) 
        self.fetch_data()
        # ============================function 
    def add_data(self):
        if self.var_dep.get()=="Type of crime"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Field are Requied",parent=self.root)
        else:        
             try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ashishtiwari@100",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_semester.get(),
                                                                        self.var_std_id.get(),
                                                                        self.var_std_name.get(),
                                                                        self.var_div.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get()
                                                                         ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success "," Criminal details has been added",parent=self.root)                                                       
             except Exception as es :
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
# =========================================fetch data===
    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="Ashishtiwari@100",database="face")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from student")
          data=my_cursor.fetchall()

          if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data :
                    self.student_table.insert("",END,values=i)
                conn.commit()
          conn.close()
# =======================get cursor========================  
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
# =================================== update function

    def update_data(self):
        if  self.var_dep.get()=="Type of crime"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All Field are Requied",parent=self.root)
        else: 
            try: 
                Upadate=messagebox.askyesno("Update","Do you want to update  this id details ",parent=self.root)
                if Upadate>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Ashishtiwari@100",database="face")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set Dep=%s, course=%s,Year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                                       ))

                else: 
                    if not Upadate :   
                        return 
                messagebox.showinfo("Success","Criminal detail successful update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#     delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
                messagebox.showerror("Error","criminal id must be requid ",parent=self.root)
        else: 
            try:
                delete=messagebox.askyesno("Criminal Delete page ","Do you want to delete this Criminal", parent=self.root)          
                if delete >0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Ashishtiwari@100",database="face")
                        my_cursor=conn.cursor()
                        sql="delete from student where student_id=%s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,val)
                else:
                    if not delete :
                                return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully delete criminal details ")
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#    reset 
    def reset_data(self):
        self.var_dep.set("Type of crime")
        self.var_course.set("Select Case Type")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Area")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
# ========================================== generate data set 
#     def generate_dataset(self):
#         if  self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
#              messagebox.showerror("Error","All Field are Requied",parent=self.root)
#         else: 
#              try: 
#                 conn=mysql.connector.connect(host="localhost",username="root",password="Ashishtiwari@100",database="face")
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("select * from student")
#                 myresult = my_cursor.fetchall()
#                 id=0
#                 for x in myresult:
#                     id+=1
#                 my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
#                                                                                                                 self.var_dep.get(),
#                                                                                                                 self.var_course.get(),
#                                                                                                                 self.var_year.get(),
#                                                                                                                 self.var_semester.get(),
#                                                                                                                 self.var_std_name.get(),
#                                                                                                                 self.var_div.get(),
#                                                                                                                 self.var_roll.get(),
#                                                                                                                 self.var_gender.get(),
#                                                                                                                 self.var_dob.get(),
#                                                                                                                 self.var_email.get(),
#                                                                                                                 self.var_phone.get(),
#                                                                                                                 self.var_address.get(),
#                                                                                                                 self.var_teacher.get(),
#                                                                                                                 self.var_radio1.get(),
#                                                                                                                 self.var_std_id.get()==id+1
#                                                                                                                                        ))
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 self.close()
# # =======================================load pre define data on face 
#                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
#                 def face_cropped(img):
#                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                         faces=face_classifier.detectMultiScale(gray,1.3,5)
#                 # scaling factor 1.3 , minimum neighbor =5
#                         for(x,y,w,h) in faces:
#                                 face_cropped=img[y:y+h,x:x+w]
#                                 return face_cropped
                                
#                 cap=cv2.VideoCapture(0)
#                 img_id=0
#                 while  True :
#                         my_frame=cap.read()
#                         if face_cropped(my_frame) is not None :
#                                 img_id+=1
#                                 face=cv2.resize(face_cropped(my_frame),(450,450)) 
#                                 face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)       
#                                 file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
#                                 cv2.imwrite(file_name_path,face)
#                                 cv2.putText(face,str(img_id),(50,50),cv2.FRONT_HERSHEY_COMPLEX,2,(0,255,0),2)
#                                 cv2.imshow("cropped Face",face)

#                         if cv2.waitKey(1)==13 or int(img_id)==100:
#                             break
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo("Result","Generating data sets compled !")
#              except Exception as es :
#                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    def generate_dataset(self):      
        if self.var_dep.get()=="Type of crime"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Field are Requied",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ashishtiwari@100",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_phone.get(),                                                                                                                
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                                                                                ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()


                    ################Load Predefined data on face frontals from opencv################
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #Scaling factor=1.3
                        #minimum Neighbour=5


                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Student(root)        
    root.mainloop()