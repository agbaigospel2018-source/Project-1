"""
To check if the username and password is accurate and matches the one entered by the user
"""

import getpass
import stdiomask
username = input("Create your username: ")
password = int(stdiomask.getpass("Create your password: "))

while True:
    user = input("Enter your username: ").title()
    if user == username:
        print("Correct username.")
        break
    else:
        print("Access denied. Enter a correct username: ")
        
count = 0

while count < 4:    
    digit = int(stdiomask.getpass("Enter your 4-digit password: "))
    if digit == password:
        print("Access granted.")
        break
    else: 
        print("Incorrect password. Enter a correct password")
        count +=1
if count == 4:
    print("Too many failed attempts.")
            