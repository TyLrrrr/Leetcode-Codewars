# Codewars Challenge:Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

def snail(snail_map):
    list = []
    direction = "right"
    n = len(snail_map) * len(snail_map)
    z = len(snail_map)
    x, y = 0, 0
    i, j = 1, 0

    if snail_map[0] == []:
        return list

    list.append(snail_map[0][0])
    
    while len(list) != n:
        if direction == "right":
            if i == z:
                direction = "down"
                i = 1
                z = z - j
                continue
            i += 1
            y += 1
            list.append(snail_map[x][y])


        if direction == "down":
            if i == z:
                direction = "left"
                i = 1
                continue
            i += 1
            x += 1
            list.append(snail_map[x][y])

        if direction == "left":
            if i == z:
                j = 1
                direction = "up"
                z = z - j
                i = 1
                continue 
            i += 1
            y -= 1
            list.append(snail_map[x][y])

        if direction == "up":
            if i == z:
                direction = "right"
                i = 1
                continue
            i += 1
            x -= 1
            list.append(snail_map[x][y])

    return list
