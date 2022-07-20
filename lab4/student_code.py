import common







def value_fn(board, turn):
    
    
        
    board_status = common.game_status(board)

    if(board_status == common.constants.X):
        return 1
    
    #O wins
    if(board_status == common.constants.O):
        return -1
    
    #tie
    if(board_status == common.constants.NONE):
       l = 0
       for y in range(3):
           for x in range(3):
               if common.get_cell(board, y, x) == 1 or common.get_cell(board, y, x) == 2:
                   l = l + 1
                   if(l == 9):
                       return common.constants.NONE


    
    if(turn == common.constants.X):
        v_max = -100000000

        for y in range(3):
            for x in range(3):
                if(common.get_cell(board, y, x) == 0):
                    common.set_cell(board, y, x, 1)
                    value_1 = value_fn(board, common.constants.O)
                    if value_1 > v_max:
                        v_max = value_1
                    common.set_cell(board, y, x, 0)
                    
        return v_max
    
    if(turn == common.constants.O):
        v_min = 100000000

        for y in range(3):
            for x in range(3):
                if(common.get_cell(board, y, x) == 0):
                    common.set_cell(board, y, x, 2)
                    value_2 = value_fn(board, common.constants.X)
                    if value_2 < v_min:
                        v_min = value_2
                    common.set_cell(board, y, x, 0)

        
        return v_min




def pruning_fn(board, turn, alpha, beta):

    board_status = common.game_status(board)

    if(board_status == common.constants.X):
        return 1
    
    #O wins
    if(board_status == common.constants.O):
        return -1
    
    #tie
    if(board_status == common.constants.NONE):
       l = 0
       for y in range(3):
           for x in range(3):
               if common.get_cell(board, y, x) == 1 or common.get_cell(board, y, x) == 2:
                   l = l + 1
                   if(l == 9):
                       return common.constants.NONE


    
    if(turn == common.constants.X):
        v_max = -100000000

        for y in range(3):
            for x in range(3):
                if(common.get_cell(board, y, x) == 0):
                    common.set_cell(board, y, x, 1)
                    value_1 = pruning_fn(board, common.constants.O, alpha, beta)
                    # print("value 1", value_1)
                    # print("vmax", v_max)
                    if value_1 > v_max:
                        v_max = value_1
                    common.set_cell(board, y, x, 0)
                    if v_max >= beta:
                        return v_max
                    if v_max > alpha:
                        alpha = v_max

                    
        return v_max
    
    if(turn == common.constants.O):
        v_min = 100000000

        for y in range(3):
            for x in range(3):
                if(common.get_cell(board, y, x) == 0):
                    common.set_cell(board, y, x, 2)
                    value_2 = pruning_fn(board, common.constants.X, alpha, beta)
                    if value_2 < v_min:
                        v_min = value_2
                    common.set_cell(board, y, x, 0)
                    if v_min <= alpha:
                        return v_min
                    if v_min < beta:
                        beta = v_min

        
        return v_min















def minmax_tictactoe(board, turn):
    #put your code here:
    #it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    #use the function common.game_status(board), to evaluate a board
    #it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
    #the program will keep track of the number of boards evaluated
    #result = common.game_status(board);

    result = value_fn(board, turn)

    if(result == 1):
        return common.constants.X
    
    if(result == -1):
        return common.constants.O
    
    if(result == common.constants.NONE):
        return common.constants.NONE

    # return common.constants.NONE


def abprun_tictactoe(board, turn):
    #put your code here:
    #it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    #use the function common.game_status(board), to evaluate a board
    #it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
    #the program will keep track of the number of boards evaluated
    #result = common.game_status(board);

    alpha = -5
    beta = 5

    result = pruning_fn(board, turn, alpha, beta)

    if(result == 1):
        return common.constants.X
    
    if(result == -1):
        return common.constants.O
    
    if(result == common.constants.NONE):
        return common.constants.NONE

    # return common.constants.NONE
