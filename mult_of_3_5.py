# Codewars Challenge: Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
#Additionally, if the number is negative, return 0.
#Note: If the number is a multiple of both 3 and 5, only count it once.
def solution(number):
    x = 0
    for i in range(number):
        if i%3 == 0 and i%5 == 0:
            x+=i
        elif i%3 == 0:
            x+=i
        elif i%5 == 0:
            x+=i
    return x
