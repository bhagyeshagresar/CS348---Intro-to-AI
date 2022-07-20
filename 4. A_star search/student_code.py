

import common

def get_x_y_start(map):
    x_y_list = []
    found_2 = False
    for y in range(0, common.constants.MAP_HEIGHT):
        for x in range(0, common.constants.MAP_WIDTH):
            # print(map[y][x])
            if(map[y][x] == 2):
                found_2 = True
                break
        if(found_2 == True):
            break
    x_y_list.append(y)
    x_y_list.append(x)
    return x_y_list


def get_x_y_end(map):
    x_y_list = []
    found_2 = False
    for y in range(0, common.constants.MAP_HEIGHT):
        for x in range(0, common.constants.MAP_WIDTH):
            # print(map[y][x])
            if(map[y][x] == 3):
                found_2 = True
                break
        if(found_2 == True):
            break
    x_y_list.append(y)
    x_y_list.append(x)
    return x_y_list




def expand(current_y_x, map, open_list, parent_list, g_list):
    y = current_y_x[0] 
    x = current_y_x[1]
    
    
    if(y-1 >= 0 and map[y-1][x] != 4 and map[y-1][x] != 1):
        parent_list[y-1][x] = [y, x]
        open_list.append([y-1, x]) #stack of [4, 3, 2, 1]
        g_list[y-1][x] = g_list[y][x] + 1
    
    if(x-1 >= 0 and map[y][x-1] != 4 and map[y][x-1] != 1):
        parent_list[y][x-1] = [y, x]
        open_list.append([y, x-1])
        g_list[y][x-1] = g_list[y][x] + 1


    if(y+1 < common.constants.MAP_HEIGHT and map[y+1][x] != 4 and map[y+1][x] != 1):
        parent_list[y+1][x] = [y, x]
        open_list.append([y+1, x])
        g_list[y+1][x] = g_list[y][x] + 1




    if(x+1 < common.constants.MAP_WIDTH and map[y][x+1] != 4 and map[y][x+1] != 1):
        parent_list[y][x+1] = [y, x]
        open_list.append([y, x+1])
        g_list[y][x+1] = g_list[y][x] + 1



    return open_list





def calculate_h(current_y_x, end_y_x):

    h = abs(current_y_x[1] - end_y_x[1]) + abs(current_y_x[0] - end_y_x[0])

    return h



def calculate_f(y, x, g_list, h_list, end_y_x):
    current_y_x = [0, 0]
    current_y_x[0] = y 
    current_y_x[1] = x

    h_list[y][x] = calculate_h(current_y_x, end_y_x)
    
    f = g_list[y][x] + h_list[y][x]

    return f



# def lowest_f(g_list, h_list, f_list, end_y_x):
    
# 	for y in range(common.constants.MAP_HEIGHT):
# 		for x in range(common.constants.MAP_WIDTH):
# 			f_list[y][x] = calculate_f(y, x, g_list, h_list, end_y_x)

# 	lowest_f_value = min([min(x) for x in f_list])

# 	for a in range(common.constants.MAP_HEIGHT):
# 		for b in range(common.constants.MAP_WIDTH):
# 			if(f_list[a][b] == lowest_f_value):
# 				break
# 	return [a, b], 


def lowest_f(open_list, map, g_list, h_list, end_y_x):

    #function to get the index with lowest f value
    min_f_value = 100000
    
    for idx, z in enumerate(open_list):
        y = z[0]
        x = z[1]

        f = calculate_f(y, x, g_list, h_list, end_y_x)
        if f < min_f_value:
            min_f_value = f
            lowest_index = idx
            a = y 
            b = x 
    # print("lowest index in function", lowest_index)
    return lowest_index







def astar_search(map):
    found = False
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1
    open_list = []
    # close_list = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
    g_list = [[1000 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
    h_list = [[1000 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]

    start_y_x = get_x_y_start(map)
    end_y_x = get_x_y_end(map)
    parent_list = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]

    g_list[start_y_x[0]][start_y_x[1]] = 0
    h_list[start_y_x[0]][start_y_x[1]] = calculate_h(start_y_x, end_y_x)
    open_list.append(start_y_x)

    while len(open_list) != 0:
        
        lowest_index = lowest_f(open_list, map, g_list, h_list, end_y_x) #coordinates of node having lowest f value
        # print("lowest index", lowest_index)
        
        current = open_list.pop(lowest_index)

        if(map[current[0]][current[1]] == 3):
            print("goal reached")
            found = True
            map[current[0]][current[1]] = 5 #represent it as goal state
            
            break
        
      
        else:
            map[current[0]][current[1]] = 4 #modify value to 4

        
        open_list = expand(current, map, open_list, parent_list, g_list)
    

    if found == True:
        y = current[0]
        x = current[1]

        while(parent_list[y][x] != 0):
            tuple_y_x = parent_list[y][x]

            map[tuple_y_x[0]][tuple_y_x[1]] = 5 # parent node coordinates

            y = tuple_y_x[0] #
            x = tuple_y_x[1]

        
        y = start_y_x[0]
        x = start_y_x[1]
        map[y][x] = 5
        
             




    return found
