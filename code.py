import mysql.connector
import sys
import maskpass
# GLOBAL VARIABLES DECLARATION
connection =""
cursor=""
username=""
password =""
def MYSQLconnectionCheck ():
    global connection
    global username
    global password
    while True:
        username = input("\n ENTER MYSQL SERVER'S USERNAME : ")
        if username=='username':
            break
        else:
            sys.stderr.write("\n Incorrect Username")
    while True:        
        password = maskpass.askpass(prompt="\n ENTER MYSQL SERVER'S PASSWORD : ",mask="*")        
        if password=='password':
            break
        else:
            sys.stderr.write("\n Incorrect password")
    connection=mysql.connector.connect(host="localhost",user=username,passwd=password)
    if connection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED SUCESSFULLY !")
        cursor=connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HOTEL")
        cursor.execute("COMMIT")
        cursor.close()
        return connection
    else:
        sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")

def MYSQLconnection():
    global userName
    global password
    global connection
    global cid
    connection=mysql.connector.connect(host="localhost",user=username,passwd=password ,
    database="HOTEL")
    if connection:
        return connection
    else:
        sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")
    connection.close()
def userEntry():
    global cid
    if connection:
        cursor=connection.cursor()
        createTable ='CREATE TABLE IF NOT EXISTS CUST_DETAILS(CID VARCHAR(20) unique,CUST_NAME VARCHAR(50), CUST_AGE VARCHAR(10), PHONE_NO VARCHAR(20),Cust_EMAIL VARCHAR(50));'
        cursor.execute(createTable)
        cid = input("Enter Customer Identification Number : ")
        name = input("Enter Customer Name : ")
        age= input("Enter Customer Age : ")
        phoneno= input("Enter Customer Contact Number : ")
        email = input("Enter Customer Email : ")
        sql="SELECT cid FROM cust_details WHERE CID= %s;"
        cursor.execute(sql,(cid,))
        data=cursor.fetchall()
        if data:
            sys.stderr.write('\nEnter a New Customer Identification Number')
        else:
            sql1 = "INSERT INTO CUST_Details VALUES(%s,%s,%s,%s,%s);"
            values= (cid,name,age,phoneno,email)
            cursor.execute(sql1,values)
            cursor.execute("COMMIT")
            print("\nNew Customer Record Entered In The System Successfully !")
            cursor.close()
    else:
        sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")