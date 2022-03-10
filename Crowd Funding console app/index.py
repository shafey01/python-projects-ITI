from login import login
from signup import signup
from mainmenu import mainmenu


def menu():
    choose = str(input("For login write l and signup write s and exit write e: "))

    if choose == "l":
        
        userId = login()
        if(userId != False):
            mainmenu(userId)
        else:
            print("this account dosen't exist , please sign up !!!")
            menu()
    elif choose == "s":
        signup()
        menu()
    elif choose == "e":
        exit()
    else:
        print("Enter valid options")
        return menu()


menu()
