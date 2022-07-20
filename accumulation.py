#codewars Challenge:  The examples below show you how to write function accum:
#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"
#The parameter of accum is a string which includes only letters from a..z and A..Z.
def accum(s):
    # your code
    x = []
    for i in s:
        x.append(i.upper())
    z = []
    y = 1
    for i in x:
        q = i * y
        y += 1
        print(y," ", q)
        z.append(q.capitalize())
    w = ""
    for i in z:
        w += i + "-"
retrun w.rstrip("-")
