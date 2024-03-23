import mysql.connector
import sys
import maskpass
import random
# GLOBAL VARIABLES DECLARATION
connection =""
cursor=""
username=""
password =""
roomrent =0
restaurentbill=0
gamingbill=0
laundarybill=0
totalAmount=0
cid=""


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

def searchCustomer():
    global cid
    if connection:
        cursor=connection.cursor()
        createTable ='CREATE TABLE IF NOT EXISTS CUST_DETAILS(CID VARCHAR(20) unique,CUST_NAME VARCHAR(50), CUST_AGE VARCHAR(10), PHONE_NO VARCHAR(20),Cust_EMAIL VARCHAR(50));'
        cursor.execute(createTable)
        cid=input("ENTER CUSTOMER ID : ")
        sql="SELECT * FROM CUST_DETAILS WHERE CID = %s;"
        cursor.execute(sql,(cid,))
        data=cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            sys.stderr.write("\nSORRY, Record Not Found Try Again !")
            return False
        cursor.close()
    else:
        sys.stderr.write("\nSomthing Went Wrong ,Please Try Again !")

def booking():
    global cid
    customer=searchCustomer()
    if customer:
        if connection:
            cursor=connection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS BOOKING (CID VARCHAR(20),CHECK_IN DATE ,CHECK_OUT DATE);"
            cursor.execute(createTable)
            checkin=input("\n Enter Customers CheckIN Date [ YYYY-MM-DD ] : ")
            while True:
                checkout=input("\n Enter Customers CheckOUT Date [ YYYY-MM-DD ] : ")
                if checkin>checkout:
                    sys.stderr.write("enter a correct checkout date")
                else:
                    break
            sql= "INSERT INTO BOOKING VALUES(%s,%s,%s);"
            values= (cid,checkin,checkout)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\nCHECK-IN AND CHECK-OUT DATE ENTERED SUCCESSFULLY !")
            cursor.close()
        else:
            sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")

def roomRent():
    global cid
    customer=searchCustomer()
    if customer:
        global roomrent
        if connection:
            roomrent=0
            cursor=connection.cursor()
            createTable ='CREATE TABLE IF NOT EXISTS ROOMS(CID VARCHAR(20),ROOM_TYPE INT ,NO_OF_DAYS INT ,ROOMNO INT unique,ROOMRENT int);'
            cursor.execute(createTable)
            print ("\n ***** We have The Following Rooms For You *****")
            print (" 1. NON-A/C SINGLE BED ----> 2000 Rs.")
            print (" 2. NON-A/C DOUBLE BED ----> 3000 Rs. ")
            print (" 3. A/C SINGLE BED ----> 4000 Rs. ")
            print (" 4. A/C DOUBLE BED ----> 5000 Rs ") 
            roomchoice =input("Enter Your Selected Room : ")
            noofdays=int(input("Enter the No. Of nights : "))
            if roomchoice=='1':
                r=1
                roomno=print("Customers Room No is : ",r)
                roomrent = noofdays * 2000
                print("\nNON-A/C SINGLE BED Room Rent is : ",roomrent)
            elif roomchoice=='2':
                r=random.randrange(11,20)
                roomno=print("Customers Room No is : ",r)
                roomrent = noofdays * 3000
                print("\nNON-A/C DOUBLE BED Room Rent is : ",roomrent)
            elif roomchoice=='3':
                r=random.randrange(21,30)
                roomno=print("Customers Room No is : ",r)
                roomrent = noofdays * 4000
                print("\nA/C SINGLE BED Room Rent is : ",roomrent)
            elif roomchoice=='4':
                r=random.randrange(31,40)
                roomno=print("Customers Room No is : ",r)
                roomrent = noofdays * 5000
                print("\nA/C DOUBLE BED Room Rent is : ",roomrent)
            else:
                sys.stderr.write("Sorry ,Maybe You Are Giving Me Wrong Input, Please Try Again !!! ")
                return False
            sql= "INSERT INTO ROOMS VALUES(%s,%s,%s,%s,%s);"
            values= (cid,roomchoice,noofdays,r,roomrent,)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("Thank You :) , Your Room Has Been Booked For : ",noofdays , "Nights" )
            print("Your Total Room Rent is : Rs. ",roomrent)
            cursor.close()
        else:
             sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")
def Restaurent():
    global cid
    customer=searchCustomer()
    if customer:
        global restaurentbill
        if connection:
            cursor=connection.cursor()
            createTable ='CREATE TABLE IF NOT EXISTS RESTAURENT(CID VARCHAR(20),CUISINE VARCHAR(100),QUANTITY VARCHAR(30),BILL VARCHAR(30));'
            cursor.execute(createTable)
            list=[]
            print('A.  STARTERS')
            print('1.  The ultimate cheese cake -----> 100 Rs.')
            print('2.  Tuna empanadillas -----> 200 Rs.')
            print('3.  Butter chicken vol-au-vents -----> 280 Rs.')
            print('4.  Sweet fried saganaki -----> 250 Rs.')
            print('5.  Bacon rings -----> 100 Rs.')
            print('6.  Blooming onion -----> 150 Rs.')
            print('7.  Prawn and ginger dumplings -----> 270 Rs.')
            print('8.  Classic canape trio -----> 300 Rs.')
            print('9.  Classic tea -----> 100 Rs.')
            print('10. Classic Coffee -----> 150 Rs.')
            print('B.  Main Course')
            print('11. Cedar-plank salmon -----> 350 Rs.')
            print('12. Habanero BBQ shrimp -----> 390 Rs.')
            print('13. Fish tacos al pastor -----> 400 Rs.')
            print('14. Caesar salad roast chicken -----> 380 Rs.')
            print('15. Garlicky ramen noodle with grilled chicken thighs -----> 410 Rs.')                                                                                                                              
            print('16. Stuffed eggplants and zucchini with fresh red tomato sauce -----> 410 Rs.')
            print('17. Srilankan cashew curry -----> 350 Rs.')
            print('18. Tandoori rotti -----> 100 Rs.')
            print('19. Shahi biriyani -----> 400 Rs.')
            print('20. Kadai paneer -----> 310 Rs.')
            print('C.  Desserts')
            print('21. Chocolate-strawberry crumble ball -----> 310 Rs.')
            print('22. Chocolate mousse -----> 210 Rs.')
            print('23. Tiramisu -----> 180 Rs.')
            print('24. Apple Pie -----> 200 Rs.')
            print('25. Milk shake -----> 150 Rs.')
            while True:
                choice_dish =input("Enter Your Cusine : ")
                quantity=int(input("Enter the Quantity : "))
                if choice_dish=='1':
                    print("\nSO YOU HAVE ORDER: The ultimate cheese cake ")
                    restaurentbill = quantity * 100
                elif choice_dish=='2':
                    print("\nSO YOU HAVE ORDER: Tuna empanadillas ")
                    restaurentbill = quantity * 200
                elif choice_dish=='3':
                    print("\nSO YOU HAVE ORDER: Butter chicken vol-au-vents ")
                    restaurentbill= quantity * 280
                elif choice_dish=='4':
                    print("\nSO YOU HAVE ORDER: Sweet fried saganaki ")
                    restaurentbill= quantity * 250
                elif choice_dish=='5':
                    print("\nSO YOU HAVE ORDER: Bacon rings ")
                    restaurentbill= quantity * 100
                elif choice_dish=='6':
                    print("\nSO YOU HAVE ORDER: Blooming onion ")
                    restaurentbill= quantity * 150
                elif choice_dish=='7':
                    print("\nSO YOU HAVE ORDER: Prawn and ginger dumplings ")
                    restaurentbill= quantity * 270
                elif choice_dish=='8':
                    print("\nSO YOU HAVE ORDER: Classic canape trio ")
                    restaurentbill= quantity * 300
                elif choice_dish=='9':
                    print("\nSO YOU HAVE ORDER: Classic tea ")
                    restaurentbill= quantity * 100
                elif choice_dish=='10':
                    print("\nSO YOU HAVE ORDER: Classic Coffee ")
                    restaurentbill= quantity * 1500
                elif choice_dish=='11':
                    print("\nSO YOU HAVE ORDER: Cedar-plank salmon ")
                    restaurentbill= quantity * 350
                elif choice_dish=='12':
                    print("\nSO YOU HAVE ORDER: Habanero BBQ shrimp ")
                    restaurentbill= quantity * 390
                elif choice_dish=='13':
                    print("\nSO YOU HAVE ORDER: Fish tacos al pastor ")
                    restaurentbill= quantity * 400
                elif choice_dish=='14':
                    print("\nSO YOU HAVE ORDER: Caesar salad roast chicken ")
                    restaurentbill= quantity * 380
                elif choice_dish=='15':
                    print("\nSO YOU HAVE ORDER: Garlicky ramen noodle with grilled chicken thighs ")
                    restaurentbill= quantity * 410
                elif choice_dish=='16':
                    print("\nSO YOU HAVE ORDER: Stuffed eggplants and zucchini with fresh red tomato sauce ")
                    restaurentbill= quantity * 410
                elif choice_dish=='17':
                    print("\nSO YOU HAVE ORDER: Srilankan cashew curry ")
                    restaurentbill= quantity * 350
                elif choice_dish=='18':
                    print("\nSO YOU HAVE ORDER: Tandoori rotti ")
                    restaurentbill= quantity * 100
                elif choice_dish=='19':
                    print("\nSO YOU HAVE ORDER: Shahi biriyani ")
                    restaurentbill= quantity * 400
                elif choice_dish=='20':
                    print("\nSO YOU HAVE ORDER: Kadai paneer ")
                    restaurentbill= quantity * 310
                elif choice_dish=='21':
                    print("\nSO YOU HAVE ORDER: Chocolate-strawberry crumble ball ")
                    restaurentbill= quantity * 310
                elif choice_dish=='22':
                    print("\nSO YOU HAVE ORDER: Chocolate mousse ")
                    restaurentbill= quantity * 210
                elif choice_dish=='23':
                    print("\nSO YOU HAVE ORDER: Tiramisu ")
                    restaurentbill= quantity * 180
                elif choice_dish=='24':
                    print("\nSO YOU HAVE ORDER: Apple Pie ")
                    restaurentbill= quantity * 200
                elif choice_dish=='25':
                    print("\nSO YOU HAVE ORDER: Milk shake ")
                    restaurentbill= quantity * 150    
                else:
                    sys.stderr.write("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                    return
                list.append(restaurentbill)
                ch=input('Anything Else?? ')
                if ch=='yes':
                    continue
                elif ch=='no':
                    break
                else:
                    sys.stderr.write("\nwrong input")
                    break
            restaurentbill=sum(list)
            sql= "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s);"
            values= (cid,choice_dish,quantity,restaurentbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\nYour Total Bill Amount Is : Rs. ",restaurentbill)
            print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n" )
            cursor.close()
        else:
            sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")

def Gaming():
    global cid
    customer=searchCustomer()
    if customer:
        global gamingbill
        if connection:
            gamingbill=0
            cursor=connection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20),GAMES VARCHAR(30),HOURS VARCHAR(30),GAMING_BILL VARCHAR(30));"
            cursor.execute(createTable)
            list=[]
            list1=[]
            print("""
                 1. Table Tennis -----> 150 Rs./HR
                 2. Bowling -----> 100 Rs./HR
                 3. Snooker -----> 250 Rs./HR
                 4. Video Games -----> 300 Rs./HR
                 5. Swimming Pool Games -----> 350 Rs./HR
             """)
            while True:
                game=input("Enter What Game You Want To Play : ")
                hour=int(input("Enter No Of Hours You Want To Play : "))
                if game=='1':
                    print("YOU HAVE SELECTED TO PLAY : Table Tennis")
                    gamingbill = hour * 150
                elif game=='2':
                    print("YOU HAVE SELECTED TO PLAY : Bowling")
                    gamingbill = hour * 100
                elif game=='3':
                    print("YOU HAVE SELECTED TO PLAY : Snooker")
                    gamingbill = hour * 250
                elif game=='4':
                    print("YOU HAVE SELECTED TO PLAY : Video Games")
                    gamingbill = hour * 300
                elif game=='5':
                    print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
                    gamingbill = hour * 350
                else:
                    sys.stderr.write("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                    return
                list.append(gamingbill)
                list1.append(hour)
                ch=input('Anything Else?? ')
                if ch=='yes':
                    continue
                elif ch=='no':
                    break
                else:
                    sys.stderr.write("\nwrong input")
                    break
            gamingbill=sum(list)
            hour=sum(list1)
            sql= "INSERT INTO GAMING VALUES(%s,%s,%s,%s);"
            values= (cid,game,hour,gamingbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\nYour Total Gaming Bill Is : Rs. ",gamingbill)
            print("FOR : ",hour," HOURS","\n\n *** WE HOPE YOU WILL ENJOY YOUR GAME ***")
            cursor.close()
        else:
            sys.stderr.write("ERROR IN ESTABLISHING MYSQL CONNECTION !")

def laundary():
    global cid
    customer=searchCustomer()
    if customer:
        global laundarybill
        if connection:
            laundarybill=0
            cursor=connection.cursor()
            createTable ='CREATE TABLE IF NOT EXISTS laundary(CID VARCHAR(20),DRESS VARCHAR(20),AMOUNT VARCHAR(30),BILL VARCHAR(30));'
            cursor.execute(createTable)
            list=[]
            list1=[]
            list2=[]
            print("""
                 1. Shirt -----> 10 Rs.
                 2. Pant -----> 10 Rs.
                 3. Suit -----> 15 Rs.
                 4. Sari -----> 15 Rs.
                 5. InnerWear -----> 05 Rs.
            """)
            while True:
                dress=input("Enter your choice you want to wash: ")
                quantity=int(input("How many you want to wash: "))
                if dress=='1':
                    print("\nShirts")
                    laundarybill = quantity * 10
                elif dress=='2':
                    print("\nPant")
                    laundarybill = quantity * 10
                elif dress=='3':
                    print("\nSuit")
                    laundarybill = quantity * 15
                elif dress=='4':
                    print("\nSari")
                    laundarybill = quantity * 15
                elif dress=='5':
                    print("\nInnerWear")
                    laundarybill = quantity * 5
                else:
                    sys.stderr.write("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                    return
                list.append(laundarybill)
                list1.append(quantity)
                list2.append(dress)
                ch=input('Anything Else?? ')
                if ch=='yes':
                    continue
                elif ch=='no':
                    break
                else:
                    sys.stderr.write("\nwrong input")
                    break
            laundarybill=sum(list)
            quantity=sum(list1)
            sql= "INSERT INTO laundary VALUES(%s,%s,%s,%s);"
            values= (cid,dress,quantity,laundarybill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\nYOU SELECT ITEM NO : ",list2,"\n\nYOUR QUANTITY IS : ",quantity," ITEMS ")
            print("Your Total Bill Is : ",laundarybill)
            cursor.close()
        else:
            sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")

def totalAmount():
    global cid
    customer=searchCustomer()
    if customer:
        global grandTotal
        global roomrent
        global restaurentbill
        global laundarybill
        global gamingbill
        if connection:
            cursor=connection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20), CUST_NAME VARCHAR(30),ROOMRENT INT ,RESTAURENTBILL INT ,GAMINGBILL INT,LAUNDARYBILL INT,tax float(20.20), TOTALAMOUNT INT);"
            cursor.execute(createTable)
            sql= "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
            name = input("Enter Customer Name : ")
            grandTotal= roomrent + restaurentbill + laundarybill + gamingbill
            Gst=18/100*grandTotal
            grandTotal+=Gst
            values= (cid,name,roomrent,restaurentbill , gamingbill, laundarybill,Gst,grandTotal)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            cursor.close()
            print("\n ***** HOTEL BARATIE ***** CUSTOMER BIILING *****")
            print("\nCUSTOMER NAME : " ,name)
            print("\nROOM RENT : Rs. ",roomrent)
            print("\nRESTAURENT BILL : Rs. ",restaurentbill) 
            print("\nLAUNDAY BILL : Rs. ",laundarybill)
            print("\nGAMING BILL : Rs. ",gamingbill)
            print("\nGST @ 18% : Rs. ",Gst)
            print("___________________________________________________")
            print("\nTotal Amount Incl of All Taxes : Rs. ",grandTotal)
            roomrent=restaurentbill=gamingbill=laundarybill=0
            cursor.close()
        else:
            sys.stderr.write("\nERROR IN ESTABLISHING MYSQL CONNECTION !")

def searchOldBill():
    global cid
    customer=searchCustomer()
    if customer:
        if connection:
            cursor=connection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20), CUST_NAME VARCHAR(30),ROOMRENT INT ,RESTAURENTBILL INT ,GAMINGBILL INT,LAUNDARYBILL INT,tax float(20.20), TOTALAMOUNT INT);"
            cursor.execute(createTable)
            sql="SELECT * FROM TOTAL WHERE CID= %s;"
            cursor.execute(sql,(cid,))
            data=cursor.fetchall()
            if data:
                print(data)
            else:
                sys.stderr.write("\nSORRY, Record Not Found Try Again !")
                cursor.close()
        else:
            sys.stderr.write("\nSomthing Went Wrong ,Please Try Again !")

def all_customers():
    if connection:
        cursor=connection.cursor()
        createTable ='CREATE TABLE IF NOT EXISTS CUST_DETAILS(CID VARCHAR(20) unique,CUST_NAME VARCHAR(50), CUST_AGE VARCHAR(10), PHONE_NO VARCHAR(20),Cust_EMAIL VARCHAR(50));'
        cursor.execute(createTable)
        sql="SELECT * FROM CUST_DETAILS;"
        cursor.execute(sql)
        data=cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            sys.stderr.write("\nSORRY, Records Not Found Try Again !")
            return False
        cursor.close()

    else:
        sys.stderr.write("\nSomthing Went Wrong ,Please Try Again !")

def all_bills():
    if connection:
        cursor=connection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20), CUST_NAME VARCHAR(30),ROOMRENT INT ,RESTAURENTBILL INT ,GAMINGBILL INT,LAUNDARYBILL INT,tax float(20.20), TOTALAMOUNT INT);"
        cursor.execute(createTable)
        sql="SELECT * FROM TOTAL;"
        cursor.execute(sql)
        data=cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            sys.stderr.write("\nSORRY, Records Not Found Try Again !")
            return False
        cursor.close()

    else:
        sys.stderr.write("\nSomthing Went Wrong ,Please Try Again !")

print("****************************************************** HOTEL BARATIE *********************************************************")
connection = MYSQLconnectionCheck()
if connection:
    MYSQLconnection()
    while(True):
        print("""
                WELCOME
        1--->Enter Customer Details
        2--->Booking
        3--->Calculate Room Rent
        4--->Calculate Restaurant Bill
        5--->Calculate Gaming Bill
        6--->Calculate laundary Bill
        7--->Display Customer Details
        8--->GENERATE TOTAL BILL AMOUNT
        9--->GENERATE OLD BILL
        10--->Show All Customers
        11--->Show All Bills
        12--->EXIT
        """)
        choice = input("\nEnter Your Choice: ")
        if choice =='1':
            userEntry()
        elif choice =='2':
            booking()
        elif choice =='3':
            roomRent()
        elif choice =='4':
            Restaurent()
        elif choice =='5':
            Gaming()
        elif choice =='6':
            laundary()
        elif choice =='7':
            searchCustomer()
        elif choice =='8':
            totalAmount()
        elif choice =='9':
            searchOldBill()
        elif choice =='10':
            all_customers()
        elif choice =='11':
            all_bills()
        elif choice =='12':
            print("############################################# THANK YOU, VISIT AGAIN #############################################")
            break
        else:
            sys.stderr.write("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    sys.stderr.write("\nERROR ESTABLISHING MYSQL CONNECTION !")
# END OF PROJECT