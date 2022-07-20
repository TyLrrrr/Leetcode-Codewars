# Codewars Challenge:Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
# If it is the case we will return k, if not return -1.
def dig_pow(n, p): 
    x = 0
    for i in str(n):
        x += int(i)**p
        p +=1
    if x%n == 0:
        y = x/n
        return y
    else:
        return -1
