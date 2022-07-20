QUEENS = 10

# def is_queen(board, y, x):
# 	found_queen = False
# 	if board[y][x] == 1:
# 		found_queen = True
	
# 	return found_queen


def check_row(board, y):
	row_equal = False

	for i in range(0, QUEENS):
		for j in range(1, QUEENS):
			if board[y][i] == 1 and board[y][j] == 1:
				row_equal = True
				print("reached")
				break
		break
	
	return row_equal 
	





def attacks(board):
	num_attacks = 0

	for y in range(0, 25):
		#check rows
		# if check_row(board, y):
		# 	num_attacks += 1
		#check diagonal 1
		for x in range(0, 25):
			if y+1 < 20 and x+1 < 20 and board[y][x] == 1 and board[y+1][x+1] == 1:
				num_attacks += 1

	# for a in range(QUEENS, -1):
	# 	for b in range(QUEENS, -1):
	# 		if board[a][b] == 1 and board[a-1][b-1] and a < 15 and b < 15:
	# 			num_attacks += 1



	return num_attacks




def gradient_search(board):
	#put yor code here

	#current state
	# old_board = board
	
	# while(attacks reduces):
	# 	best_board = old_board

	# 	for y in range(QUEENS):
	# 		for r in range(QUEENS):
	# 			# new_board = 
	# 			if (attacks(new_board) < attacks(best_board)):
	# 				best_board = new_board
				
	# 	old_board = best_board
	# board = best_board
	
	attacks_num = attacks(board)

	
	return attacks_num
	

	



	



