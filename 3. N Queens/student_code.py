
QUEENS = 10

# def is_queen(board, y, x):
# 	found_queen = False
# 	if board[y][x] == 1:
# 		found_queen = True
    
# 	return found_queen


# def check_row(board, y):
# 	row_equal = False

# 	for i in range(0, QUEENS):
# 		# print("check i", i)
# 		for j in range(1, QUEENS):
# 			# print("check j", j)
# 			if board[y][i] == 1 and board[y][j] == 1:
# 				row_equal = True
# 				# print("reached")
# 				break
# 		break
    
# 	return row_equal 
    

def find_queen(old_board, x):
    #check specific column for a queen
    for a in range(QUEENS):
        if(old_board[a][x] == 1):
            break
    return a


def copy_fn(board):

    temp_board = [ [0]*QUEENS for i in range(QUEENS)]

    for i in range(QUEENS):
        for j in range(QUEENS):
            temp_board[i][j] = board[i][j]
    
    return temp_board


def calc_attacks_row(y, board):
    num_attacks = 0
    for i in range(0, QUEENS):
        for j in range(i+1, QUEENS):
            # print("check j", j)
            if board[y][i] == 1 and board[y][j] == 1:
                num_attacks += 1
                # print("reached")
    return num_attacks


def attacks(board):
    forward_diagonal = []
    reverse_diagonal = []
    num_attacks = 0
    a = 0
    b = 0
    c = 0
    d = 0
    #calculate num of attacks for rows
    for y in range(0, QUEENS):
        for i in range(0, QUEENS):
            for j in range(i+1, QUEENS):
                # print("check j", j)
                if board[y][i] == 1 and board[y][j] == 1:
                    num_attacks += 1


    for y in range(0, QUEENS):
        for x in range(0, QUEENS):
            if(board[y][x] == 1):
                
                # b = x
                for i in range(1, QUEENS):
                    if(y+i < QUEENS and x+i < QUEENS and board[y+i][x+i] == 1):
                        num_attacks += 1
                    # if(x-i >= 0 and y+i < QUEENS and board[y+i][x-i] == 1 ):
                    #     num_attacks +=1
                    # if(x-i >= 0 and y-i < QUEENS and board[y-i][x-i] == 1):
                    #     num_attacks += 1
                    if(x+i < QUEENS and y-i >= 0 and board[y-i][x+i] == 1):
                        num_attacks += 1


                # for j in range()
            
            # if(a-b == c - d or a+b == c+d):
            #     print("here")
            #     num_attacks += 1
                

    return num_attacks

# def make_col_zero(board, i):
# 	for i in range(board)



def gradient_search(board):
    #put yor code here
    old_board = copy_fn(board)
    best_board = [ [0]*QUEENS for i in range(QUEENS)]


    attacks_old = 999
    # best_board_attacks = attacks(old_board)
    # old_board_attacks = 9999
    # i = 0
    while(attacks(best_board) < attacks_old):
        # i = i + 1
        # print("iterations", i)
        best_board = copy_fn(old_board)
        attacks_old  = attacks(best_board)

        for x in range(QUEENS):
            a = find_queen(old_board, x)
                
            
            #set column to zero
            for y in range(QUEENS):
                old_board[y][x] = 0

            for i in range(QUEENS):
                old_board[i][x] = 1
                new_board = copy_fn(old_board)
                old_board[i][x] = 0
                attacks_newboard  = attacks(new_board)
                # attacks_old  = attacks(best_board)
            
                if attacks(new_board) < attacks(best_board):
                    best_board = copy_fn(new_board)
                        # prev_attacks = attacks(old_board)
                        # best_board_attacks = attacks(new_board)
            old_board[a][x] = 1

                    
            #set queen pos to 1 again
            # old_board[i][a] = 1
        
        old_board = copy_fn(best_board)
        # old_board[i][a] = 1

        

    for i in range(QUEENS):
        for j in range(QUEENS):
            board[i][j] = best_board[i][j]

    # print("board", board)
    # print(attacks(board))
    if(attacks(board) == 0):
        return True
    else:
        return False
    # num = attacks(board)
    # print("attacks", num)


   

    

    



    



