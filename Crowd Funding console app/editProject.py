from editMethods import *
# from mainmenu import mainmenu
from viewProject import view




def edit(userId):
    
    flag = view(userId)
    if flag == False:
        print("no projects yet")
    else:
        while True:
            choose = input("Enter your choosec for edit,\n (n) for project Name,\n (d) for project Details,\n (t) for Total target,\n (a) for The Date \n (x) for exit, \nEnter: ")

            if choose == "n":
                view(userId)
                proname = input("Enter your project name you want to edit the name of it : ")
                newName = input("Enter your new project name : ")
                editName(userId, proname, newName)
                break
                
            elif choose == "d":
                view(userId)
                proname = input("Enter your project name you want to edit the Details of it : ")
                newDetails = input("Enter your new project Dtails : ")
                editDetail(userId, proname, newDetails)
                break
            elif choose == "t":
                view(userId)
                proname = input("Enter your project name you want to edit the Total Target of it : ")
                newtarget = isValidTotal()
                editTarget(userId,proname,newtarget)
                break

            elif choose == "a":
                view(userId)
                proname = input("Enter your project name you want to edit the Date of it : ")
                newDate = isValidDate()
                editDate(userId,proname,newDate)
                break
            
                
            elif choose == "x":
                exit()
                
            else:
                print("Enter valid options")
            


