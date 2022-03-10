import datetime
from validation import *

def isUnique(projectName):
    info = []
    flag = True
    
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        
        if len(info) > 1:
            for i in info:
                
                # x = str(i).split("|")
                if projectName in i:
                    flag = False

    return flag




def create(userId):
    flag = False
    while True:

        projectName = isValidNameProject()
        res = isUnique(projectName)
        if res == True:
            break
        else:
            print("Please enter unique Project Name ..")
        

    details = input("Enter your details about your project : ")
    totalTarget = isValidTotal()
    date = isValidDate()
    projectId = str(datetime.datetime.now())

    proinfo = [projectId,projectName,details,totalTarget,date, userId]
    proinfo2 = "|".join(proinfo)
    with open('proInfo', 'a') as file:
        file.writelines(str(proinfo2 + "\n"))
        print("creation Succes")
        flag = True
    


    


        