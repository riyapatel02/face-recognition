from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import mysql.connector
from mysql.connector import cursor
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #-------------->Varaibles declaration---------->
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_stu_id = StringVar()
        self.var_stu_name = StringVar()
        self.var_sec = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
       
        # First image-->
        img = Image.open("student3.jpg")
        img.resize((450,150),Image.ANTIALIAS) #resize the img(width,height) & ANTIALIAS-->Convert high level img into low level
        self.photo_img = ImageTk.PhotoImage(img)

        label = Label(self.root,image=self.photo_img)
        label.place(x=0,y=0,width=450,height=150)

        # Second image-->
        img2 = Image.open("student1.jpg")
        img2.resize((500,150),Image.ANTIALIAS) #resize the img(width,height) & ANTIALIAS-->Convert high level img into low level
        self.photo_img1 = ImageTk.PhotoImage(img2)

        label = Label(self.root,image=self.photo_img1)
        label.place(x=450,y=0,width=600,height=150)

        #Third image-->
        img3 = Image.open("student2.jpg")
        img3=img3.resize((500,150),Image.ANTIALIAS)
        self.photo_img2= ImageTk.PhotoImage(img3)

        label = Label(self.root,image=self.photo_img2)
        label.place(x=900,y=0,width=450,height=150)

        #Label
        title_lbl = Label(self.root,text="Student Management System",font=("times new roman",25,"bold"),bg="black",fg="pink")
        title_lbl.place(x=0,y=140,width=1380,height=45)

        #BackgroundImage-->
        bg_img = Image.open("stu_bg.jpg")
        bg_img=bg_img.resize((2000,1000),Image.ANTIALIAS)
        self.photo_img_bg= ImageTk.PhotoImage(bg_img)

        label = Label(self.root,image=self.photo_img_bg)
        label.place(x=0,y=185,width=2000,height=1000)


        #frame-->
        main_frame = Frame(self.root,bd=2,bg="black")
        main_frame.place(x=10,y=190,width=1340,height=500)

        #Left Side Label Frame-->
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",bg="pink",font=("times new roman",12,"bold"))
        left_frame.place(x=20,y=5,width=645,height=485)

        img4 = Image.open("girl.jpeg")
        img4=img4.resize((633,130),Image.ANTIALIAS)
        self.photo_img3= ImageTk.PhotoImage(img4)

        label = Label(left_frame,image=self.photo_img3)
        label.place(x=2,y=0,width=633,height=120)
        #Current Course Information LabelFrame-->
        cur_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,bg="white",text="Current Course Information",font=("times new roman",12,"bold"))
        cur_course_frame.place(x=5,y=125,width=630,height=95)

        #Department
        dep_lbl = Label(cur_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lbl.grid(row=0,column=0,padx=15)

        dep_combo= ttk.Combobox(cur_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=25,state="read only")
        dep_combo["values"]=("Select Department",'IT','Computer Science','Civil','Electronics','Mechanical')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8)

        #Course
        crs_lbl = Label(cur_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        crs_lbl.grid(row=0,column=3,padx=15,sticky=W)

        crs_combo = ttk.Combobox(cur_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=25,state="read only")
        crs_combo["values"]=("Select Course",'BSE','BCA','BBA','MCA','BTECH')
        crs_combo.current(0)
        crs_combo.grid(row=0,column=4)

        #Year
        yr_lbl = Label(cur_course_frame,text="Year",bg="white",font=("times new roman",12,"bold"))
        yr_lbl.grid(row=1,column=0,padx=15,sticky=W)

        yr_combo = ttk.Combobox(cur_course_frame,textvariable=self.var_year,width=25,state="read only",font=("times new roman",10,"bold"))
        yr_combo["values"] = ("Select Year",'2020-2021','2021-2022','2022-2023','2023-2024')
        yr_combo.current(0)
        yr_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        #Semester
        sem_lbl = Label(cur_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_lbl.grid(row=1,column=3,padx=15,sticky=W)

        sem_combo = ttk.Combobox(cur_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=25,state="read only")
        sem_combo["values"]=("Select Semester",'Sem-1','Sem-2','Sem-3','Sem-4')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=4,padx=2,pady=8,sticky=W)

        #Class Student Information LabelFrame-->
        csi_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,bg="white",text="Class Student Information",font=("times new roman",12,"bold"))
        csi_frame.place(x=5,y=225,width=630,height=230)
        #studentId:
        stuid_lbl = Label(csi_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        stuid_lbl.grid(row=0,column=0,padx=10,sticky=W)

        stuid_entry =ttk.Entry(csi_frame,width=23,textvariable=self.var_stu_id,font=("times new roman",10,"bold"))
        stuid_entry.grid(row=0,column=1,padx=10,sticky=W)
        #studentName:
        stuname_lbl = Label(csi_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        stuname_lbl.grid(row=0,column=2,padx=10,sticky=W)

        stuname_entry =ttk.Entry(csi_frame,width=23,textvariable=self.var_stu_name,font=("times new roman",10,"bold"))
        stuname_entry.grid(row=0,column=3,padx=10,sticky=W)
        #Class Section:
        sec_lbl = Label(csi_frame,text="Section:",font=("times new roman",12,"bold"),bg="white")
        sec_lbl.grid(row=1,column=0,padx=10,sticky=W)

        
        sec_combo = ttk.Combobox(csi_frame,width=20,state="read only",textvariable=self.var_sec,font=("times new roman",10,"bold"))
        sec_combo["values"] = ("A",'B','C')
        sec_combo.current(0)
        sec_combo.grid(row=1,column=1,padx=11,pady=5,sticky=W)

        # sec_entry =ttk.Entry(csi_frame,width=23,textvariable=self.var_sec,font=("times new roman",10,"bold"))
        # sec_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #RollNo:
        roll_lbl = Label(csi_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_lbl.grid(row=1,column=2,padx=10,sticky=W)

        roll_entry =ttk.Entry(csi_frame,textvariable=self.var_roll,width=23,font=("times new roman",10,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #DOB:
        dob_lbl = Label(csi_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_lbl.grid(row=2,column=0,padx=10,sticky=W)

        dob_entry =ttk.Entry(csi_frame,textvariable=self.var_dob,width=23,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #Gender:
        gen_lbl = Label(csi_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gen_lbl.grid(row=2,column=2,padx=10,sticky=W)

        gender_combo = ttk.Combobox(csi_frame,width=20,state="read only",textvariable=self.var_gender,font=("times new roman",10,"bold"))
        gender_combo["values"] = ('Male','Female','Other')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=11,pady=5,sticky=W)

        # gen_entry =ttk.Entry(csi_frame,width=23,textvariable=self.var_gender,font=("times new roman",10,"bold"))
        # gen_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #PhoneNo:
        phno_lbl = Label(csi_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phno_lbl.grid(row=3,column=0,padx=10,sticky=W)

        phno_entry =ttk.Entry(csi_frame,width=23,textvariable=self.var_phone,font=("times new roman",10,"bold"))
        phno_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #EmailId:
        email_lbl = Label(csi_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
        email_lbl.grid(row=3,column=2,padx=10,sticky=W)

        email_entry =ttk.Entry(csi_frame,width=23,textvariable=self.var_email,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #RadioButtons:
        self.var_radio = StringVar()
        radio_b1=ttk.Radiobutton(csi_frame,variable=self.var_radio,text="Take photo sample",value="Yes")
        radio_b1.grid(row=5,column=0)

        radio_b2=ttk.Radiobutton(csi_frame,variable=self.var_radio,text="No photo sample",value="No")
        radio_b2.grid(row=5,column=1)
        
        #Button's Frame:
        btn_frame  = Frame(left_frame,relief=RIDGE,bg="black",bd=2)
        btn_frame.place(x=10,y=390,width=620,height=30)
        #Save Button
        save_btn = Button(btn_frame,text="Save",width=20,command=self.add_data,font=("times new roman",10,"bold"),bg="lightpink",fg="black")
        save_btn.grid(row=0,column=1,padx=3)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman",10,"bold"),bg="lightpink",fg="black")
        update_btn.grid(row=0,column=2,padx=3)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman",10,"bold"),bg="lightpink",fg="black")
        delete_btn.grid(row=0,column=3,padx=3)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",10,"bold"),bg="lightpink",fg="black")
        reset_btn.grid(row=0,column=4,padx=3)

        btn_frame2  = Frame(left_frame,relief=RIDGE,bg="black",bd=2)
        btn_frame2.place(x=10,y=420,width=620,height=29)
        #Take a photo sample button:
        ptosample_btn = Button(btn_frame2,text="Take Photo Sample",command=self.generate_dataset,width=33,font=("times new roman",11,"bold"),bg="lightpink",fg="black")
        ptosample_btn.grid(row=0,column=1,padx=3)
        #Update Photo Sample:
        upsample_btn = Button(btn_frame2,text="Update Photo Sample",width=32,font=("times new roman",11,"bold"),bg="lightpink",fg="black")
        upsample_btn.grid(row=0,column=2,padx=3)


        #Right Side Label Frame-->
        right_frame = LabelFrame(main_frame,relief=RIDGE,text="Student Details",bg="pink",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=5,width=645,height=485)

        img5 = Image.open("student.jpg")
        img5=img5.resize((633,110),Image.ANTIALIAS)
        self.photo_img4= ImageTk.PhotoImage(img5)

        label = Label(right_frame,image=self.photo_img4)
        label.place(x=4,y=5,width=630,height=110)

        #Search System-->
        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white",text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=120,width=630,height=60)
        
        search_lbl = Label(search_frame,text="Search By :",font=("times new roman",15,"bold"),bg="black",fg="pink")
        search_lbl.grid(row=0,column=0,padx=10,sticky=W)

        
        search_combo = ttk.Combobox(search_frame,width=15,state="read only",font=("times new roman",10,"bold"))
        search_combo["values"] = ("Select",'Roll_No','Phone_No')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,sticky=W)

        search_entry =ttk.Entry(search_frame,width=15,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=14,font=("times new roman",10,"bold"),bg="lightpink",fg="black")
        search_btn.grid(row=0,column=3,padx=3)

        showall_btn = Button(search_frame,text="Show All",width=14,font=("times new roman",10,"bold"),bg="lightpink",fg="black")
        showall_btn.grid(row=0,column=4,padx=3)

        #Table Frame-->
        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=185,width=630,height=270)
        #ScrollBar-->
        scroll_barx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_bary=ttk.Scrollbar(table_frame,orient=VERTICAL)
        #Table-->
        self.student_table= ttk.Treeview(table_frame,column=('dep','course','year','sem','id','name','sec','roll','dob','email','gender','phone','address','teacher','photo'),xscrollcommand=scroll_barx.set,yscrollcommand=scroll_bary.set)
        
        scroll_barx.pack(side=BOTTOM,fill=X)
        scroll_bary.pack(side=RIGHT,fill=Y)
        scroll_barx.config(command=self.student_table.xview)
        scroll_bary.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("phone",text="PhoneNo")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        #setting width of col-->


        self.student_table.pack(fill=BOTH,expand=1)
        #setting width of col-->
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=120)
        self.student_table.column("gender",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=115)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #----------->Function Declarations------------->
    def add_data(self):
        if self.var_dep.get()== "Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            tmsg.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",username="root",password="riya789868",database="facerecognitionsystem")
                #creating cursor-->
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(), 
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_stu_id.get(),
                                                                                                                    self.var_stu_name.get(),
                                                                                                                    self.var_sec.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio.get()      
                                                                                                              ))
                conn.commit() #so that our data  keep updating
                self.fetch_data()
                conn.close()
                tmsg.showinfo("Success","Student Details has been added successfully",parent = self.root)
            except Exception as es:
                tmsg.showerror("Error",f"Due To :{str(es)}",parent = self.root)
    
    #------------->Fetch Data--------->
    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="riya789868",database="facerecognitionsystem")        
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #------->Get Cursor----------->
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_stu_id.set(data[4])
        self.var_stu_name.set(data[5])
        self.var_sec.set(data[6])
        self.var_roll.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio.set(data[14])

    #-------->Update Function------>

    def update_data(self):
        if self.var_dep.get()== "Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            tmsg.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update= tmsg.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn= mysql.connector.connect(host="localhost",username="root",password="riya789868",database="facerecognitionsystem")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,stu_name=%s,sec=%s,roll=%s,dob=%s,email=%s,gender=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where stu_id=%s",(
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(), 
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_stu_name.get(),
                                                                                                                                                                                                self.var_sec.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio.get(),
                                                                                                                                                                                                self.var_stu_id.get()    
                                                                                                                                                                                             ))
                else:
                    if  not update:
                        return
                tmsg.showinfo("Success","Student details successfully updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                tmsg.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    
    #-------->Delete Function----->

    def delete_data(self):
        if self.var_stu_id.get()=="":
            tmsg.showerror("Error","Student ID must be required.",parent=self.root)
        else:
            try:
                delete= tmsg.askyesno("Delete Data","Do you want to delete this student",parent = self.root)
                if delete>0:
                    conn= mysql.connector.connect(host="localhost",username="root",password="riya789868",database="facerecognitionsystem")
                    my_cursor = conn.cursor()
                    sql = "delete from student where stu_id=%s"
                    val = (self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                tmsg.showinfo("Success","Successfully deleted student details.",parent=self.root)
            
            except Exception as es:
                tmsg.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    
    #------->Reset Function------------>
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stu_id.set("")
        self.var_stu_name.set("")
        self.var_sec.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")     
        self.var_teacher.set("")   
        self.var_radio.set("")    

    #-------> Generate Data Set (Take a Photo samples)----->
    def generate_dataset(self):
        if self.var_dep.get()== "Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            tmsg.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",username="root",password="riya789868",database="facerecognitionsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,stu_name=%s,sec=%s,roll=%s,dob=%s,email=%s,gender=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where stu_id=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(), 
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_stu_name.get(),
                                                                                                                                                                                                                    self.var_sec.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio.get(),
                                                                                                                                                                                                                    self.var_stu_id.get()== id+1   
                                                                                                                                                                                                               ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load Predefined data on face frontals from Opencv------>
                face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum Neighbour = 5                

                    for (x,y,w,h) in faces: #x=len,y=breadth,w=width,h=height of rect
                        face_cropped= img[y:y+h,x:x+w]
                        return face_cropped

                capture = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,myframe= capture.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(myframe),(400,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path_name = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                tmsg.showinfo("Result","Generating data sets completed")

            except Exception as es:
                tmsg.showerror("Error",f"Due To: {str(es)}",parent=self.root)




if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()