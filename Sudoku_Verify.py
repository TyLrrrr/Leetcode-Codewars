# Codewars Challenge: verify sudoku answer is correct with a 9x9 board
def valid_solution(board):
    test_list = []
    check_list = [1,2,3,4,5,6,7,8,9]
    ################### Test Rows #################
    for i in board:
        for j in i:
            test_list.append(j)
        test_list.sort()    
        if test_list != check_list:
            return False
        test_list = []
    ################### Test Columns ##############
    x = 0
    while x < 9:
        for i in board:
            test_list.append(i[x])
        test_list.sort()
        if test_list != check_list:
            return False
        test_list = []
        x += 1
    ################## Move and Call Quadrant ############
    step = 0
    iter = 0
    startx = 0
    starty = 0
    while step < 3:
        while iter < 3:
            check = quadrant(startx,starty,board,test_list,check_list)
            if check == False:
                return False
            starty +=3
            iter += 1
            test_list =[]
        startx += 3
        step += 1
        starty = 0
        iter = 0
    return True
    ################### Test Quadrant ################
def quadrant(startx,starty,board,test_list,check_list):
    x, y, step, iter = startx, starty, 0, 0
    while step < 3:
        while iter < 3:
            test_list.append(board[x][y])
            y += 1
            iter += 1
        x += 1
        step += 1
        y = starty
        iter = 0
    test_list.sort()
    if test_list != check_list:
        return False
    return True
