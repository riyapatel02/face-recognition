from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import mysql.connector
from mysql.connector import cursor
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="blue")

        #Label--->
        title_lbl = Label(self.root,text="Developer",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1380,height= 50)
        #TopImage-->
        img_top = Image.open("dev.jpg")
        img_top=img_top.resize((1400,650),Image.ANTIALIAS)
        self.photo_img= ImageTk.PhotoImage(img_top)

        label = Label(self.root,image=self.photo_img)
        label.place(x=5,y=55,width=1350,height=638)

        #frame-->
        main_frame = Frame(self.root,bd=2,bg="black")
        main_frame.place(x=940,y=60,width=400,height=500)

        #Developer Image-->
        img_dev = Image.open("dev.jpg")
        img_dev=img_dev.resize((100,100),Image.ANTIALIAS)
        self.photo_img1= ImageTk.PhotoImage(img_dev)

        label = Label(main_frame,image=self.photo_img1)
        label.place(x=300,y=0,width=100,height=100)

        #Developer Info-->
        dep_lbl = Label(main_frame,text="Hello,I am a Developer",font=("times new roman",12,"bold"),bg="black",fg="white")
        dep_lbl.place(x=0,y=5)







if __name__=="__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()