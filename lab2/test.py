


QUEENS = 10





# for i in range(len(data1)):
#     for j in range(len(data1)):
#         print(data1[i][j])
# def check_row(board, y):
#     row_equal = False

#     for i in range(0, QUEENS):
#         for j in range(1, QUEENS):
#             if board[y][i] == 1 and board[y][j] == 1:
#                 row_equal = True
#                 break
#         break
    
#     return row_equal 




# # def gradient_search(board):
# #     #put yor code here

# #     #current state
# #     # old_board = board
    
# #     # while(attacks reduces):
# #     # 	best_board = old_board

# #     # 	for y in range(QUEENS):
# #     # 		for r in range(QUEENS):
# #     # 			# new_board = 
# #     # 			if (attacks(new_board) < attacks(best_board)):
# #     # 				best_board = new_board
                
# #     # 	old_board = best_board
# #     # board = best_board
    
# #         queen_in_row = check_row(board, 1)

# #         if(queen_in_row == True):
# #             print("true")

# #         return queen_in_row
    



# # gradient_result = gradient_search(data1)

# # print(gradient_result)


# check_row(data1, 1)




QUEENS = 10
forward_diagonal = []

board = [ [0]*10 for i in range(10)]

print(board)




for y in range(0, QUEENS):
    for x in range(0, QUEENS):
        if y+1 < QUEENS and x+1 < QUEENS:
            forward_diagonal.append(board[y][x])
            forward_diagonal.append(board[y+1][x+1])
            print("forward diagonal",len(forward_diagonal))



