# Codewars Challenge: write a function that takes an integer as input, 
# and returns the number of bits that are equal to one in the binary representation of that number. 
def count_bits(n):
    import math as m
    x = int(n)
    base2 = []
    while x > 0:
        y = x % 2
        y = int(y)
        if y > 0:
            z = 1
        else:
            z = 0
        x /= 2
        x = m.trunc(x)
        base2.append(z)
    base2 = base2[::-1]
    count = 0
    for i in base2:
           if i == 1:
                count += 1
    return count
