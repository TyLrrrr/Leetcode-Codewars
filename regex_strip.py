# codewars Challenge: Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
# Any whitespace at the end of the line should also be stripped out.

import re
def strip_comments(strng, markers):
    list = []
    answer = ""
    x = re.split("\n",strng)
    
    if len(markers) == 0:
        return strng
    
    reg_str="["
    for i in markers:
        reg_str += "\\" + i 
    reg_str += "]"

    for i in x:
        y = re.search(reg_str, i)
        if y != None:
            list.append(i[0:y.span()[0]:1])
        else:
            list.append(i) 

    for i in list:
        if i == '':
            answer += "\n"
        else:
            answer += i.rstrip() +"\n"

    z = re.search("(?s:.*)\\n\\n",answer)
    if z != None:
        answer = answer[0:-1:1]
        return answer
    else:
        return answer.rstrip()
