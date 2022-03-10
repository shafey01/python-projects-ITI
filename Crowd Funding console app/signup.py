import datetime
from login import login
from validation import *


def valid(_email):
    info = []
    flag = False
    # email = isValidEmail()
    # password = input("Enter your password : ")
    with open('usersInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            x = str(i).split("|")
            if str(_email) in i:
                print("email exist")
                return 1
           

        
            
        
    



def signup():
    name = isValidName()
    password = isValidPass()
    email = isValidEmail()
    phone = isValidPhone()
    id = str(datetime.datetime.now())
    userinfo = [id,name,password,email,phone]
    userinfo = "|".join(userinfo)
    check = valid(email)
    if(check == 1):
         print("try another email please")
        
    else:
        with open('usersInfo', 'a') as file:
            file.writelines(str(userinfo + "\n"))
            print("Signup Succes")
       




