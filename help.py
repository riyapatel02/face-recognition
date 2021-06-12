from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import mysql.connector
from mysql.connector import cursor
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="cyan")

        #Label--->
        title_lbl = Label(self.root,text="Help Desk",font=("times new roman",25,"bold"),bg="black",fg="cyan")
        title_lbl.place(x=4,y=2,width=1350,height= 50)
        #TopImage-->
        img_top = Image.open("helpdesk.jpeg")
        img_top=img_top.resize((1400,650),Image.ANTIALIAS)
        self.photo_img= ImageTk.PhotoImage(img_top)

        label = Label(self.root,image=self.photo_img)
        label.place(x=4,y=55,width=1350,height=638)
        
        #Label--->
        hlp_lbl = Label(label,text="Email: riyapatel022000@gmail.com",font=("times new roman",12,"bold"),bg="black",fg="cyan")
        hlp_lbl.place(x=520,y=170)



if __name__=="__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()