def dry_ground(terrain):
    iter = 0
    answerList = []
    list1 = getmap(terrain)
    count = getCount(list1)
    water_level = -0.5
    flood_counter = 0
    ############################ Do work here ############################
    print("dry land: ", count, "\n")
    printmap(list1)
    answerList.append(countZeros(list1))
    
    while iter < 3:
        for i in range(0,len(list1)):
            for j in range(0, len(list1[i])):
                if list1[i][j]%1 != 0:
                    list1[i][j] += 1
        flood_counter = 0
        water_level += 1
        while flood_counter < 40:
            for i in range(0,len(list1)):
                if i == 0:
                    try:
                        for j in range(0, len(list1[i])):
                            if list1[i][j] == water_level and list1[i+1][j] < water_level:
                                list1[i+1][j] = water_level
                            if list1[i][j] == water_level and list1[i][j-1] < water_level:
                                if j-1 != -1:
                                    list1[i][j-1] = water_level
                            if list1[i][j] == water_level and list1[i][j+1] < water_level:
                                list1[i][j+1] = water_level
                    except IndexError:
                        continue
                elif i == len(list1)-1:
                    try:
                        for j in range(0, len(list1[i])):
                            if list1[i][j] == water_level and list1[i-1][j] < water_level:
                                list1[i-1][j] = water_level
                            if list1[i][j] == water_level and list1[i][j-1] < water_level:
                                if j-1 != -1:
                                    list1[i][j-1] = water_level
                            if list1[i][j] == water_level and list1[i][j+1] < water_level:
                                list1[i][j+1] = water_level
                    except IndexError:
                        continue
                else: 
                    for j in range(0, len(list1[i])):
                        try:
                            if list1[i][j] == water_level and list1[i-1][j] < water_level:
                                list1[i-1][j] = water_level
                            if list1[i][j] == water_level and list1[i+1][j] < water_level:
                                list1[i+1][j] = water_level
                            if list1[i][j] == water_level and list1[i][j-1] < water_level:
                                if j-1 != -1:
                                    list1[i][j-1] = water_level
                            if list1[i][j] == water_level and list1[i][j+1] < water_level:
                                list1[i][j+1] = water_level
                        except IndexError:
                            continue
            flood_counter += 1
        
        iter += 1
        print("dry land: ", countZeros(list1), "\n")
        printmap(list1)

        answerList.append(countZeros(list1))
        
    ########################### Stop work here ############################

    print("\n",answerList)
    a = answerList[0]
    b = answerList[1]
    c = answerList[2]
    d = answerList[3]
    return a,b,c,d
######################################### DONT TOUCH BELOW ##################################
def getmap(terrain):
    list1, list2, line = [], [], []
    currentLevel, iter = 0, 0
    step = "list1"
    
    for i in terrain:
        for j in i:
            if j == " ":
                line.append(0)
            elif j == "-":
                line.append(-.5)
            else:
                line.append(1)
        list1.append(line)
        line = []

    while iter < 24:
        currentLevel += 1
        if step == "list1": ################################################ FLIP
            list2 = []
            
            for i in range(0,len(list1)):

                if i == 0:
                    list2.append(list1[i])
                else:
                    for j in range(0, len(list1[i])):
                        try:
                            if j == 0:
                                line.append(list1[i][j])
                            elif list1[i][j] == currentLevel and list1[i-1][j] == currentLevel and list1[i+1][j] == currentLevel and list1[i][j-1] == currentLevel and list1[i][j+1] == currentLevel:
                                line.append(currentLevel + 1)
                            else:
                                line.append(list1[i][j])
                        except IndexError:
                            line.append(list1[i][j])
                    list2.append(line)
                    line = []
            step = "list2"
        if step == "list2":  ###################################################### FLIP
            list1 = []
            for i in range(0,len(list2)):
                if i == 0:
                    list1.append(list2[i])
                else:
                    for j in range(0, len(list2[i])): 
                        try:
                            if j == 0:
                                line.append(list1[i][j])
                            elif list2[i][j] == currentLevel and list2[i-1][j] == currentLevel and list2[i+1][j] == currentLevel and list2[i][j-1] == currentLevel and list2[i][j+1] == currentLevel:
                                line.append(currentLevel + 1)
                            else:
                                line.append(list2[i][j])
                        except IndexError:
                            line.append(list2[i][j])
                    list1.append(line)
                    line = []
            step = "list1"
        iter += 1
        
    return list1

def printmap(list):
    line= ""
    for i in list:
        for j in i:
            if j == 0:
                line += " "
            elif j%1 != 0:
                line += "-"
            else:
                line += str(j)
        print(line)
        line = ""

def printNumMap(list):
    for i in list:
        print(i)
        
def countZeros(list):
    count = 0
    for i in list:
        for j in i:
            if j%1 == 0:
                count += 1
    return count
    
def getCount(list):
    x = 0
    for i in list:
        for j in i:
            x += 1
    return x
