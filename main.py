from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
from student import Student
import os
from trainData import Train_data
from facerecognizer import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from tkinter import messagebox as tmsg

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #Background Image-->
        # self.bg = ImageTk.PhotoImage(file = "bgimg.jpg")
        # self.bg_img = Label(self.root,image= self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        # First image-->
        img = Image.open("BestFacialRecognition.jpg")
        img=img.resize((600,130),Image.ANTIALIAS) #resize the img(width,height) & ANTIALIAS-->Convert high level img into low level
        self.photo_img = ImageTk.PhotoImage(img)

        label = Label(self.root,image=self.photo_img)
        label.place(x=0,y=0,width=500,height=130)

        # Second image-->
        img2 = Image.open("facialrecognition.png")
        img2=img2.resize((500,150),Image.ANTIALIAS) #resize the img(width,height) & ANTIALIAS-->Convert high level img into low level
        self.photo_img1 = ImageTk.PhotoImage(img2)

        label = Label(self.root,image=self.photo_img1)
        label.place(x=450,y=0,width=500,height=150)

        #Third image-->
        img3 = Image.open("images.jpg")
        img3=img3.resize((430,150),Image.ANTIALIAS)
        self.photo_img2= ImageTk.PhotoImage(img3)

        label = Label(self.root,image=self.photo_img2)
        label.place(x=930,y=0,width=430,height=150)
        #Label-->
        title_lbl = Label(self.root,text="Face Recognition Attendance System Software",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=130,width=1360,height=40)

        #BackgroundImage-->
        bg_img = Image.open("bgimg.jpg")
        bg_img=bg_img.resize((2000,1000),Image.ANTIALIAS)
        self.photo_img_bg= ImageTk.PhotoImage(bg_img)

        label = Label(self.root,image=self.photo_img_bg)
        label.place(x=0,y=170,width=2000,height=1000)

        #DateTime func--->
        def time():
            string = strftime('%H:%M:%S %p')
            tym_lbl.config(text= string)
            tym_lbl.after(1000, time)

        tym_lbl = Label(title_lbl,font=("times new roman",12,"bold"),bg="skyblue",fg="black")
        tym_lbl.place(x=0,y=0,width=110,height= 35)
        time()

        
        #Student image-->
        img4 = Image.open("stud2.webp")
        img4=img4.resize((220,170),Image.ANTIALIAS)
        self.photo_img4= ImageTk.PhotoImage(img4)

        but1 = Button(self.root,image=self.photo_img4,cursor="hand2",command=self.student_details)
        but1.place(x=150,y=210,width=220,height=170)

        but_1 = Button(self.root,text='Student Details',command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=150,y=370,width=220)

        # Detect Face-->
        img5 = Image.open("face_detector1.jpg")
        img5=img5.resize((220,170),Image.ANTIALIAS)
        self.photo_img5= ImageTk.PhotoImage(img5)

        but1 = Button(self.root,image=self.photo_img5,command=self.facedetector_func,cursor="hand2")
        but1.place(x=420,y=210,width=220,height=170)

        but_1 = Button(self.root,text='Face Detector',command=self.facedetector_func,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=420,y=370,width=220)

        # Attendence-->
        
        img_a = Image.open("atten1.jpg")
        img_a=img_a.resize((220,220),Image.ANTIALIAS)
        self.photo_imga= ImageTk.PhotoImage(img_a)

        but1 = Button(self.root,image=self.photo_imga,command=self.attendance_func,cursor="hand2")
        but1.place(x=690,y=210,width=220,height=170)

        but_1 = Button(self.root,text='Attendence',command=self.attendance_func,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=690,y=370,width=220)

        # Help Desk Button-->
        img6 = Image.open("help.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photo_img6= ImageTk.PhotoImage(img6)

        but1 = Button(self.root,image=self.photo_img6,command=self.help_func,cursor="hand2")
        but1.place(x=960,y=210,width=220,height=170)

        but_1 = Button(self.root,text='Help Desk',command=self.help_func,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=960,y=370,width=220)
  

        # Train Face Button-->
        img7 = Image.open("train1.webp")
        img7=img7.resize((220,170),Image.ANTIALIAS)
        self.photo_img7= ImageTk.PhotoImage(img7)

        but1 = Button(self.root,command=self.traindata_func,image=self.photo_img7,cursor="hand2")
        but1.place(x=150,y=450,width=220,height=170)

        but_1 = Button(self.root,text='Train Data',command=self.traindata_func,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=150,y=600,width=220)

        # Photos Button--8
        img8 = Image.open("faceimg.png")
        img8=img8.resize((220,170),Image.ANTIALIAS)
        self.photo_img8= ImageTk.PhotoImage(img8)

        but1 = Button(self.root,image=self.photo_img8,command=self.open_img,cursor="hand2")
        but1.place(x=420,y=450,width=220,height=170)

        but_1 = Button(self.root,text='Photos',command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=420,y=600,width=220)

        # Developer Face Button-->
        img9 = Image.open("developer.webp")
        img9=img9.resize((220,170),Image.ANTIALIAS)
        self.photo_img9= ImageTk.PhotoImage(img9)

        but1 = Button(self.root,image=self.photo_img9,command=self.developer_func,cursor="hand2")
        but1.place(x=690,y=450,width=220,height=170)

        but_1 = Button(self.root,text='Developer',command=self.developer_func,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=690,y=600,width=220)

        # Exit Button-->
        img10 = Image.open("exit.jpg")
        img10=img10.resize((220,170),Image.ANTIALIAS)
        self.photo_img10= ImageTk.PhotoImage(img10)

        but1 = Button(self.root,command=self.exit_func,image=self.photo_img10,cursor="hand2")
        but1.place(x=960,y=450,width=220,height=170)

        but_1 = Button(self.root,command=self.exit_func,text='Exit',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        but_1.place(x=960,y=600,width=220)

    #------>Functions Button for studentDetails(main.py)-------->

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app =Student(self.new_window)

    #------>Function for Exit(main.py)------>
    def exit_func(self):
        self.exit_func= tmsg.askyesno("Exit","Are you sure exit this app",parent=self.root)
        if self.exit_func>0:
            self.root.destroy()
        else:
            return

        
    #-------->Function for Photos(main.py)------>
    def open_img(self):
        os.startfile("data")
        
    #------>Functions Button for Train Data(main.py)-------->
    def traindata_func(self):
        self.new_window = Toplevel(self.root)
        self.app =Train_data(self.new_window)

    #------>Functions Button for Face Detector(main.py)-------->
    def facedetector_func(self):
        self.new_window = Toplevel(self.root)
        self.app =Face_Recognition(self.new_window)
    
    #------>Functions Button for Attendance(main.py)-------->
    def attendance_func(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    #------>Functions Button for Developer(main.py)-------->
    def developer_func(self):
        self.new_window = Toplevel(self.root)
        self.app=Developer(self.new_window)

    #------>Functions Button for Developer(main.py)-------->
    def help_func(self):
        self.new_window = Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()