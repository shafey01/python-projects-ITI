from validation import isValidDate, isValidName

def search(userId):
    info = []
    newList = []
    flag = False
    # name = isValidName()
    date = isValidDate()
    counter = 0
    
    with open('proInfo', 'r') as file:
        userInfo = file.readlines()
        for i in range(len(userInfo)):
            x = userInfo[i].strip("\n")
            info.append(x)

        info = list(info)
        for i in info:
            
            if userId in i and str(date) in i:  
                x = str(i).split("|")

                print(f"{x[1]} {x[2]} {x[3]} {x[4]}")
                # newList = [x[0],x[1],x[2],x[3],x[4],x[5]]
                # newList = '|'.join(newList)
                # print("info..", info[counter])
                # info[counter] = str(newList)
                # print("new..", info[counter])
                flag = True
            # counter +=1
    if flag == False:
        print("There is no projects in this date !!! ")

    