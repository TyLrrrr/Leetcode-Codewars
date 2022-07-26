#codewars Challenge, implement memoization into a function that gives you fibonacci

#create a dictionary to store our values
fac_dic = {}

def fibonacci(n):
    if n in [0, 1]: # could do if n < 2: retrun 1
        return n
    # just keeps adding values to the dictionary
    if n not in fac_dic:
        fac_dic[n] = fibonacci(n-1) + fibonacci(n-2)
    #returns the value of the key n
    return fac_dic[n]

# had to learn about memoization 
# https://towardsdatascience.com/mastering-memoization-in-python-dcdd8b435189
