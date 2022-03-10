from validation import *
from viewProject import view

def editName(userId, projectName, newName):
    info = []
    newList = []
    flag = False
    name = isValidName
    counter = 0
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if str(userId) in i and str(projectName) in i:    
                x = str(i).split("|")

                x[1] = str(newName)
                newList = [x[0],x[1],x[2],x[3],x[4],x[5]]
                newList = '|'.join(newList)
                # print("info..", info[counter])
                info[counter] = str(newList)
                # print("new..", info[counter])
            counter +=1

    with open('proInfo', 'w') as file:
        for i in info:
          file.writelines(str(i + "\n"))
    print("Edit Succes")

    
def editDetail(userId, projectName, newDetails):
    info = []
    newList = []
    flag = False
    name = isValidName
    counter = 0
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if str(userId) in i and str(projectName) in i: 
                x = str(i).split("|")

                x[2] = str(newDetails)
                newList = [x[0],x[1],x[2],x[3],x[4],x[5]]
                newList = '|'.join(newList)
                # print("info..", info[counter])
                info[counter] = str(newList)
                # print("new..", info[counter])
            counter +=1

    with open('proInfo', 'w') as file:
        for i in info:
          file.writelines(str(i + "\n"))
    print("Edit Succes")



def editTarget(userId, projectName, newTarget):
    info = []
    newList = []
    flag = False
    name = isValidName
    counter = 0
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if str(userId) in i and str(projectName) in i: 
                x = str(i).split("|")

                x[3] = str(newTarget)
                newList = [x[0],x[1],x[2],x[3],x[4],x[5]]
                newList = '|'.join(newList)
                # print("info..", info[counter])
                info[counter] = str(newList)
                # print("new..", info[counter])
            counter +=1

    with open('proInfo', 'w') as file:
        for i in info:
          file.writelines(str(i + "\n"))
    print("Edit Succes")



def editDate(userId, projectName, newDate):
    info = []
    newList = []
    flag = False
    name = isValidName
    counter = 0
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if str(userId) in i and str(projectName) in i:
                x = str(i).split("|")

                x[4] = str(newDate)
                newList = [x[0],x[1],x[2],x[3],x[4],x[5]]
                newList = '|'.join(newList)
                # print("info..", info[counter])
                info[counter] = str(newList)
                # print("new..", info[counter])
            counter +=1

    with open('proInfo', 'w') as file:
        for i in info:
          file.writelines(str(i + "\n"))
    print("Edit Succes")