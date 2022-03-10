from search import search
from validation import *
from viewProject import view

def searchpro(userId, proname):
    info = []
    newList = []
    flag = False
    # name = isValidName()
    # date = isValidDate()
    counter = 0
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if userId in i and str(proname) in i:  
                # x = str(i).split("|")

                # print(f"{x[1]} {x[2]} {x[3]} {x[4]}")
                # newList = [x[0],x[1],x[2],x[3],x[4],x[5]]
                # newList = '|'.join(newList)
                # print("info..", info[counter])
                # info[counter] = str(newList)
                # print("new..", info[counter])
                flag = True
            # counter +=1
    # if flag == False:
    #     print("There is no projects in this date !!! ")
    return flag


def deletePro(userId):
    
    info = []
    newList = []
    
    counter = 0
    flag = view(userId)
    
    if flag == False:
        print("no projects to delete !!")
    else:
        projectName = isValidNamefordelete()
        # name = isValidName()

        valid = searchpro(userId, projectName)
        if valid == False:
            print("no projects with this name")
        else:

            with open('proInfo', 'r') as file:
                userInfo = file.readlines()
                for i in range(len(userInfo)):
                    x = userInfo[i].strip("\n")
                    info.append(x)

                info = list(info)
                # print(info)
                for i in info:
                    
                    if str(userId) in i and str(projectName) in i:
                        x = str(i).split("|")

                        # print("index of",counter) 
                        # print("index of .....", info[counter])
                        break  
                        # x[1] = str(newName)
                        # newList = [x[0],x[1],x[2],x[3],x[4],x[5]]
                        # newList = '|'.join(newList)
                        # print("info..", info[counter])
                        # info[counter] = str(newList)
                        # print("new..", info[counter])
                    counter +=1

            info.pop(counter)
            # print(len(info))

            with open('proInfo', 'w') as file:
                for i in info:
                    file.writelines(str(i + "\n"))
            print("Delete Succes")