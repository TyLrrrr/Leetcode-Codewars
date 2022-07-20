# Codewars Challenge:
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of 
# odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns 
# this "outlier" N.
def find_outlier(integers):
    y = 0
    for i in integers:
        if i%2 == 0:
            y+=1

    if y == 1:
        even = True
    else:
        even = False
    
    if even == True:
        for i in integers:
            if i%2 == 0:
                z = i
    else: 
        for i in integers:
            if i%2 != 0:
                z = i
    return z
