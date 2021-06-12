from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox as tmsg
from tkinter import ttk
import mysql.connector
from main import Face_Recognition_System

def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1400x790+0+0")
        self.root.title('Login Window')
        self.root.config(bg="lightpink")

        #Variable--->
        self.var_userEntry=StringVar()
        self.var_passEntry=StringVar()


        # Bg Image:-
        self.bg = ImageTk.PhotoImage(file = "static/pinkimg.jpg")
        self.bg_img = Label(self.root,image= self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login Frame:-
        frame_login = Frame(self.root,bg="white")
        frame_login.place(x=150,y=150,height=350,width=500)

        # IconImage-->
        # img1 = Image.open("static/loginimg.png")
        # img1=img1.resize((50,50),Image.ANTIALIAS)
        # self.photo_img1= ImageTk.PhotoImage(img1)

        # label = Label(frame_login,image=self.photo_img1)
        # label.place(x=170,y=10,width=50,height=45)

        title = Label(frame_login,text="Login Here",font="Impact 35 bold",fg="pink",bg="white").place(x=90,y=30)
        desc = Label(frame_login,text="Please enter valid credentials",font=("Goudy old style", 15 ,"bold"),fg="Brown",bg="white").place(x=90,y=100)

        #IconImage-->
        img1 = Image.open("static/loginimg.png")
        img1=img1.resize((22,22),Image.ANTIALIAS)
        self.photo_img1= ImageTk.PhotoImage(img1)

        label = Label(frame_login,image=self.photo_img1)
        label.place(x=90,y=140,width=20,height=20)

        user = Label(frame_login,text="Email",font=("Goudy old style", 15 ,"bold"),fg="gray",bg="white").place(x=120,y=140)
        self.userEntry = Entry(frame_login,bg="light grey",textvariable=self.var_userEntry)
        self.userEntry.place(x=90,y=170,width=300,height=25)

        #IconImage-->
        img2 = Image.open("static/privacy.jpg")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photo_img2= ImageTk.PhotoImage(img2)

        label = Label(frame_login,image=self.photo_img2)
        label.place(x=90,y=202,width=20,height=20)
        
        password = Label(frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=120,y=200)
        self.passEntry = Entry(frame_login,bg="light gray",textvariable=self.var_passEntry)
        self.passEntry.place(x=90,y=230,width=300,height=25)

        forg_b1 = Button(frame_login,text="Forget Password?",command=self.forgot_pass,bd=0,bg="white",fg="Brown",font=("times new roman",10)).place(x=90,y=260)

        new_ac_b2 = Button(frame_login,text="Create New Account?",command=self.register_window,bd=0,bg="white",fg="Brown",font=("times new roman",10)).place(x=220,y=260)

        login_b2 = Button(self.root,text="LogIn",bg="pink",font=("times new roman",20),fg='brown',command=self.login_func).place(x=300,y=470,width=180,height=40)
    #----->Function-->
    def login_func(self):
        if self.var_userEntry.get()=="" or self.var_passEntry.get()=="":
            tmsg.showerror("Error","All Fields are required",parent =self.root)
        # if self.passEntry.get()!="12345" or self.userEntry.get()!="Stranger":
        #     tmsg.showerror("Error","Invalid Username Or Password",parent =self.root)
        else:
            # tmsg.showinfo("Welcome",f"Welcome {self.userEntry.get()}\n Have a great day!..",parent=self.root)
            conn= mysql.connector.connect(host="localhost",user="root",password="riya789868",database="facerecognitionsystem")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.var_userEntry.get(),
                                                                                        self.var_passEntry.get()
                                                                                      ))
            row = my_cursor.fetchone()
            if row==None:
                tmsg.showerror("Error","Invalid Username & Password")
            else:
                open_main = tmsg.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close




    #----> function for create new user btn-->
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    #------> function for forget password btn(Window)--->
    def forgot_pass(self):
        if self.var_userEntry=="":
            tmsg.showerror("Error","Please enter the email address to reset password")
        else:
            conn= mysql.connector.connect(host="localhost",user="root",password="riya789868",database="facerecognitionsystem")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value = (self.var_userEntry.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row==None:
                    tmsg.showerror("Error",'Please enter the valid user name')
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x400+670+170")
                self.root2.config(bg="pink")

                # ---->variables for forget pass window--->
                self.var_combobox = StringVar()
                self.var_sanswer = StringVar()
                self.var_newpass = StringVar()

                #Label-->
                lab = Label(self.root2,text="Forget Password?",font=("times new roman",20),fg="black",bg="pink")
                lab.place(x=5,y=5,relwidth=1)

                #ComboBox-->
                combobox_lbl = Label(self.root2,text="Select Security Questions:",font=("times new roman",13,"bold"),bg="pink")
                combobox_lbl.place(x=50,y=80)

                combobox= ttk.Combobox(self.root2,font=("times new roman",12,"bold"),textvariable=self.var_combobox,width=26,state="read only")
                combobox["values"]=("Select",'What is your birth month?',"What is your favorite book?")
                combobox.current(0)
                combobox.place(x=50,y=105)
                #Security Answer -->
                sanswer_lbl = Label(self.root2,text="Security Answer:",font=("times new roman",13,"bold"),bg="pink")
                sanswer_lbl.place(x=50,y=150)

                sanswer_entry =ttk.Entry(self.root2,width=28,textvariable=self.var_sanswer,font=("times new roman",12,"bold"))
                sanswer_entry.place(x=50,y=175)
                #New Password -->
                np_lbl = Label(self.root2,text="New Password:",font=("times new roman",13,"bold"),bg="pink")
                np_lbl.place(x=50,y=210)

                np_entry =ttk.Entry(self.root2,width=28,textvariable=self.var_newpass,font=("times new roman",12,"bold"))
                np_entry.place(x=50,y=235)
                #Reset Button
                reset_b = Button(self.root2,text="Reset",command=self.resetpass_btn,font=("times new roman",20),fg='pink',bg="black")
                reset_b.place(x=120,y=270,width=110,height=40)
                
    # ---------->Reset btn func---->
    def resetpass_btn(self):
        if self.var_combobox.get=="Select":
            tmsg.showerror("Error","Select the security question")
        elif self.var_sanswer.get()=="":
            tmsg.showerror("Error","Please enter the security answer")
        elif self.var_newpass.get()=="":
            tmsg.showerror("Error","Please enter the new password")
        else:
            conn= mysql.connector.connect(host="localhost",user="root",password="riya789868",database="facerecognitionsystem")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.var_userEntry.get(),self.var_combobox.get(),self.var_sanswer.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                tmsg.showerror("Error","Please enter correct Security Answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.var_newpass.get(),self.var_userEntry.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                tmsg.showinfo("Info","your password has been reset,\n please login new password")
            
    



#Register Class--->

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
        title = Label(frame_register,text="Register Here",font=("impact",30,"bold"),fg="hotpink2",bg="white").place(x=45,y=10)

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

        but2 = Button(frame_register,image=self.photo_img3,bd=0,command=self.reg_logbtn,cursor="hand2")
        but2.place(x=543,y=440,width=180,height=80)

    #----> function for Register Page Login Btn ---->
    def reg_logbtn(self):
        self.new_window = Toplevel(self.root)
        self.app = Login(self.new_window)

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
    main()
    



