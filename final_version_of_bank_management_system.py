import pandas as pd
import os
import pyttsx3
import sys
import datetime
speaker=pyttsx3.init()
def data():
    speaker.say("You have selected to Input and Write Data..")
    speaker.runAndWait()
    a=pd.read_csv("bank.csv")
    speaker.say("Please enter the details for the account number, account holder and its amount..")
    speaker.runAndWait()
    z=int(input('Please enter account number: '))
    try:
        b=a[a["ACCOUNT NO"]==z].index.values
        b=b[0]
        speaker.say("This account number already exists..")
        print("This account number already exists")
        speaker.runAndWait()
    except:
        y=input("Please enter the account holder's name: ")
        x=int(input('Please enter the amount: '))
        a1=pd.DataFrame({"ACCOUNT NO":z,"NAME":y,"BALANCE":x},index=[0])
        a=a.append(a1)
        a.to_csv("bank.csv",index=False)
        speaker.say("Data has been added..")
        print("Data has been added")
        speaker.runAndWait()
def display():
    speaker.say("You have selected to Display the Accounts with details..")
    speaker.runAndWait()
    a=pd.read_csv("bank.csv")
    print(a)
def delete():
    speaker.say("You have selected to Delete Data..")
    speaker.runAndWait()
    a=pd.read_csv("bank.csv")
    speaker.say("Please enter the account number you want to delete from the data..")
    speaker.runAndWait()
    z=int(input("Please enter the account number you want to delete from the data: "))
    try:
        I=a[a["ACCOUNT NO"]==z].index.values
        I=I[0]
        try:
            j=(a[a["ACCOUNT NO"]==z].index.values)
            a=a.drop(index=j)
            a.to_csv("bank.csv",index=False)
            speaker.say("The account has been deleted..")
            print("The account has been deleted")
            speaker.runAndWait()
        except:
            speaker.say("This account does not exist..")
            print("This account does not exist")
            speaker.runAndWait()
    except IndexError:
        speaker.say("This account does not exist..")
        print("This account does not exist")
        speaker.runAndWait()
def withdraw():
    speaker.say("You have selected to Withdraw from an account..")
    speaker.runAndWait()
    try:
        a=pd.read_csv("bank.csv")
        speaker.say("Please enter the account number and the amount that is being withdrawn..")
        speaker.runAndWait()
        z=int(input("enter the account number: "))
        x=int(input("enter the amount: "))
        i=a[a["ACCOUNT NO"]==z].index.values
        i=i[0]
        b=a.xs(i)["BALANCE"]
        if x > b:
            print("INVALID")
            print("The amount in the account is",b)
        else:
            nb=b-x
            a.loc[i,"BALANCE"]=nb
            a.to_csv("bank.csv",index=False)
            speaker.say("The amount has been debited to the account..")
            print("Rs.",x,"has been debited to the account")
            a=pd.read_csv('bank.csv')
            print("Balance amount in the account is:",a.xs(i)["BALANCE"])
            speaker.runAndWait()
    except IndexError:
        speaker.say("INVALID")
        print("INVALID")
        speaker.runAndWait()
def deposit():
    speaker.say("You have selected to Deposit to an account..")
    speaker.runAndWait()
    try:
        a=pd.read_csv("bank.csv")
        speaker.say("Please enter the account number and the amount that is being deposited..")
        speaker.runAndWait()
        z=int(input("enter the account number: "))
        x=int(input("enter the amount: "))
        i=a[a["ACCOUNT NO"]==z].index.values
        i=i[0]
        b=a.xs(i)["BALANCE"]
        nb=b+x
        a.loc[i,"BALANCE"]=nb
        speaker.say("The amount has been deposited in the account..")
        print("The amount has been credited to the account")
        print("The amount credited to the account is",x)
        print("Balance:",a.xs(i)["BALANCE"])
        speaker.runAndWait()
        a.to_csv("bank.csv",index=False)
    except IndexError:
        speaker.say("INVALID")
        print("INVALID")
        speaker.runAndWait()
def search():
    a=pd.read_csv("bank.csv")
    speaker.say("Please enter the account number you want to see the details about..")
    speaker.runAndWait()
    l=int(input("Please enter the account number you want to see the details about: "))
    try:
        b=a[a["ACCOUNT NO"]==l].index
        b=b[0]
        try:
            b=a[a["ACCOUNT NO"]==l].index
            print(a.loc[b])
        except:
            None
    except:
        speaker.say("This account does not exist..")
        print("This account does not exist")
        speaker.runAndWait()
f=os.path.exists("login.csv")
if f:
    None
else:
    z=pd.DataFrame({'username':['mehulverma','mayank','tanisha','mansha'],'user id':['Mehul Verma','Mayank Jain','Tanisha Saigal','Mansha'],'password':['26052004','m1234','t1234','ma1234']})
    z.to_csv('login.csv',index=False)
try:
    df=pd.read_csv("login.csv")
except:
    z=pd.DataFrame({'username':['mehulverma','mayank','tanisha','mansha'],'user id':['Mehul Verma','Mayank Jain','Tanisha Saigal','Mansha'],'password':['26052004','m1234','t1234','ma1234']})
    z.to_csv('login.csv',index=False)
def login():
    a=pd.read_csv('login.csv')
    speaker.say("To access the bank management system please enter your username and password..")
    speaker.runAndWait()
    b=input("Please enter your username: ")
    try:
        I=a[a["username"]==b].index.values
        I=I[0]
        try:
            c=input("Please enter your password: ")
            C=a[a["password"]==c].index.values
            C=C[0]
            l="Welcome",a.xs(C)['user id']
            print()
            speaker.say(l)
            print("Welcome",a.xs(C)['user id'])
            speaker.runAndWait()
        except:
            speaker.say("wrong password..")
            print("wrong password")
            speaker.runAndWait()
            sys.exit()
    except:
        speaker.say("wrong username..")
        print("wrong username")
        speaker.runAndWait()
        sys.exit()
mv= os.path.exists("bank.csv")
if mv:
    None
else:
    df = pd.DataFrame(columns=["ACCOUNT NO","NAME","BALANCE"])
    df.to_csv('bank.csv',index=False)
try:
    df=pd.read_csv("bank.csv")
except:
    df = pd.DataFrame(columns=["ACCOUNT NO","NAME","BALANCE"])
    df.to_csv('bank.csv',index=False)
login()
print()
print(datetime.datetime.today().strftime("%A"),"\t\t",datetime.datetime.now())
while True:
    print()
    print("------------------------")
    print("-BANK MANAGEMENT SYSTEM-")
    print("------------------------")
    speaker.say("WELCOME TO THE BANK MANAGEMENT SYSTEM")
    speaker.runAndWait()
    speaker.say("MENU")
    print("MENU")    
    speaker.runAndWait()
    speaker.say("1. Input & Write Data")
    print("1. Input & Write Data")
    speaker.runAndWait()
    speaker.say("2. Display")
    print("2. Display")
    speaker.runAndWait()
    speaker.say("3. Delete Data")
    print("3. Delete Data")
    speaker.runAndWait()
    speaker.say("4. withdraw or deposit money")
    print("4. Withdraw or Deposit money")
    speaker.runAndWait()
    speaker.say("5. Search")
    print("5. Search")
    speaker.runAndWait()
    speaker.say("6. Exit")
    print("6. Exit")
    speaker.runAndWait()
    speaker.say("You can enter your choice now..")
    speaker.runAndWait()
    ch=input("enter your choice: ")
    if ch=="1" or ch=='input data' or ch=='Input Data' or ch=='INPUT DATA' or ch=='inputdata' or ch=='INPUTDATA' or ch=='input & write data' or ch=='Input & Write Data' or ch=='INPUT&WRITEDATA' or ch=='input and write data':
        data()
    elif ch=="2" or ch=='DISPLAY' or ch=='display' or ch=='data' or ch=='DATA':
        display()
    elif ch=="3" or ch=='delete' or ch=='DELETE' or ch=='erase' or ch=='ERASE' or ch=='Delete' or ch=='Erase':
        delete()
    elif ch=="4":
        speaker.say("Do you want to withdraw or deposit money from the account?..")
        speaker.runAndWait()
        a=input("Do you want to withdraw or deposit money from the account? : \n 1. withdraw \n 2.deposit")
        if a=="1" or a=="withdraw" or a=="Withdraw" or a=="WITHDRAW":
            withdraw()
        elif a=="2" or a=="deposit" or a=="Deposit" or a=="DEPOSIT":
            deposit()
        else:
            speaker.say("Invalid!!!")
            print("Invalid!!!")
            speaker.runAndWait()
    elif ch=="5" or ch=="search" or ch=="Search" or ch=="SEARCH":
        search()
    elif ch=="6" or ch=='quit' or ch=='QUIT' or ch=='exit' or ch=='EXIT' or ch=='end' or ch=='END':
        speaker.say("Thank You for using the Bank Management System")
        speaker.runAndWait()
        print("Thank You for using the Bank Management System")
        sys.exit()
    else:
        speaker.say("INVALID!!!")
        speaker.runAndWait()
        print("Invalid!!!")
        speaker.say("CLOSING THE SYSTEM...")
        speaker.runAndWait()
        sys.exit()