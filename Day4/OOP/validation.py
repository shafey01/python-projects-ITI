import re


emailRegex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
dateRegex = re.compile(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$')

def isValidEmail():
    while True:
        email = input("Enter your Email : ")
        if re.fullmatch(emailRegex, email):
            return email

def isValidEmailFrom():
    while True:
        email = input("Enter the Email you want send from : ")
        if re.fullmatch(emailRegex, email):
            return email
        print("Please Enter valid Email !!!")
        

def isValidEmailTo():
    while True:
        email = input("Enter the Email you want send to : ")
        if re.fullmatch(emailRegex, email):
            return email
        print("Please Enter valid Email !!!")
        


def isValidDate():
    while True:
        date = input("Enter your the Date : ")
        if re.fullmatch(dateRegex, date):
            return date



def isValidName():
    while True:
        name = input("Enter your name : ")
        x = name.isalpha()
        if x:
            return name

def emailsubject():
    while True:
        name = input("Enter your email subject : ")
        # x = name.isalpha()
        if isinstance(name, str):
            return name
        print("Email subject must be alphabetic ")
        

def isValidNamefordelete():
    while True:
        name = input("Enter your project name to delete : ")
        # x = name.isalpha()
        if isinstance(name, str):
            return name

def isValidNameProject():
    while True:
        name = input("Enter your Project Name : ")
        x = name.isalpha()
        if x:
            return name


def isValidPass():
    while True:
        password = input("Enter your Pass : ")
        x = password.isalnum()
        if x:
            return password


def isValidPhone():
    while True:
        phone = input("Enter your phone : ")
        if phone.isdigit():
            return phone





def isValidTotal():
    while True:
        phone = input("Enter your Total Target : ")
        if phone.isdigit():
            return phone







