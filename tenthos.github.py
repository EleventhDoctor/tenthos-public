from os import kill
import random
import time

accCount = 0

def developerMode():
    devpin = 131208
    print("Please enter the Development PIN.")
    devAttempt = input(">> ")
    devAttempt = int(devAttempt)
    if devAttempt == devpin:
        print("Welcome to Developer Mode! Loading...")
        time.sleep(1)
        print("Developer Menu")
        print("1) Account Manager")
        print("2) Menu")
        devChoice = input(">> ")
        if devChoice == "1":
            print("Loading Account Manager...")
            time.sleep(1)
            accManager()
        if devChoice == "2":
            print("Returning to menu...")
            time.sleep(1)
            menu()

            
def boot():
    print("TenthOS is booting...")
    time.sleep(1)
    print("Welcome to TenthOS, please login.")

def login():
    user1 = input("Please enter your Username: ")
    if user1 == account.username:
        print("Username chosen: " + account.username + " .")
        pin1 = input("Please enter your PIN: ")
        if pin1 == account.pin:
            print("Welcome! Loading user prefrences...")
    else:
        print("Account not detected. Please try again.")
        login()

def menu():
    print("Menu Options")
    print("1) Terminal (Beta)")
    print("2) Account Manager")
    print("3) Shutdown OS")
    print("4) Developer Mode")
    choice = input(">> ")
    if choice == "1":
        print("Booting TenthTerminal...")
        time.sleep(1)
        terminal()
    elif choice == "2":
        print("This feature has not been implimented yet. Returning to menu...")
        time.sleep(1)
        menu()
    elif choice == "3":
        print("Shutting down TenthOS...")
        shutdown()
    elif choice == "4":
        print("Loading...")
        time.sleep(1)
        developerMode()
    else:
        menu()


    
def accCreator():
    print("Welcome to Account Creator.")
    if accCount == 5:
            print("Account Creator is not avaliable. Returning to Manager Menu...")
            accManager()
    if accCount == 1:
        class account2:
            username = input("Please enter a username: ")
            pin= input("Please enter a PIN: ")
            accCount + 1
        print("Account Slots Remaining: " + 5 - accCount)
        
    elif accCount == 2:
        class account3:
            username = input("Please enter a username: ")
            pin = input("Please enter a PIN: ")
            accCount + 1
        print("Account Slots Remaining: " + 5 - accCount)
    elif accCount == 3:
        class account4:
            username = input("Please enter a username: ")
            pin = input("Please enter a PIN: ")
            accCount + 1
        print("Account Slots Remaining: " + 5 - accCount)
    elif accCount == 4:
        class account5:
            username = input("Please enter a username: ")
            pin = input("Please enter a PIN: ")
            accCount + 1
        print("Account Slots Remaining: " + 5 - accCount)

def accManager():
    print("Welcome to Account Manager!")
    print("Please select an option:")
    print("1) Account Creator")
    print("2) Account Management")
    accManagerChoice = input(">> ")
    if accManagerChoice == "1":
        print("Loading Account Creator...")
        accCreator()
        

def shutdown():
    print("TenthOS is shutting down...")
    kill()

def terminal():
    print("Welcome to terminal, please enter a command on the next line.")
    chosencommand = input("> ")
    if chosencommand == "help" or chosencommand == "Help":
        print("TenthTerminal v1.0.0")
        print("This terminal is not scripted yet.")
    elif chosencommand == "shutdown":
        shutdown()
    elif chosencommand == "menu":
        print("Returning to menu...")
        time.sleep(1)
        menu()    

print("Welcome to TenthOS! This OS is TEXT BASED.")
time.sleep(1)

print("Please setup your account.")

class account:
    username = input("Please enter a username: ")
    pin = input("Please enter a PIN: ")
    accCount + 1

if account.username == "stark":
    print("Would you like to enable JARVIS? (y/n")
    jarvisEnabled = input(">> ")
    if jarvisEnabled == "Y" or jarvisEnabled == "y":
        print("Welcome to your new OS, sir.")
        time.sleep(1)
        print("Checking Storage Avaliability...")
        print("Storage Avaliabe on TENTHOS: 98%")
        jarvisEnabled = False
print("Thank you for setting up your account. This account will hold ADMINISTRATOR status.")
time.sleep(2)
boot()
login()
time.sleep(2)
print("")
menu()