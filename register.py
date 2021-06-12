from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox as tmsg
from tkinter import ttk
import mysql.connector

class Register:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1400x790+0+0")
        self.root.title('Register')
        self.root.config(bg="lightpink")

        #------->variables----->
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        #BgImage-->
        img1 = Image.open("static/register.jpg")
        img1=img1.resize((1350,700),Image.ANTIALIAS)
        self.photo_img1= ImageTk.PhotoImage(img1)

        label = Label(self.root,image=self.photo_img1)
        label.place(x=0,y=0,width=1350,height=700)

        #Register Frame:-
        frame_register = Frame(self.root,bg="white")
        frame_register.place(x=300,y=100,height=500,width=700)
        #Label-->
        title = Label(frame_register,text="Register Here",font=("times new roman",20,"bold"),fg="hotpink2",bg="white").place(x=10,y=10)

        #Labels $ Entry-->
        #First Name-->
        fname_lbl = Label(frame_register,text="First Name:",font=("times new roman",14,"bold"),bg="white")
        fname_lbl.place(x=50,y=80)

        fname_entry =ttk.Entry(frame_register,textvariable=self.var_fname,width=28,font=("times new roman",12,"bold"))
        fname_entry.place(x=55,y=105)
        #Last Name-->
        lname_lbl = Label(frame_register,text="Last Name:",font=("times new roman",14,"bold"),bg="white")
        lname_lbl.place(x=320,y=80)

        lname_entry =ttk.Entry(frame_register,width=28,textvariable=self.var_lname,font=("times new roman",12,"bold"))
        lname_entry.place(x=325,y=105)

        #Contact No-->
        con_lbl = Label(frame_register,text="Contact No:",font=("times new roman",14,"bold"),bg="white")
        con_lbl.place(x=50,y=140)

        con_entry =ttk.Entry(frame_register,width=28,textvariable=self.var_contact,font=("times new roman",12,"bold"))
        con_entry.place(x=55,y=165)
        #Email -->
        email_lbl = Label(frame_register,text="Email:",font=("times new roman",14,"bold"),bg="white")
        email_lbl.place(x=320,y=140)

        email_entry =ttk.Entry(frame_register,width=28,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.place(x=325,y=165)
        #ComboBox-->
        combo_lbl = Label(frame_register,text="Select Security Questions:",font=("times new roman",14,"bold"),bg="white")
        combo_lbl.place(x=50,y=200)

        combo= ttk.Combobox(frame_register,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),width=26,state="read only")
        combo["values"]=("Select",'What is your birth month?',"What is your favorite book?")
        combo.current(0)
        combo.place(x=53,y=225)
        #Security Answer -->
        sans_lbl = Label(frame_register,text="Security Answer:",font=("times new roman",14,"bold"),bg="white")
        sans_lbl.place(x=320,y=200)

        sans_entry =ttk.Entry(frame_register,width=28,textvariable=self.var_securityA,font=("times new roman",12,"bold"))
        sans_entry.place(x=325,y=225)
        #Password-->
        pass_lbl = Label(frame_register,text="Password:",font=("times new roman",14,"bold"),bg="white")
        pass_lbl.place(x=50,y=260)

        pass_entry =ttk.Entry(frame_register,width=28,textvariable=self.var_pass,font=("times new roman",12,"bold"))
        pass_entry.place(x=55,y=285)
        #Confirm Password -->
        cpass_lbl = Label(frame_register,text="Confirm Password:",font=("times new roman",14,"bold"),bg="white")
        cpass_lbl.place(x=320,y=260)

        cpass_entry =ttk.Entry(frame_register,width=28,textvariable=self.var_confpass,font=("times new roman",12,"bold"))
        cpass_entry.place(x=325,y=285)
        #Check Button--->
        self.var_chkbtn = IntVar()
        checkbtn=Checkbutton(frame_register,text="I agree the terms & conditions",variable=self.var_chkbtn ,bg="white",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=320)
        # Register Image Button-->
        regbtn = Image.open("static/regbtn.png")
        regbtn=regbtn.resize((160,80),Image.ANTIALIAS)
        self.photo_img2= ImageTk.PhotoImage(regbtn)

        but1 = Button(frame_register,command=self.register_data,image=self.photo_img2,bd=0,cursor="hand2")
        but1.place(x=30,y=360,width=160,height=80)
        # Login Image Button-->
        logbtn = Image.open("static/logbtn.jpg")
        logbtn=logbtn.resize((180,80),Image.ANTIALIAS)
        self.photo_img3= ImageTk.PhotoImage(logbtn)

        but2 = Button(frame_register,image=self.photo_img3,bd=0,cursor="hand2")
        but2.place(x=543,y=440,width=180,height=80)


    #----->Function---->
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            tmsg.showerror("Error","All Fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            tmsg.showerror("Error","Password & Confirm Password must be same")
        elif self.var_chkbtn.get()==0:
            tmsg.showerror("Error","Please agree our terms & conditions")
        else:
            conn= mysql.connector.connect(host="localhost",user="root",password="riya789868",database="facerecognitionsystem")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row= my_cursor.fetchone()
            if row!=None:
                tmsg.showerror("Error","User already exist, Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                      ))
            conn.commit()
            conn.close()
            tmsg.showinfo("Welcome","Thanks for registering with us!")





if __name__=="__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()