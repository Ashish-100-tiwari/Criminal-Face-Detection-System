from cmath import exp
import imp
from logging import root
from re import L
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk

class student :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System ")
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1355,height=510)
        # left label
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("time new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=670,height=480)
        # image 1in
        img_left=Image.open(r"C:\Users\hp\Documents\vscode's\.vscode\criminal face recognation system\college_images\facialrecognition.png")
        img_left=img_left.resize((650,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=8,y=0,width=650,height=80)

        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course ",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=80,width=650,height=100)
        # department
        dep_label=Label(current_course_frame,text="Department",font=("time new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("time new roman",10,"bold"),state="readonly",width=17)
        dep_combo["values"]=("select Department","computer","IT","Civil","Machnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # # course
        course_label=Label(current_course_frame,text="Course",font=("time new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,font=("time new roman",10,"bold"),state="readonly",width=17)
        course_combo["values"]=("select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        # # year
        year_label=Label(current_course_frame,text="Year",font=("time new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,font=("time new roman",10,"bold"),state="readonly",width=17)
        year_combo["values"]=("select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)
        # # semester
        sem_label=Label(current_course_frame,text="Semester",font=("time new roman",10,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=2,sticky=W)
        sem_combo=ttk.Combobox(current_course_frame,font=("time new roman",10,"bold"),state="readonly",width=17)
        sem_combo["values"]=("select sem","sem1","sem2","sem3","sem4")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=2,sticky=W)

        # class student infor
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="student info ",font=("time new roman",12,"bold"))
        class_student_frame.place(x=5,y=180,width=650,height=270)
        # id label
        id=Label(class_student_frame,text="ID Number ",font=("time new roman",10,"bold"),bg="white")
        id.grid(row=0,column=0,padx=10,sticky=W)
        # Id entry
        id_entry=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        id_entry.grid(row=0,column=1,padx=10,sticky=W)
        # id name
        Name=Label(class_student_frame,text="Enter Number ",font=("time new roman",10,"bold"),bg="white")
        Name.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        # Id name entry
        Name_entry=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        # class divion
        class_div_label=Label(class_student_frame,text="Class Division",font=("time new roman",10,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        # Id name entry
        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         #Roll no
        roll_no_label=Label(class_student_frame,text="Roll number",font=("time new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        #Roll no entry
        roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #Gender label
        gender_label=Label(class_student_frame,text="Gender",font=("time new roman",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        #gender entry
        gender_label=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        gender_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #DOB label
        dob_label=Label(class_student_frame,text="DOB",font=("time new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        #gender entry
        dob_label=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        dob_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        # email
        email_label=Label(class_student_frame,text="Email :",font=("time new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        #email entry
        email_label=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        email_label.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #Phone
        Phone_label=Label(class_student_frame,text="Phone :",font=("time new roman",10,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        #phone entry
        Phone_label=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        Phone_label.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #Address
        Address_label=Label(class_student_frame,text="Address :",font=("time new roman",10,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        #phone entry
        Address_label=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        Address_label.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        #Teacher 
        teacher_label=Label(class_student_frame,text="Teacher:",font=("time new roman",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        #Teacher entry
        teacher_label=ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        teacher_label.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        #radio button
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take photo sample ",value="yes")
        radiobtn1.grid(row=6,column=0)
        radiobtn1=ttk.Radiobutton(class_student_frame,text="No photo sample ",value="yes")
        radiobtn1.grid(row=6,column=1)
        # button frame
        btn_frame= Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=645,height=35)
        
        save_btn=Button(btn_frame,text="Save",width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=10)

        update_btn=Button(btn_frame,text="Update",width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=10)

        delete_btn=Button(btn_frame,text="Delete",width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=10)

        reset_btn=Button(btn_frame,text="Reset",width=5,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10)

        take_photo_btn=Button(btn_frame,text="Take photo",width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4,padx=10)

        update_btn=Button(btn_frame,text="update Photo",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=5,padx=10)
        # right label
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("time new roman",12,"bold"))
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
        sem_label=Label(current_course_frame,text="Semester",font=("time new roman",10,"bold"),bg="white")
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
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
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

        







if __name__=="__main__":
    root=Tk()
    obj=student(root)        
    root.mainloop()