def alphabet_position(text):
    x = "".join(text).lower().strip(".").replace(" ","")
    y = ""
    for i in x:
        if ord(i)-96 <= 0:
            continue
        else:
            y += str(ord(i)-96)+ " "
    return y.rstrip()
