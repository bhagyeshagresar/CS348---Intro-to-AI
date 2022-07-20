import common

def get_x_y(map):
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


def expand_stack(current_y_x, map, stack, parent_list):
    y = current_y_x[0] 
    x = current_y_x[1]
    

    if(y-1 >= 0 and map[y-1][x] != 4 and map[y-1][x] != 1):
        # print("found top of child")
        stack.append([y-1, x]) # append coordinates of current_y_x[]
        parent_list[y-1][x] = [y, x]
    
    if(x-1 >= 0 and map[y][x-1] != 4 and map[y][x-1] != 1):
        # print("found left child")

        stack.append([y, x-1])
        parent_list[y][x-1] = [y, x]

    if(y+1 < common.constants.MAP_HEIGHT and map[y+1][x] != 4 and map[y+1][x] != 1):
        # print("found bottom child")
        stack.append([y+1, x])
        parent_list[y+1][x] = [y, x]



    if(x+1 < common.constants.MAP_WIDTH and map[y][x+1] != 4 and map[y][x+1] != 1):
        # print("found right child")
        stack.append([y, x+1]) #stack of [4, 3, 2, 1]
        parent_list[y][x+1] = [y, x]


    return stack




def expand_queue(current_y_x, map, queue, parent_list):
    y = current_y_x[0] 
    x = current_y_x[1]


    if(x+1 < common.constants.MAP_WIDTH and map[y][x+1] != 4 and map[y][x+1] != 1):
        # print("found right child")
        queue.append([y, x+1]) #stack of [4, 3, 2, 1]
        parent_list[y][x+1] = [y, x]
    
    if(y+1 < common.constants.MAP_HEIGHT and map[y+1][x] != 4 and map[y+1][x] != 1):
        # print("found bottom child")
        queue.append([y+1, x])
        parent_list[y+1][x] = [y, x]

    
    if(x-1 >= 0 and map[y][x-1] != 4 and map[y][x-1] != 1):
        # print("found left child")
        queue.append([y, x-1])
        parent_list[y][x-1] = [y, x]

    if(y-1 >= 0 and map[y-1][x] != 4 and map[y-1][x] != 1):
        # print("found top of child")
        queue.append([y-1, x]) # append coordinates of current_y_x[]
        parent_list[y-1][x] = [y, x]
    
 


    return queue




def df_search(map):
    found = False
    # PUT YOUR CODE HERE

    stack = []
    visited_list = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)] 
    parent_list = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
    # parent_list = []
    list_y_x = get_x_y(map) #start location
    

    stack.append(list_y_x)  # stack = [[1, 1]] (pos of value 2)

    i = 0

    while len(stack) != 0:

        i = i + 1

        current = stack.pop() #map element just removed
        
        if(map[current[0]][current[1]] == 3):
            print("goal reached")
            found = True
            map[current[0]][current[1]] = 5 #represent it as goal state

            break
        
      
        else:
            map[current[0]][current[1]] = 4 #modify value to 4


        
        stack = expand_stack(current, map, stack, parent_list)
       
    
    if found == True:
        y = current[0]
        x = current[1]

        while(parent_list[y][x] != 0):
            tuple_y_x = parent_list[y][x]

            map[tuple_y_x[0]][tuple_y_x[1]] = 5 # parent node coordinates

            y = tuple_y_x[0] #
            x = tuple_y_x[1]

        y = list_y_x[0]
        x = list_y_x[1]
        map[y][x] = 5
        
             


   




       
    return found


def bf_search(map):
    found = False;
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1

    queue = []
    # visited_list = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)] 
    parent_list = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
    # parent_list = []
    list_y_x = get_x_y(map) #start location
    

    queue.append(list_y_x)  # stack = [[1, 1]] (pos of value 2)

    i = 0

    while len(queue) != 0:

        i = i + 1

        current = queue.pop(0) #map element just removed
        
        if(map[current[0]][current[1]] == 3):
            print("goal reached")
            found = True
            map[current[0]][current[1]] = 5 #represent it as goal state

            break
        
      
        else:
            map[current[0]][current[1]] = 4 #modify value to 4


        
        queue = expand_queue(current, map, queue, parent_list)
       
    
    if found == True:
        y = current[0]
        x = current[1]

        while(parent_list[y][x] != 0):
            tuple_y_x = parent_list[y][x]

            map[tuple_y_x[0]][tuple_y_x[1]] = 5 # parent node coordinates

            y = tuple_y_x[0] #
            x = tuple_y_x[1]

        y = list_y_x[0]
        x = list_y_x[1]
        map[y][x] = 5
        
             





    return found





    