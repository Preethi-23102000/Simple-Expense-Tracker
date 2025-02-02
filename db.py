import mysql.connector
import datetime
#from tkinter import messagebox
now = datetime.datetime.utcnow()
mydb = mysql.connector.connect(
  host="localhost",
  user="<username>",
  password="<password>"
  
)

mycursor =mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS pythoncourseproject")
mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="<username>",
  password="<password>",
  database="pythoncourseproject"
)

rc=0
#mycursor = mydb.cursor()

CREATE_USER="CREATE TABLE IF NOT EXISTS userID (uid VARCHAR(100)  PRIMARY KEY,password VARCHAR(150),number VARCHAR(20));"
CREATE_GROCERIES = "CREATE TABLE IF NOT EXISTS groceries (id INTEGER AUTO_INCREMENT  PRIMARY KEY,good VARCHAR(255), price INTEGER, date DATE,uid VARCHAR(100) , CONSTRAINT fk_uidg FOREIGN KEY (uid) REFERENCES userID(uid));"
CREATE_HOUSEHOLD = "CREATE TABLE IF NOT EXISTS household (id INTEGER AUTO_INCREMENT PRIMARY KEY,good VARCHAR(255), price INTEGER, date DATE,uid VARCHAR(100) ,CONSTRAINT fk_uidh FOREIGN KEY (uid) REFERENCES userID(uid));"
CREATE_ENTERTAINMENT = "CREATE TABLE IF NOT EXISTS entertainment (id INTEGER AUTO_INCREMENT  PRIMARY KEY,good VARCHAR(255), price INTEGER, date DATE,uid VARCHAR(100) ,CONSTRAINT fk_uide FOREIGN KEY (uid) REFERENCES userID(uid));"
CREATE_MEDICAL = "CREATE TABLE IF NOT EXISTS medical (id INTEGER AUTO_INCREMENT  PRIMARY KEY,good VARCHAR(255), price INTEGER, date DATE,uid VARCHAR(100) ,CONSTRAINT fk_uidm FOREIGN KEY (uid) REFERENCES userID(uid));"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER AUTO_INCREMENT  PRIMARY KEY,good VARCHAR(255), price INTEGER, date DATE,uid VARCHAR(100) ,CONSTRAINT fk_uido FOREIGN KEY (uid) REFERENCES userID(uid));"


INSERT_USER = "INSERT INTO userID (uid ,password ,number ) VALUES(%s,%s,%s)"
INSERT_GROCERIES = "INSERT INTO groceries (good, price, date,uid) VALUES(%s,%s,%s,%s)"
INSERT_HOUSEHOLD = "INSERT INTO household (good, price, date,uid) VALUES(%s,%s,%s,%s)"
INSERT_ENTERTAINMENT = "INSERT INTO entertainment (good, price, date,uid) VALUES(%s,%s,%s,%s)"
INSERT_MEDICAL = "INSERT INTO medical (good, price, date,uid) VALUES(%s,%s,%s,%s)"
INSERT_OTHER = "INSERT INTO other (good, price, date,uid) VALUES(%s,%s,%s,%s)"


SELECT_ALL0 = "SELECT * FROM userID;"
#change made from here
SELECT_ALL1 = "SELECT * FROM groceries WHERE uid = %s;"
SELECT_ALL2 = "SELECT * FROM household WHERE uid = %s;"
SELECT_ALL3 = "SELECT * FROM entertainment WHERE uid = %s;"
SELECT_ALL4 = "SELECT * FROM medical WHERE uid = %s;"
SELECT_ALL5 = "SELECT * FROM other WHERE uid = %s;"

SELECT_GROCERIES = "SELECT * FROM groceries WHERE good = %s AND price = %s AND uid = %s ;"
SELECT_HOUSEHOLD = "SELECT * FROM household WHERE good = %s AND price = %s AND uid = %s ;"
SELECT_ENTERTAINMENT = "SELECT * FROM entertainment WHERE good = %s AND price = %s AND uid = %s ;"
SELECT_MEDICAL = "SELECT * FROM medical WHERE good = %s AND price = %s AND uid = %s ;"
SELECT_OTHER = "SELECT * FROM other WHERE good = %s AND price = %s AND uid = %s ;"

DELETE_GROCERIES = "DELETE FROM groceries WHERE good = %s AND price = %s AND uid = %s;"
DELETE_HOUSEHOLD = "DELETE FROM household WHERE good = %s AND price = %s AND uid = %s;"
DELETE_ENTERTAINMENT = "DELETE FROM entertainment WHERE good = %s AND price = %s AND uid = %s;"
DELETE_MEDICAL = "DELETE FROM medical WHERE good = %s AND price = %s AND uid = %s;"
DELETE_OTHER = "DELETE FROM other WHERE good = %s AND price = %s AND uid = %s;"





###create for every table###
def create_tables():
    mycursor = mydb.cursor()
    mycursor.execute(CREATE_USER)
    mycursor.execute(CREATE_GROCERIES)
    mycursor.execute(CREATE_HOUSEHOLD)
    mycursor.execute(CREATE_ENTERTAINMENT)
    mycursor.execute(CREATE_MEDICAL)
    mycursor.execute(CREATE_OTHER)
    mycursor.close()
    

##user

def insert_user(uid, password,mobNo):
     mycursor = mydb.cursor()
     val = (uid, password,mobNo)
     mycursor.execute(INSERT_USER,val )
     mydb.commit()
     mycursor.close()
    
    
"""    
def check_User( u, p):
    mycursor = mydb.cursor()
    mycursor.execute("select * from logindetails")
    uids=[]
    flag =0
    tup=mycursor.fetchall()
    for i in tup:
        uids.append(i[0])
    for i in tup:
        if i[0]==u and i[1] == p: 
            messagebox.showinfo(title="Loggen In", message="Login sucessful")
            flag=1
            break
        else:
            messagebox.showerror(title="ERROR", message="Wrong user ID/password")
            flag=0
    mydb.commit()
    mycursor.close()
    if flag==1:
        main.ExpenseTracker.MainMenu()
    return flag
     """
    ###INSERT VALUES### 
def insert_groceries(good, price,d,m,y,uid):
     mycursor = mydb.cursor()
     date=datetime.datetime(y,m,d)
     formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
     val = (good, price, formatted_date,uid)
     mycursor.execute(INSERT_GROCERIES,val )
     mydb.commit()
     mycursor.close()
     



def insert_household(good, price,d,m,y,uid):
    mycursor = mydb.cursor()
    date=datetime.datetime(y,m,d)
    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
    val = (good, price, formatted_date,uid)
    mycursor.execute(INSERT_HOUSEHOLD,val)
    mydb.commit()
    mycursor.close()

def insert_entertainment(good, price,d,m,y,uid):
    mycursor = mydb.cursor()
    date=datetime.datetime(y,m,d)
    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
    val = (good, price, formatted_date,uid)
    mycursor.execute(INSERT_ENTERTAINMENT, val)
    mydb.commit()
    mycursor.close()

def insert_medical(good, price,d,m,y,uid):
     mycursor = mydb.cursor()
     date=datetime.datetime(y,m,d)
     formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
     val = (good, price, formatted_date,uid)
     mycursor.execute(INSERT_MEDICAL, val)
     mydb.commit()
     mycursor.close()
     
def insert_other(good, price,d,m,y,uid):
     mycursor = mydb.cursor()
     date=datetime.datetime(y,m,d)
     formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
     val = (good, price, formatted_date,uid)
     mycursor.execute(INSERT_OTHER, val)
     mydb.commit()
     mycursor.close()

###SELECT_ALL###


#change made here
def select_all_groceries(uid):
     mycursor = mydb.cursor()
     val=(uid,)
     mycursor.execute(SELECT_ALL1,val)
     #have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output





def select_all_household(uid):
     mycursor = mydb.cursor()
     val=(uid,)
     mycursor.execute(SELECT_ALL2,val)
     #have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output

def select_all_entertrainment(uid):
     mycursor = mydb.cursor() 
     val=(uid,)
     mycursor.execute(SELECT_ALL3,val)
     #have to store data into a list of Tuple
     list = mycursor.fetchall()
     
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output

def select_all_medical(uid):
     mycursor = mydb.cursor() 
     val=(uid,)
     mycursor.execute(SELECT_ALL4,val)
     #have to store data into a list of Tuple
     list = mycursor.fetchall()
     
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output
 
def select_all_other(uid):
     mycursor = mydb.cursor()
     val=(uid,)
     mycursor.execute(SELECT_ALL5,val)
     #have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output



###SELECT SPECIFIC###

def select_grocery(good, price,uid):
     mycursor = mydb.cursor() 
     val=(good, price,uid)
     mycursor.execute(SELECT_GROCERIES, val)
     # have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output

def select_household(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(SELECT_HOUSEHOLD, val)
     # have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output
 
     

def select_entertainment(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(SELECT_ENTERTAINMENT, val)
     # have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output
 
     

def select_medical(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(SELECT_MEDICAL, val)
     # have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output
 
def select_other(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(SELECT_OTHER, val)
     # have to store data into a list of Tuple
     list = mycursor.fetchall()
     mycursor.close()
     output = ''
     for x in list:
         output = output + str(x[1]) + ' :: ' + str(x[2]) + ' :: ' + ' ' + str(x[3]) + '\n'
     return output
    


###DELETE VALUE###
def delete_grocery(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(DELETE_GROCERIES,val)
     mydb.commit()
     mycursor.close()

def delete_household(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(DELETE_HOUSEHOLD, val)
     mydb.commit()
     mycursor.close()
        

def delete_entertainment(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(DELETE_ENTERTAINMENT, val)
     mydb.commit()
     mycursor.close()
       
def delete_medical(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(DELETE_MEDICAL, val)
     mydb.commit()
     mycursor.close()
     
def delete_other(good, price,uid):
     mycursor = mydb.cursor()
     val=(good, price,uid)
     mycursor.execute(DELETE_OTHER, val)
     mydb.commit()
     mycursor.close()