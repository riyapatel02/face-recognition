from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np


class Train_data:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="skyblue")

        #Label--->
        title_lbl = Label(self.root,text="Train Data Set",font=("times new roman",25,"bold"),bg="pink",fg="black")
        title_lbl.place(x=0,y=0,width=1380,height= 50)
        #TopImage-->
        img_top = Image.open("train1.webp")
        img_top=img_top.resize((1400,430),Image.ANTIALIAS)
        self.photo_img= ImageTk.PhotoImage(img_top)

        label = Label(self.root,image=self.photo_img)
        label.place(x=5,y=55,width=1350,height=430)

        #Button-->
        
        but_1 = Button(self.root,text='Train Data',command=self.trainData_classifier,font=("times new roman",25,"bold"),bd=3,relief=RIDGE,bg="black",fg="pink")
        but_1.place(x=428,y=445,width=500,height=40)

        # BottomImage-->
        img_botm = Image.open("trai.jpg")
        img_botm=img_botm.resize((1400,200),Image.ANTIALIAS)
        self.photo_img1= ImageTk.PhotoImage(img_botm)

        label = Label(self.root,image=self.photo_img1)
        label.place(x=5,y=490,width=1350,height=200)

    #----------->function---->
    def trainData_classifier(self):
        data_dir =("data")
        path =[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces =[]
        ids=[]

        for image in path:
            img= Image.open(image).convert('L') #Gray Scale Image
            imageNp = np.array(img,'uint8') #converting image into grid using numpy for better performance
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        #--------->Train the classifier----->
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        tmsg.showinfo("Result","Training datasets completed!")


if __name__=="__main__":
    root = Tk()
    obj = Train_data(root)
    root.mainloop()