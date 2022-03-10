
from validation import *

def login():
    info = []
    flag = False
    email = isValidEmail()
    password = input("Enter your password : ")
    with open('usersInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if email in i and str(password) in i:
                x = str(i).split("|")

                flag = True
                return x[0]
    return flag

        
            
        
    

