from createProject import create
from deleteProject import deletePro
from viewProject import view
from editProject import edit
from search import search



def mainmenu(id):

    while True:
        choose = input("Enter your choose , c for create , v for view, e for edit, s for search, d for delete , x for exit : ")

        if choose == "c":
            create(id)
        elif choose == "v":
            view(id)
        
        elif choose == "e":
            edit(id)
            
        elif choose == "d":
            # view(id)
            deletePro(id)
            
        elif choose == "s":
            search(id)
        elif choose == "x":
            exit()

        else:
            print("Enter valid options")
            # return mainmenu(id)


