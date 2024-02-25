import mysql.connector
import sys
import random
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
        if username=='root':
            break
        else:
            sys.stderr.write("\n Incorrect Username")
    while True:        
        password = maskpass.askpass(prompt="\n ENTER MYSQL SERVER'S PASSWORD : ",mask="*")        
        if password=='as@10295':
            break
        else:
            sys.stderr.write("\n Incorrect password")
    connection=mysql.connector.connect(host="localhost",user=username,passwd=password)
    if connection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED SUCESSFULLY !")
        cursor=connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HOTEL_BARATIE ")
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
    database="HOTEL_BARATIE")
    if connection:
        return connection
    else:
        sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")
    connection.close()