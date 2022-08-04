#Codewars Challenge: A bird flying high above a mountain range is able to estimate the height of the highest peak. Can you?
#Example
#The birds-eye view

#^^^^^^
# ^^^^^^^^
#  ^^^^^^^
#  ^^^^^
#  ^^^^^^^^^^^
#  ^^^^^^
#  ^^^^

# The bird-brain calculations

#111111
# 1^^^^111
#  1^^^^11
#  1^^^1
#  1^^^^111111
#  1^^^11
#  1111

#111111
# 12222111
#  12^^211
#  12^21
#  12^^2111111
#  122211
#  1111

#111111
# 12222111
#  1233211
#  12321
#  12332111111
#  122211
#  1111

#Height = 3

mountain = [
          "^^^^^^        ",
          " ^^^^^^^^     ",
          "  ^^^^^^^     ",
          "  ^^^^^       ",
          "  ^^^^^^^^^^^ ",
          "  ^^^^^^      ",
          "  ^^^^        "] 

def peak_height(mountain):
    list1, list2, line = [], [], []
    currentLevel, iter = 0, 0
    step = "list1"
    
    for i in mountain:
        for j in i:
            if j == " ":
                line.append(0)
            else:
                line.append(1)
        list1.append(line)
        line = []

    while iter < 24:
        currentLevel += 1
        if step == "list1": ################################################
            list2 = []
            
            for i in range(0,len(list1)):

                if i == 0:
                    list2.append(list1[i])
                else:
                    for j in range(0, len(list1[i])):
                        try:
                            if list1[i][j] == currentLevel and list1[i-1][j] == currentLevel and list1[i+1][j] == currentLevel and list1[i][j-1] == currentLevel and list1[i][j+1] == currentLevel:
                                line.append(currentLevel + 1)
                            else:
                                line.append(list1[i][j])
                        except IndexError:
                            line.append(list1[i][j])
                    list2.append(line)
                    line = []
            step = "list2"
        if step == "list2":  ######################################################
            list1 = []
            for i in range(0,len(list2)):
                if i == 0:
                    list1.append(list2[i])
                else:
                    for j in range(0, len(list2[i])): 
                        try:
                            if list2[i][j] == currentLevel and list2[i-1][j] == currentLevel and list2[i+1][j] == currentLevel and list2[i][j-1] == currentLevel and list2[i][j+1] == currentLevel:
                                line.append(currentLevel + 1)
                            else:
                                line.append(list2[i][j])
                        except IndexError:
                            line.append(list2[i][j])
                    list1.append(line)
                    line = []
            step = "list1"
        iter += 1
        
    printmap(list1)
    answer = getmax(list1)
    return answer

def printmap(list):
    line= ""
    for i in list:
        for j in i:
            if j == 0:
                line += " "
            else:
                line += str(j)
        print(line)
        line = ""

def getmax(list):
    maxList = []
    for i in list:
        maxList.append(max(i))
    answer = max(maxList)
    return answer
