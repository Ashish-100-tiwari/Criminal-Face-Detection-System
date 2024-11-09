import imp
from logging import root
from tkinter import*
from tkinter import*
import tkinter
import os
from tkinter import ttk
from PIL import Image,ImageTk
from criminal import Criminal
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from Help import Help

class Face_Recognition_System :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Criminal Face Detection System")
# image 1 "C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\bg1.jpg"
        img=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\bg1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
# image 2
        img1=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
# image 3
        img2=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\bg1.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
# background image 
        img3=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\dev.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
# student button
        img4=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\c.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.criminal_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Criminal Details",command=self.criminal_details,cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=250,width=150,height=40)
#Detect face button 
        img5=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\faci.png")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=500,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=250,width=150,height=40)
#Attendance Face button       
        img6=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\face_detector1.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendence_data,cursor="hand2")
        b1.place(x=800,y=100,width=150,height=150)
# Attendance
        b1_1=Button(bg_img,text="Detection",command=self.attendence_data,cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=250,width=150,height=40) 
# Help face button
        img7=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\help.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,command=self.help_data,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=150,height=150)

        b1_1=Button(bg_img,command=self.help_data,text="Help Desk",cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=250,width=150,height=40)
#Train face button
        img8=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\clock.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=350,width=150,height=150)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=500,width=150,height=40)
#Photos face button
        img9=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\kpng.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=350,width=150,height=150)

        b1_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=500,width=150,height=40)
#Developer face button
        img10=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\kpng.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,command=self.developer_data,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=350,width=150,height=150)

        b1_1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=500,width=150,height=40)
#Exit face button
        img11=Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\exit.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,command=self.iExit,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=350,width=150,height=150)

        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=500,width=150,height=40)

    def open_img(self):
        os.startfile("data")    
# =================================================function button
    def criminal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Criminal(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)        

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
                self.root.destroy()
        else:
                return

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)        
    root.mainloop()