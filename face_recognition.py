from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import date, datetime

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x700+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition System",font=("time new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1370,height=40)

        img_left = Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\face_detector1.jpg")
        img_left = img_left.resize((650,700),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        label1 = Label(self.root,image=self.photoimg_left)
        label1.place(x=0,y=40,width=650,height=700)

        img_right = Image.open(r"C:\Users\rkt98\OneDrive\Documents\e books\criminal face recognation system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_right = img_right.resize((950,700),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        label2 = Label(self.root,image=self.photoimg_right)
        label2.place(x=650,y=40,width=950,height=700)

        b2=Button(label2,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("time new roman",18,"bold"),bg="red",fg="white")
        b2.place(x=360,y=590,width=200,height=40)
###########Attendance###############

    def mark_attendance(self,i,r,n,d):
        with open("ashish.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



# ###########face recognition#####

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feature=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
            
            coord=[]
            
            for (x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                # print(id)
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="Ashishtiwari@100",database="face")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"  # Ensure n is a valid string

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"  # Ensure r is a valid string

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"  # Ensure d is a valid string
                
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                if confidence>77:
                    cv2.putText(img,f"Cellno.:{123}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{'ashish'}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Type of crime:{'robbery'}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Criminal_id:{546}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap=cv2.VideoCapture(0)

        while True:
            ret,img=videocap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Welcome to Face Recognition',img)

            if cv2.waitKey(1)==13:
                break
        videocap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
