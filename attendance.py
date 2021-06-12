from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import csv
from tkinter import filedialog

#global variable:
mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="skyblue")

        #--->Variables----->
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attend_status = StringVar()



        # First image-->
        img = Image.open("student3.jpg")
        img=img.resize((700,180),Image.ANTIALIAS) #resize the img(width,height) & ANTIALIAS-->Convert high level img into low level
        self.photo_img = ImageTk.PhotoImage(img)

        label = Label(self.root,image=self.photo_img)
        label.place(x=3,y=3,width=700,height=180)

        # Second image-->
        img2 = Image.open("student2.jpg")
        img2=img2.resize((700,180),Image.ANTIALIAS) #resize the img(width,height) & ANTIALIAS-->Convert high level img into low level
        self.photo_img1 = ImageTk.PhotoImage(img2)

        label = Label(self.root,image=self.photo_img1)
        label.place(x=700,y=3,width=655,height=180)

        #Label
        title_lbl = Label(self.root,text="Student Attendance Management System",font=("times new roman",25,"bold"),bg="skyblue",fg="black")
        title_lbl.place(x=3,y=160,width=1353,height=45)

        #frame-->
        main_frame = Frame(self.root,bd=2,bg="black")
        main_frame.place(x=10,y=210,width=1340,height=480)

        #Left Side Label Frame-->
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",bg="skyblue",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=8,width=645,height=460)

        img4 = Image.open("girl.jpeg")
        img4=img4.resize((635,130),Image.ANTIALIAS)
        self.photo_img3= ImageTk.PhotoImage(img4)

        label = Label(left_frame,image=self.photo_img3)
        label.place(x=5,y=0,width=630,height=120)

        #Frame-->
        my_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="skyblue")
        my_frame.place(x=5,y=125,width=630,height=300)

        #Label $ Entry--->
        #attendence id:-
        att_id_lbl = Label(my_frame,text="Attendence Id:",font=("times new roman",12,"bold"),bg="skyblue")
        att_id_lbl.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        att_id_entry =ttk.Entry(my_frame,width=23,textvariable=self.var_id,font=("times new roman",10,"bold"))
        att_id_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #Roll-->
        roll_lbl = Label(my_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="skyblue")
        roll_lbl.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        roll_entry =ttk.Entry(my_frame,width=23,textvariable=self.var_roll,font=("times new roman",10,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Name-->
        name_lbl = Label(my_frame,text="Name:",font=("times new roman",12,"bold"),bg="skyblue")
        name_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        name_entry =ttk.Entry(my_frame,width=23,textvariable=self.var_name,font=("times new roman",10,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Department-->
        dep_lbl = Label(my_frame,text="Department:",font=("times new roman",12,"bold"),bg="skyblue")
        dep_lbl.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        dep_entry =ttk.Entry(my_frame,width=23,textvariable=self.var_dep,font=("times new roman",10,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #Time-->
        time_lbl = Label(my_frame,text="Time:",font=("times new roman",12,"bold"),bg="skyblue")
        time_lbl.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        time_entry =ttk.Entry(my_frame,textvariable=self.var_time,width=23,font=("times new roman",10,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Date-->
        date_lbl = Label(my_frame,text="Date:",font=("times new roman",12,"bold"),bg="skyblue")
        date_lbl.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        date_entry =ttk.Entry(my_frame,width=23,textvariable=self.var_date,font=("times new roman",10,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Attendence Status ComboBox-->
        att_st_lbl = Label(my_frame,text="AttendenceStatus:",font=("times new roman",12,"bold"),bg="skyblue")
        att_st_lbl.grid(row=3,column=0,padx=10,sticky=W)

        
        att_st_combo = ttk.Combobox(my_frame,textvariable=self.var_attend_status,width=20,state="read only",font=("times new roman",10,"bold"))
        att_st_combo["values"] = ("Status",'Present','Absent')
        att_st_combo.current(0)
        att_st_combo.grid(row=3,column=1,padx=11,pady=5,sticky=W)

        #Button's Frame:
        btn_frame  = Frame(left_frame,relief=RIDGE,bg="black",bd=2)
        btn_frame.place(x=10,y=370,width=620,height=40)
        #Import csv Button
        import_btn = Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",10,"bold"),bg="pink",fg="black")
        import_btn.grid(row=0,column=1,padx=3,pady=5)
        #Export csv Button
        export_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,width=20,font=("times new roman",10,"bold"),bg="pink",fg="black")
        export_btn.grid(row=0,column=2,padx=3)
        #Update Button
        update_btn = Button(btn_frame,text="Update",width=20,font=("times new roman",10,"bold"),bg="pink",fg="black")
        update_btn.grid(row=0,column=3,padx=3)
        #Reset Button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",10,"bold"),bg="pink",fg="black")
        reset_btn.grid(row=0,column=4,padx=3)

  

        
        #Right Side Label Frame-->
        right_frame = LabelFrame(main_frame,relief=RIDGE,text="Student Information",bg="skyblue",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=8,width=645,height=460)

        #Table Frame:
        table_frame  = Frame(right_frame,relief=RIDGE,bg="white",bd=2)
        table_frame.place(x=5,y=3,width=630,height=425)

        #--------->ScrollBar Table----->
        scrollbarx =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbary =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable = ttk.Treeview(table_frame,columns=("id","rollNo","name","department","time","date","attendanceStatus"),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT,fill=Y)

        scrollbarx.config(command=self.attendanceReportTable.xview)
        scrollbary.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attandence Id")
        self.attendanceReportTable.heading("rollNo",text="Roll No")
        self.attendanceReportTable.heading("name",text="Name ")
        self.attendanceReportTable.heading("department",text="Department ")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendanceStatus",text="Attendance Status")

        self.attendanceReportTable["show"]="headings"   #remove space at first column

        self.attendanceReportTable.column("id",width=100) #set the width of cols
        self.attendanceReportTable.column("rollNo",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=110)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendanceStatus",width=110)

        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #------->Fetch Data------>
    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i  in rows:
            self.attendanceReportTable.insert("",END,values=i)
    #Import csv func--->
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd,title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export csv func--->
    def exportCsv(self):
        try:
            if len(mydata)<1:
                tmsg.showerror("No Data","No data found to export",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                tmsg.showinfo("Data Export","Your data exported to " +os.path.basename(fln) +" successfully")
        except Exception as es:
            tmsg.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    # Get Cursor Func--->
    def get_cursor(self,event=""):
        cursor_row  = self.attendanceReportTable.focus()
        content = self.attendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])  
        self.var_name.set(rows[2])  
        self.var_dep.set(rows[3])  
        self.var_time.set(rows[4])  
        self.var_date.set(rows[5])  
        self.var_attend_status.set(rows[6])   

    #-->Reset Function-->
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")  
        self.var_name.set("")  
        self.var_dep.set("")  
        self.var_time.set("")  
        self.var_date.set("")  
        self.var_attend_status.set("")


if __name__=="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()