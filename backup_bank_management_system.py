import pandas as pd
import csv
import os
import pyttsx3

speaker = pyttsx3.init()


def data():
    speaker.say("You have selected to Input and Write Data..")
    speaker.runAndWait()
    f = open("bank.csv", "a", newline="")
    w = csv.writer(f)
    speaker.say("Enter the number of accounts you want to add..")
    speaker.runAndWait()
    n = int(input("Enter the number of accounts you want to add: "))
    for x in range(n):
        speaker.say("Enter the account number..")
        speaker.runAndWait()
        a = int(input("Enter the account number : "))
        speaker.say("Enter the name of the account holder..")
        speaker.runAndWait()
        n = input("Enter the name of the account holder: ")
        speaker.say("Enter the balance amount..")
        speaker.runAndWait()
        b = int(input("enter the balance amount :"))
        l = [a, n, b]
        w.writerow(l)
    f.close()


def display():
    speaker.say("You have selected to Display the Accounts with details..")
    speaker.runAndWait()
    f = open("bank.csv", "r", newline="")
    acct = csv.reader(f)
    for i in acct:
        print(i)
    f.close()


def delete():
    speaker.say("You have selected to Delete the data..")
    speaker.runAndWait()
    updatedlist = []
    with open("bank.csv", newline="") as f:
        reader = csv.reader(f)
        speaker.say(
            "Enter the account number of the account holder you wish to remove from file.."
        )
        speaker.runAndWait()
        number = input(
            "Enter the account number of the account holder you wish to remove from file: "
        )
        for row in reader:
            if row[0] != number:
                updatedlist.append(row)
        updatefile(updatedlist)


def updatefile(updatedlist):
    speaker.say("Updating the File..")
    speaker.runAndWait()
    with open("bank.csv", "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        speaker.say("The file has been updated..")
        speaker.runAndWait()
        print("The file has been updated")


file = os.path.exists("bank.csv")
if file:
    None
else:
    df = pd.DataFrame(columns=["ACCOUNT NO", "NAME", "BALANCE"])
    df.to_csv("bank.csv", index=False)
df = pd.read_csv("bank.csv")
a = "ACCOUNT NO"
if a not in df:
    df = pd.DataFrame(columns=["ACCOUNT NO", "NAME", "BALANCE"])
    df.to_csv("bank.csv", index=False)
else:
    None
while True:
    print()
    print("------------------------")
    print("-BANK MANAGEMENT SYSTEM-")
    print("------------------------")
    speaker.say("WELCOME TO THE BANK MANAGEMENT SYSTEM")
    speaker.runAndWait()
    # print("MENU \n 1 = Input & Write Data \n 2 = Display \n 3 = Delete Data \n 4 = Exit")
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
    speaker.say("4. Exit")
    print("4. Exit")
    speaker.runAndWait()
    speaker.say("You can enter your choice now..")
    speaker.runAndWait()
    ch = int(input("enter your choice: "))
    if (
        ch == 1
        or ch == "input data"
        or ch == "Input Data"
        or ch == "INPUT DATA"
        or ch == "inputdata"
        or ch == "INPUTDATA"
        or ch == "input & write data"
        or ch == "Input & Write Data"
        or ch == "INPUT&WRITEDATA"
        or ch == "input and write data"
    ):
        data()
    elif ch == 2 or ch == "DISPLAY" or ch == "display" or ch == "data" or ch == "DATA":
        display()
    elif (
        ch == 3
        or ch == "delete"
        or ch == "DELETE"
        or ch == "erase"
        or ch == "ERASE"
        or ch == "Delete"
        or ch == "Erase"
    ):
        delete()
    elif (
        ch == 4
        or ch == "quit"
        or ch == "QUIT"
        or ch == "exit"
        or ch == "EXIT"
        or ch == "end"
        or ch == "END"
    ):
        speaker.say("Thank You for using the Bank Management System")
        speaker.runAndWait()
        print("Thank You for using the Bank Management System")
        exit()
    else:
        speaker.say("INVALID!!!")
        speaker.runAndWait()
        print("INVALID!!!")
        speaker.say("CLOSING THE SYSTEM...")
        speaker.runAndWait()
        exit()
