# Codewar Challenge: In this kata you are required to, given a string, replace every letter with its position in the alphabet. a=1, b=2, etc...
#ignore non alpha chars
def alphabet_position(text):
    x = "".join(text).lower().strip(".").replace(" ","")
    y = ""
    for i in x:
        if ord(i)-96 <= 0:
            continue
        else:
            y += str(ord(i)-96)+ " "
    return y.rstrip()
