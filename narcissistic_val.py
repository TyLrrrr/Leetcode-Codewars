# codewar challenge: Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.

def narcissistic( value ):
    x = len(str(value))
    y = 0
    z = str(value)
    for i in z:
        y += int(i)**x
    if y == value:
        return True
    else:
        return False
