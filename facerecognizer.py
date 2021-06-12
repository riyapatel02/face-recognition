from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import mysql.connector
from time import strftime
from datetime import datetime
from mysql.connector import cursor
import cv2
import os
from mysql.connector import connection
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="green")


        #Label--->
        title_lbl = Label(self.root,text="Face Recognition",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1380,height= 50)
        #Image1-->
        img1 = Image.open("face_detector1.jpg")
        img1=img1.resize((650,700),Image.ANTIALIAS)
        self.photo_img= ImageTk.PhotoImage(img1)

        label = Label(self.root,image=self.photo_img)
        label.place(x=5,y=55,width=650,height=637)

        #Image2-->
        img2 = Image.open("facedetector2.jpg")
        img2=img2.resize((705,690),Image.ANTIALIAS)
        self.photo_img1= ImageTk.PhotoImage(img2)

        label2 = Label(self.root,image=self.photo_img1)
        label2.place(x=650,y=55,width=705,height=637)

        #Button-->
        but_1 = Button(label2,text='Face Recognition',command=self.face_recog,font=("times new roman",15,"bold"),bd=1,relief=RIDGE,bg="darkgreen",fg="white")
        but_1.place(x=260,y=590,width=180,height=30)

    #----->Attendence Function--------->
    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry= line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)and (n not in name_list)and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtStrig = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtStrig},{d1},Present")


    #--->Function of Face Recognition----->

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn= mysql.connector.connect(host="localhost",username="root",password="riya789868",database="facerecognitionsystem")
                my_cursor = conn.cursor()

                my_cursor.execute("select stu_name from student where Stu_id="+str(id))
                n = my_cursor.fetchone()
                n ="+".join(n)

                    
                my_cursor.execute("select roll from student where Stu_id="+str(id))
                r = my_cursor.fetchone()
                r ="+".join(r)

                my_cursor.execute("select dep from student where Stu_id="+str(id))
                d = my_cursor.fetchone()
                d ="+".join(d)

                my_cursor.execute("select Stu_id from student where Stu_id="+str(id))
                i = my_cursor.fetchone()
                i ="+".join(i)



                if confidence>77:
                    cv2.putText(img,f"Id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendence(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
                video_cap.release()
                cv2.destroyAllWindows()


if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()