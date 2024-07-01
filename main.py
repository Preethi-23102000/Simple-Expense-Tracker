import mysql.connector
import db
import tkinter as t
#import  tkinter.ttk as ttk
#import datetime
from tkinter import messagebox
import re
from PIL import ImageTk, Image


mydb = mysql.connector.connect(
  host="localhost",
  user="<username>",
  password="<password>",
  database="pythoncourseproject"
)


#fix date input

LARGE_FONT = ("Verdana", 32)


class ExpenseTracker:
    UserName="Username"
    UserCreated=False
    
    def __init__(self, master):
        self.frame = t.Frame(master)
        self.frame.pack()
        # self.main_window()

    def isValid(self,s):
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        return Pattern.match(s)

    ### display function calls for database update deletion and listing added or deleted#
    def added(self, boxaile):
        myLabel = t.Label(boxaile, text="The record has been inserted")
        myLabel.place(x =30,y = 400, width=200, height=50)

    def delete(self, boxaile):
        myLabel = t.Label(boxaile, text="The value has been deleted ")
        myLabel.place(x =30,y = 400, width=200, height=50)
        
   
    """
    def found(self, boxaile):
        myLabel = t.Label(boxaile, text="                                 ")
        myLabel.place(x =30,y = 280, width=200, height=50)

    def selected(self, boxaile):
        if db.rc==0:
            myLabel = t.Label(boxaile, text="No records were found")
            myLabel.place(x =30,y = 280, width=200, height=50)
        else:
            myLabel = t.Label(boxaile, text="The records are displayed")
            myLabel.place(x =30,y = 280, width=200, height=50)
       """
        #change made here
    def display_all(self, database,boxaile):
        select_all = database(self.UserName,)
        x=select_all
        length = len(x.split('\n'))
        
        if length==1:
            myLabel = t.Label(boxaile, text="No records were found")
            myLabel.place(x =30,y = 400, width=200, height=50)
        else:
            myLabel = t.Label(boxaile, text="The records are displayed")
            myLabel.place(x =30,y = 400, width=200, height=50)
        return select_all
        

    def insertUser(self, database, val1, val2 ,val3,val4):
        uid = val1.get()
        mobNo = val2.get()
        password = val3.get()
        re_password = val4.get()
        flagM=1
        flagP=1
        flagU=1
        
        mycursor = mydb.cursor()
        mycursor.execute("select * from userID")
        uids=[]
        tup=mycursor.fetchall()
        for i in tup:
            uids.append(i[0])
        for j in uids:
            if j==uid : 
                messagebox.showinfo(title="Existing Username", message="Username is already in use please choose another!!")
                flagU=0
                break
            else:
                flagU=1
                
        mydb.commit()
        mycursor.close()
        if (self.isValid(mobNo)):
            flagM=1
        else:
            messagebox.showwarning("Wrong Number","Enter valid number!!")
            flagM=0
       
        if password==re_password :
            flagP=1
        else:
            messagebox.showwarning("MissMatch","The Passwords entered do no match!!")
            flagP=0
            
        if flagM==1 and flagP==1 and flagU==1:
            insertion = database(uid,password,mobNo)
            self.UserCreated=True
            messagebox.showinfo("Confirmation","New User Created!!")
            return insertion
        
        
    """
    def checkUser(self, database, val1, val2):
        uid = val1.get()
        password = val2.get()
        checking = database(uid,password)
        return checking
    """
    def check_User( self,val1,val2):
        u=val1.get()
        p=val2.get()
        flag=0
        self.UserName=u
        mycursor = mydb.cursor()
        mycursor.execute("select * from userID")
        uids=[]
        tup=mycursor.fetchall()
        for i in tup:
            uids.append(i[0])
        for i in tup:
            if i[0]==u and i[1] == p: 
                messagebox.showinfo(title="Loggen In", message="Login sucessful")
                flag=1
                self.MainMenu()
                break
            else:
                flag =0
                
        if flag==0:
            messagebox.showerror(title="ERROR", message="Wrong user ID/password")
        mydb.commit()
        mycursor.close()
       
            
        
    """
    def select_all(self, database):
        
        UN=self.UserName
        selection = database(UN,)
        return selection
    """
    
    def insert(self, database, val1, val2, val3,val4,val5):
        goods = val1.get()
        price = val2.get()
        d=int(val3.get())
        m=int(val4.get())
        y=int(val5.get())
        insertion = database(goods, price, d,m,y,self.UserName)
        return insertion

    def find_expense(self, database, val1, val2,boxaile) :
        goods = val1.get()
        price = val2.get()
        find = database(goods, price,self.UserName)
        x=find
        length = len(x.split('\n'))
        
        if length==1:
            myLabel = t.Label(boxaile, text="No records were found")
            myLabel.place(x =30,y = 400, width=200, height=50)
        else:
            myLabel = t.Label(boxaile, text="The records are displayed")
            myLabel.place(x =30,y = 400, width=200, height=50)
        return find

    def delete_expense(self,database1,database2, val1, val2,boxaile):
        goods = val1.get()
        price = val2.get()
        select_all = database2(self.UserName,)
        x=select_all
        lengthX = len(x.split('\n'))
        delete = database1(goods, price,self.UserName)
        select_all2 = database2(self.UserName,)
        y=select_all2
        lengthY = len(y.split('\n'))
        
        if lengthX==lengthY:
            myLabel = t.Label(boxaile, text="No records were deleted")
            myLabel.place(x =30,y = 400, width=200, height=50)
        elif lengthY < lengthX:
            myLabel = t.Label(boxaile, text="The records were deleted")
            myLabel.place(x =30,y = 400, width=200, height=50)
        return delete
#_______________________________________________________________________________________________
    def LogIn(self):
        top = t.Toplevel(self.frame)
        top.geometry('550x400')
        top.title('Expense Tracker : Log In')
        
        image = Image.open("images\\login.png")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        """
        center_frame = t.Frame(top, relief='raised', borderwidth=2)
        center_frame.place(relx=0.6, rely=0.1, anchor=t.NW)
        """
        lb1 = t.Label(top, text="Login",font=("Arial", 20,"bold"),bg="#ffffff")
        lb1.place(x =230,y = 10, width=100, height=50)
        
        #lb2 = t.Label(top, text="User Name :",font=("Arial", 12,"bold"),bg="#05445E",fg="white")
        lb2 = t.Label(top, text="User Name :",font=("Arial", 12,"bold"),bg="#D4F1F4") 
        lb2.place(x =120,y = 110, width=100, height=35)
        
        e1 = t.Entry(top,bg="#D4F1F4")             
        e1.place(x =250,y = 110, width=200, height=35)
        
        
        lb3 = t.Label(top, text="Password :",font=("Arial", 12,"bold"),bg="#D4F1F4") 
        lb3.place(x =120,y = 170, width=100, height=35)
            
        e2 = t.Entry(top,show="*",bg="#D4F1F4")
        e2.place(x =250,y = 170, width=200, height=35)
        
        button1 = t.Button(top, text="Log In",command=lambda : self.check_User(e1,e2),font=("Arial", 11),bg="#189AB4")
        button1.place(x =230,y = 230, width=100, height=30)
        
        lb4 = t.Label(top, text="New to Expense Tracker ? Sign Up !!",font=("Arial", 10),bg="#75E6DA")
        lb4.place(x =150,y = 270, width=250, height=30)
        
        button2 = t.Button(top, text="Sign Up",command=self.SignUp,font=("Arial", 11),bg="#189AB4")
        button2.place(x =230,y = 310, width=100, height=30)
        
        
#_______________________________________________________________________________________________
    def SignUp(self):
        top = t.Toplevel(self.frame)
        top.geometry('521x521')
        top.title('Expense Tracker : Sign Up')
        
        
               
        image = Image.open("images\\signup.jpg")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        lb1 = t.Label(top, text="Create Account",font=("Arial", 20,"bold"),bg="#ffffff")
        lb1.place(x =120,y = 30, width=300, height=50)
        
        lb2 = t.Label(top, text="User Name :",font=("Arial", 12),bg="#D78261") 
        lb2.place(x =70,y = 110, width=150, height=35)
        
        e1 = t.Entry(top,bg="#EBD4BF")              
        e1.place(x =250,y = 110, width=200, height=35)
        
        
        lb3 = t.Label(top, text="Mobile Number :",font=("Arial", 12),bg="#D78261") 
        lb3.place(x =70,y = 170, width=150, height=35)
            
        e2 = t.Entry(top,bg="#EBD4BF")  
        e2.place(x =250,y = 170, width=200, height=35)
        
        lb4 = t.Label(top, text="Password :",font=("Arial", 12),bg="#D78261") 
        lb4.place(x =70,y = 230, width=150, height=35)
            
        e3 = t.Entry(top,show="*",bg="#EBD4BF")  
        e3.place(x =250,y = 230, width=200, height=35)
        
        lb5 = t.Label(top, text="Re-Enter Password :",font=("Arial", 12),bg="#D78261") 
        lb5.place(x =70,y = 290, width=150, height=35)
            
        e4 = t.Entry(top,show="*",bg="#EBD4BF")  
        e4.place(x =250,y = 290, width=200, height=35)
        
            
        button1 = t.Button(top, text="Sign Up",command=lambda: self.insertUser(db.insert_user,e1,e2,e3,e4),font=("Arial", 11),bg="#B96554")
        button1.place(x =230,y = 350, width=100, height=30)
        
        lb4 = t.Label(top, text="Existing user ? Log in !!",font=("Arial", 10),bg="#EBD4BF")  
        lb4.place(x =190,y = 390, width=180, height=30)
        
        button2 = t.Button(top, text="Log in",command=lambda: top.destroy(),font=("Arial", 11),bg="#B96554")
        button2.place(x =230,y = 430, width=100, height=30)
        
        if self.UserCreated==True :
            top.destroy()

 #_______________________________________________________________________________________________       
        
    
    def MainMenu(self):
        top = t.Toplevel(self.frame)
        top.geometry('603x594')
        top.title('Expense Tracker : Main Menu')
        
        image = Image.open("images\\mainmenu.jpg")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        l1=t.Label(top,text="Welcome To Expense Tracker",font=("Arial", 20),bg="#f4f8fb")
        l1.place(x =100,y = 20, width=400, height=50)
       
        
        l3=t.Label(top,text="The app for all your money management needs.",font=("Arial", 12),bg="#f4f8fb")
        l3.place(x =100,y = 55, width=400, height=40)
        
        
        
        
        l2=t.Label(top,text="Main Menu",font=("Arial", 25),bg="#E8E0ED")
        l2.place(x =180,y = 100, width=250, height=40)
        
        
        button1 = t.Button(top, text="Groceries Expenses", command=self.groceries,height = 2, width = 20,bg="#E1C2F0")
        button1.place(x =210,y = 190, width=180, height=40)
        
        

        button2 = t.Button(top, text="Household Expenses", command=self.household,height = 2, width = 20,bg="#E1C2F0")
        button2.place(x =210,y = 245, width=180, height=40)
        

        button3 = t.Button(top, text="Entertainment Expenses",command=self.entertainment,height = 2, width = 20,bg="#E1C2F0") 
        button3.place(x =210,y = 305, width=180, height=40)
        

        button4 = t.Button(top, text="Medical Expenses", command=self.medical,height = 2, width = 20,bg="#E1C2F0")
        button4.place(x =210,y = 365, width=180, height=40)
        
        button5 = t.Button(top, text="Other Expenses", command=self.other,height = 2, width = 20,bg="#E1C2F0")
        button5.place(x =210,y = 425, width=180, height=40)
        
        
       
#_______________________________________________________________________________________________
    
    def groceries(self):


        top = t.Toplevel(self.frame)
        top.geometry('581x466')
        top.title('Expense Tracker : Groceries Expenses')
        image = Image.open("images\\groceries.jpg")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        l1 = t.Label(top, text="Item purchased : ",bg="#F6EEE5")
        l1.grid(row = 1, column = 0, sticky = t.W, pady = 2)
        l1.place(x =10,y = 10, width=100, height=20)
        l2 = t.Label(top, text="Amount : ",bg="#F6EEE5")
        l2.grid(row = 2, column = 0, sticky = t.W, pady = 2)
        l2.place(x =10,y = 40, width=100, height=20)
        l3 = t.Label(top, text="Date of payment :",bg="#F6EEE5")
        l3.grid(row = 3, column = 0, sticky = t.W, pady = 2)
        l3.place(x =10,y = 70, width=100, height=20)

        e1 = t.Entry(top,bg="#F6EEE5")
        #e1.grid(row=1, column=1,columnspan=3, sticky=t.W, pady=2)
        e1.place(x =130,y = 10, width=200, height=20)
        e2 = t.Entry(top,bg="#F6EEE5")
        #e2.grid(row=2, column=1,columnspan=3, sticky=t.W, pady=2)
        e2.place(x =130,y = 40, width=200, height=20)
        e3 = t.Entry(top,bg="#F6EEE5")
        #e3.grid(row=3, column=1, sticky=t.W, pady=2)
        e3.place(x =130,y = 70, width=55, height=20)
        e4 = t.Entry(top,bg="#F6EEE5")
        # e4.grid(row=3, column=2, sticky=t.W, pady=2)
        e4.place(x =195,y = 70, width=55, height=20)
        e5 = t.Entry(top,bg="#F6EEE5")
        #e5.grid(row=3, column=3, sticky=t.W, pady=2)
        e5.place(x =265,y = 70, width=70, height=20)
        
        
        l4 = t.Label(top, text="DD       /      MM        /     YYYY",bg="#fff7f0")
        l4.place(x =130,y = 90, width=180, height=20)
        
        l5 = t.Label(top, text="Product  ::   Price   ::  Date ",bg="#fff7f0")
        l5.place(x =30,y = 120, width=200, height=20)
        
        text = t.Text(top, width=40, height=10,bg="#F6EEE5")
        #text.grid(row=11, column=1, columnspan=2)
        text.place(x =30,y = 140, width=450, height=250)
        

        #BUTTONS###

        B1 = t.Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_groceries,e1,e2,e3,e4,e5), self.added(top)),bg="#B59F84")
        #B1.grid(row=10, column=5)
        B1.place(x =350,y = 30, width=100, height=20)
        
                                                                                                                            #change made here
        B2 = t.Button(top, text="Select All", command=lambda:  (text.delete(1.0, t.END), text.insert(t.END, self.display_all(db.select_all_groceries,top))),bg="#B59F84")
        #B2.grid(row=2, column=5)
        B2.place(x =350,y = 60, width=100, height=20)

        B3 = t.Button(top, text="Find value", command=lambda: (text.delete(1.0, t.END), text.insert(t.END, self.find_expense(db.select_grocery, e1,e2,top))),bg="#B59F84")
        #B3.grid(row=2, column=6)
        B3.place(x =470,y = 60, width=100, height=20)

        B4 = t.Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_grocery,db.select_all_groceries, e1,e2,top)),bg="#B59F84")
        #B4.grid(row=1, column=6)
        B4.place(x =470,y = 30, width=100, height=20)
        
        B5 = t.Button(top, text="Main Menu", command= lambda : top.destroy(),bg="#B59F84")
        B5.place(x =390,y = 90, width=100, height=20)

         
#_______________________________________________________________________________________________

    def household(self):
        top = t.Toplevel(self.frame)
        top.geometry('581x466')
        top.title('Expense Tracker : Household Expenses')
        
        image = Image.open("images\\household.jpg")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        
       
             
        l1 = t.Label(top, text="Item purchased : ",bg="#FAF9F2")
        #l1.grid(row = 1, column = 0, sticky = t.W, pady = 2)
        l1.place(x =10,y = 10, width=100, height=30)        
        l2 = t.Label(top, text="Amount : ",bg="#FAF9F2")
        #l2.grid(row = 2, column = 0, sticky = t.W, pady = 2)
        l2.place(x =10,y = 40, width=100, height=30)
        l3 = t.Label(top, text="Date of payment :",bg="#FAF9F2")
        #l3.grid(row = 3, column = 0, sticky = t.W, pady = 2)
        l3.place(x =10,y = 70, width=100, height=30)

       
        e1 = t.Entry(top,bg="#FAF9F2")     
        #e1.grid(row=1, column=1,columnspan=3, sticky=t.W, pady=2)
        e1.place(x =130,y = 10, width=200, height=20)
        e2 = t.Entry(top,bg="#FAF9F2")
        #e2.grid(row=2, column=1,columnspan=3, sticky=t.W, pady=2)
        e2.place(x =130,y = 40, width=200, height=20)
        e3 = t.Entry(top,bg="#FAF9F2")
        #e3.grid(row=3, column=1, sticky=t.W, pady=2)
        e3.place(x =130,y = 70, width=55, height=20)
        e4 = t.Entry(top,bg="#FAF9F2")
       # e4.grid(row=3, column=2, sticky=t.W, pady=2)
        e4.place(x =195,y = 70, width=55, height=20)
        e5 = t.Entry(top,bg="#FAF9F2")
        #e5.grid(row=3, column=3, sticky=t.W, pady=2)
        e5.place(x =265,y = 70, width=70, height=20)
        
        
        l4 = t.Label(top, text="DD       /      MM        /     YYYY",bg="#FAF9F2")
        l4.place(x =130,y = 90, width=180, height=20)
        
        l5 = t.Label(top, text="Product  ::   Price   ::  Date ",bg="#FAF9F2")
        l5.place(x =30,y = 120, width=200, height=20)
        
        text = t.Text(top, width=40, height=10,bg="#FAF9F2")
        #text.grid(row=11, column=1, columnspan=2)
        text.place(x =30,y = 140, width=450, height=250)
        

        #BUTTONS###

        B1 = t.Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_household,e1,e2,e3,e4,e5), self.added(top)),bg="#bfb4b4")
        #B1.grid(row=10, column=5)
        B1.place(x =350,y = 30, width=100, height=20)
        

        B2 = t.Button(top, text="Select All", command=lambda: (text.delete(1.0, t.END), text.insert(t.END, self.display_all(db.select_all_household,top))),bg="#bfb4b4")
        #B2.grid(row=2, column=5)
        B2.place(x =350,y = 60, width=100, height=20)

        B3 = t.Button(top, text="Find value", command=lambda: (text.delete(1.0, t.END), text.insert(t.END, self.find_expense(db.select_household, e1,e2,top))),bg="#bfb4b4")
        #B3.grid(row=2, column=6)
        B3.place(x =470,y = 60, width=100, height=20)

        B4 = t.Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_household,db.select_all_household, e1,e2,top)),bg="#bfb4b4")
        #B4.grid(row=1, column=6)
        B4.place(x =470,y = 30, width=100, height=20)
        
        B5 = t.Button(top, text="Main Menu", command= lambda : top.destroy(),bg="#bfb4b4")
        B5.place(x =390,y = 90, width=100, height=20)


#_______________________________________________________________________________________________


    def entertainment(self):
        top = t.Toplevel(self.frame)
        top.geometry('581x466')
        top.title('Expense Tracker : Entertainment Expenses')
        image = Image.open("images\\entertainment.jpg")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        
       
             
        l1 = t.Label(top, text="Item purchased : ",bg="#ffffff")
        #l1.grid(row = 1, column = 0, sticky = t.W, pady = 2)
        l1.place(x =10,y = 10, width=100, height=25)        
        l2 = t.Label(top, text="Amount : ",bg="#ffffff")
        #l2.grid(row = 2, column = 0, sticky = t.W, pady = 2)
        l2.place(x =10,y = 40, width=100, height=25)
        l3 = t.Label(top, text="Date of payment :",bg="#ffffff")
        #l3.grid(row = 3, column = 0, sticky = t.W, pady = 2)
        l3.place(x =10,y = 70, width=100, height=25)

       
        e1 = t.Entry(top,bg="#ffffff")     
        #e1.grid(row=1, column=1,columnspan=3, sticky=t.W, pady=2)
        e1.place(x =130,y = 10, width=200, height=20)
        e2 = t.Entry(top,bg="#ffffff")
        #e2.grid(row=2, column=1,columnspan=3, sticky=t.W, pady=2)
        e2.place(x =130,y = 40, width=200, height=20)
        e3 = t.Entry(top,bg="#ffffff")
        #e3.grid(row=3, column=1, sticky=t.W, pady=2)
        e3.place(x =130,y = 70, width=55, height=20)
        e4 = t.Entry(top,bg="#ffffff")
       # e4.grid(row=3, column=2, sticky=t.W, pady=2)
        e4.place(x =195,y = 70, width=55, height=20)
        e5 = t.Entry(top,bg="#ffffff")
        #e5.grid(row=3, column=3, sticky=t.W, pady=2)
        e5.place(x =265,y = 70, width=70, height=20)
        
        
        l4 = t.Label(top, text="DD       /      MM        /     YYYY",bg="#ffffff")
        l4.place(x =130,y = 90, width=180, height=20)
        
        l5 = t.Label(top, text="Product  ::   Price   ::  Date ",bg="#ffffff")
        l5.place(x =30,y = 120, width=200, height=20)
        
        text = t.Text(top, width=40, height=10,bg="#ffffff")
        #text.grid(row=11, column=1, columnspan=2)
        text.place(x =30,y = 140, width=450, height=250)
        

        #BUTTONS###

        B1 = t.Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_entertainment,e1,e2,e3,e4,e5), self.added(top)),bg="#dbe8de")
        #B1.grid(row=10, column=5)
        B1.place(x =350,y = 30, width=100, height=25)
        

        B2 = t.Button(top, text="Select All", command=lambda:  (text.delete(1.0, t.END), text.insert(t.END, self.display_all(db.select_all_entertrainment,top))),bg="#dbe8de")
        #B2.grid(row=2, column=5)
        B2.place(x =350,y = 60, width=100, height=25)

        B3 = t.Button(top, text="Find value", command=lambda: (text.delete(1.0, t.END), text.insert(t.END, self.find_expense(db.select_entertainment, e1,e2,top))),bg="#dbe8de")
        #B3.grid(row=2, column=6)
        B3.place(x =470,y = 60, width=100, height=25)

        B4 = t.Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_entertainment,db.select_all_entertrainment, e1,e2,top)),bg="#dbe8de")
        #B4.grid(row=1, column=6)
        B4.place(x =470,y = 30, width=100, height=25)
        
        
        
        B5 = t.Button(top, text="Main Menu", command= lambda : top.destroy(),bg="#dbe8de")
        B5.place(x =390,y = 90, width=100, height=25)

#_______________________________________________________________________________________________


    def medical(self):
        top = t.Toplevel(self.frame)
        top.geometry('581x466')
        top.title('Expense Tracker : Medical Expenses')
        image = Image.open("images\\medical.jpg")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        l1 = t.Label(top, text="Treatment/Product : ",bg="#E4ECDA")
        l1.grid(row = 1, column = 0, sticky = t.W, pady = 2)
        l1.place(x =10,y = 10, width=120, height=20)
        l2 = t.Label(top, text="Amount : ",bg="#E4ECDA")
        l2.grid(row = 2, column = 0, sticky = t.W, pady = 2)
        l2.place(x =10,y = 40, width=120, height=20)
        l3 = t.Label(top, text="Date of payment :",bg="#E4ECDA")
        l3.grid(row = 3, column = 0, sticky = t.W, pady = 2)
        l3.place(x =10,y = 70, width=120, height=20)

        e1 = t.Entry(top,bg="#E4ECDA")   
        #e1.grid(row=1, column=1,columnspan=3, sticky=t.W, pady=2)
        e1.place(x =150,y = 10, width=200, height=20)
        e2 = t.Entry(top,bg="#E4ECDA")
        #e2.grid(row=2, column=1,columnspan=3, sticky=t.W, pady=2)
        e2.place(x =150,y = 40, width=200, height=20)
        e3 = t.Entry(top,bg="#E4ECDA")
        #e3.grid(row=3, column=1, sticky=t.W, pady=2)
        e3.place(x =150,y = 70, width=50, height=20)
        e4 = t.Entry(top,bg="#E4ECDA")
       # e4.grid(row=3, column=2, sticky=t.W, pady=2)
        e4.place(x =210,y = 70, width=50, height=20)
        e5 = t.Entry(top,bg="#E4ECDA")
        #e5.grid(row=3, column=3, sticky=t.W, pady=2)
        e5.place(x =270,y = 70, width=70, height=20)
        
        
        l4 = t.Label(top, text="DD       /      MM        /     YYYY",bg="#E4ECDA")
        l4.place(x =150,y = 90, width=180, height=20)
        
        l5 = t.Label(top, text="Product  ::   Price   ::  Date ",bg="#E4ECDA")
        l5.place(x =30,y = 120, width=200, height=20)
        
        text = t.Text(top, width=40, height=10,bg="#E4ECDA")
        #text.grid(row=11, column=1, columnspan=2)
        text.place(x =30,y = 140, width=450, height=250)
        

        #BUTTONS###

        B1 = t.Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_medical,e1,e2,e3,e4,e5), self.added(top)),bg="#54B6B8")
        #B1.grid(row=10, column=5)
        B1.place(x =350,y = 30, width=100, height=20)
        

        B2 = t.Button(top, text="Select All", command=lambda:  (text.delete(1.0, t.END), text.insert(t.END, self.display_all(db.select_all_medical,top))),bg="#54B6B8")
        #B2.grid(row=2, column=5)
        B2.place(x =350,y = 60, width=100, height=20)

        B3 = t.Button(top, text="Find value", command=lambda: (text.delete(1.0, t.END), text.insert(t.END, self.find_expense(db.select_medical, e1,e2,top))),bg="#54B6B8")
        #B3.grid(row=2, column=6)
        B3.place(x =470,y = 60, width=100, height=20)

        B4 = t.Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_entertainment,db.select_all_medical, e1,e2,top)),bg="#54B6B8")
        #B4.grid(row=1, column=6)
        B4.place(x =470,y = 30, width=100, height=20)
        
        
        
        B5 = t.Button(top, text="Main Menu", command= lambda : top.destroy(),bg="#54B6B8")
        B5.place(x =390,y = 90, width=100, height=20)

#_______________________________________________________________________________________________


    def other(self):
        top = t.Toplevel(self.frame)
        top.geometry('581x466')
        top.title('Expense Tracker : Other Expenses')
        
        image = Image.open("images\\others.jpg")

        render = ImageTk.PhotoImage(image)
        img = t.Label(top, image=render)
        img.image = render
        img.place(x=0, y=0)
        
       
             
        l1 = t.Label(top, text="Item purchased : ",bg="#C8DFE8")
        #l1.grid(row = 1, column = 0, sticky = t.W, pady = 2)
        l1.place(x =10,y = 10, width=100, height=25)        
        l2 = t.Label(top, text="Amount : ",bg="#C8DFE8")
        #l2.grid(row = 2, column = 0, sticky = t.W, pady = 2)
        l2.place(x =10,y = 40, width=100, height=25)
        l3 = t.Label(top, text="Date of payment :",bg="#C8DFE8")
        #l3.grid(row = 3, column = 0, sticky = t.W, pady = 2)
        l3.place(x =10,y = 70, width=100, height=25)

       
        e1 = t.Entry(top,bg="#C8DFE8")     
        #e1.grid(row=1, column=1,columnspan=3, sticky=t.W, pady=2)
        e1.place(x =130,y = 10, width=200, height=20)
        e2 = t.Entry(top,bg="#C8DFE8")
        #e2.grid(row=2, column=1,columnspan=3, sticky=t.W, pady=2)
        e2.place(x =130,y = 40, width=200, height=20)
        e3 = t.Entry(top,bg="#C8DFE8")
        #e3.grid(row=3, column=1, sticky=t.W, pady=2)
        e3.place(x =130,y = 70, width=55, height=20)
        e4 = t.Entry(top,bg="#C8DFE8")
       # e4.grid(row=3, column=2, sticky=t.W, pady=2)
        e4.place(x =195,y = 70, width=55, height=20)
        e5 = t.Entry(top,bg="#C8DFE8")
        #e5.grid(row=3, column=3, sticky=t.W, pady=2)
        e5.place(x =265,y = 70, width=70, height=20)
        
        
        l4 = t.Label(top, text="DD       /      MM        /     YYYY",bg="#ffffff")
        l4.place(x =130,y = 90, width=180, height=20)
        
        l5 = t.Label(top, text="Product  ::   Price   ::  Date ",bg="#ffffff")
        l5.place(x =30,y = 120, width=200, height=20)
        
        text = t.Text(top, width=40, height=10,bg="#C8DFE8")
        #text.grid(row=11, column=1, columnspan=2)
        text.place(x =30,y = 140, width=450, height=250)
        

        #BUTTONS###

        B1 = t.Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_other,e1,e2,e3,e4,e5), self.added(top)),bg="#F4B86A")
        #B1.grid(row=10, column=5)
        B1.place(x =350,y = 30, width=100, height=20)
        

        B2 = t.Button(top, text="Select All", command=lambda:  (text.delete(1.0, t.END), text.insert(t.END, self.display_all(db.select_all_other,top))),bg="#F4B86A")
        #B2.grid(row=2, column=5)
        B2.place(x =350,y = 60, width=100, height=20)

        B3 = t.Button(top, text="Find value", command=lambda: (text.delete(1.0, t.END), text.insert(t.END, self.find_expense(db.select_other, e1,e2,top))),bg="#F4B86A")
        #B3.grid(row=2, column=6)
        B3.place(x =470,y = 60, width=100, height=20)

        B4 = t.Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_other,db.select_all_other, e1,e2,top)),bg="#F4B86A")
        #B4.grid(row=1, column=6)
        B4.place(x =470,y = 30, width=100, height=20)
        
        B5 = t.Button(top, text="Main Menu", command= lambda : top.destroy(),bg="#F4B86A")
        B5.place(x =390,y = 90, width=100, height=20)

#_______________________________________________________________________________________________
 


def main():
    db.create_tables()
    root = t.Tk()
    root.geometry("694x554")
  
    
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)
    
    img = ImageTk.PhotoImage(Image.open("images\\expensetracker.jpg"))  
    l=t.Label(root,image=img)
    l.pack()
    center_frame = t.Frame(root, relief='raised', borderwidth=2)
    center_frame.place(relx=0.6, rely=0.1, anchor=t.NW)
    button1=t.Button(center_frame,text ='Expense Tracker',font=("Arial", 20),bg="white",command=lambda : tracker.LogIn(),relief="ridge" )
    button1.pack()
   
    
    #root.overrideredirect(1)
    #root.withdraw()
           
    root.mainloop()


main()