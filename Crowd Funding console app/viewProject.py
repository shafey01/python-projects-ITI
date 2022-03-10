
def view(userId):
    info = []
    flag = False
    counter = 0
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if userId in i:
                counter +=1
                x = str(i).split("|")
                print(f"{counter}) {x[1]}" )
                flag = True
    if(flag == False):
        print("there is no projects yet")
        return flag