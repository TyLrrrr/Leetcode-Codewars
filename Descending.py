# Codewars Challenge: our task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
def descending_order(num):
    x=[]
    # Bust a move right here
    for i in str(num):
        x.append(int(i))
    x.sort()
    x = x[::-1]
    y = ""
    for i in range(len(x)):
        y += str(x[i])
    y = int(y)
    return y
