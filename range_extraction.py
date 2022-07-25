# Codewars Challenge: A format for expressing an ordered list of integers is to use a comma separated list of either individual integers or
#  or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes 
# all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

def solution(args):
    test = ""
    hold, sub = [], []
    x, min, max = 1, 0, 0

    for i in args: 
        # i equals the element of the current iteration so if i + 1 equals args[x] which would be the next element in the list
        # it will append into a sub list.
        if i+1 == args[x]:            
            sub.append(i)    
        else:
            # in order to grab that last number I test if there's a sub list and append the current iteration then place it in 
            # a holding list for later
            if len(sub) > 0:
                sub.append(i)
                hold.append(sub)
            else:
                hold.append(i)
            #clears the sub list for the next time it's needed
            sub = []
        # x value should be 1 ahead of the current iteration until the end to prevent a index error 
        if x >= len(args)-1:
            x = len(args)-1
        else:
            x += 1
    # take the hold list and manipulate it so it will return in the proper format
    for i in hold:
        # since the challenge only wants porions larger than 2 long to be formatted I threw it through this if statement
        # test if its a list and format properly
        if type(i) == list:
            if len(i) <= 2:
                min = i[0]
                max = i[1]
                test += str(min)+","+str(max)+","
            else:    
                min = i[0]
                max = i[-1]
                test += str(min) + "-" + str(max) + ","
        else: 
            test += str(i) +","
    #return the string with the last comma stripped
    return test.rstrip(",")
