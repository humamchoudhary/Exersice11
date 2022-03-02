from distutils.log import Log
from tkinter import E


Login = {
    "Humam": "1234Pakistan",
    "Tufail": "Password1234",
    "Ali": "Pak_1234",
    "Ahmed": "LongPassword"
    # Letting there are 6 more username and passwords
}
Usernames = list(Login.keys())
Passwords = list(Login.values())
usrname = input("Enter your name: ")
pswd = input("Enter your password: ")
try:
    if Login[usrname] == pswd:
        print("Logged in")
    elif Login[usrname] != pswd:
        print("Wrong password")
except KeyError:
    print("The username doesnt exists in the system!")
