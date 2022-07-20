from numpy import append
import common
map = [[0, 3, 1],
        [8, 2, 5],
        [0, 7, 0]]


def get_x_y(map):
    x_y_list = []
    found_2 = False
    for y in range(0, 3):
        for x in range(0, 3):
            # print(map[y][x])
            if(map[y][x] == 2):
                found_2 = True
                break
        if(found_2 == True):
            break
    x_y_list.append(y)
    x_y_list.append(x)
    return x_y_list



def print_map(map):
    for y in range(3):
        for x in range(3):
            map[y][x]

    return map





def dfs(map):
    stack = []
    visited = [[0 for i in range(3)] for j in range(3)]
    i = 0
    pop_list = []
    
    list_y_x = get_x_y(map)
    y = list_y_x[0]
    x = list_y_x[1]
    print(list_y_x)

    
    stack.append(map[y][x])  #2
    found = False
    i = 0

    while(len(stack) != 0):
        #pop the element 
        map[y][x] = stack.pop() #1
        # i = i + 1
       
        print("map[y][x]", map[y][x])
        #process the element
        if(map[y][x] == 3):
            print("goal found")
            found = True
            break
        
        else:
            map[y][x] = 4
            # print(visited)
         
        
        if(y-1 < 3 and map[y-1][x] != 4):
            # print("found top of child")
            stack.append(map[y-1][x])
            print("stack 1", stack)
            

        if(x-1 < 3 and map[y][x-1] != 4):
            # print("found left child")
            stack.append(map[y][x-1])
            print("stack 2", stack)
            # print(map[y][x-1])
            #5

        if(y+1 < 3 and map[y+1][x] != 4):
            # print("found bottom child")
            stack.append(map[y+1][x])
            print("stack 3", stack)

        

        if(x+1 < 3 and map[y][x+1] != 4):
            # print("found right child")
            stack.append(map[y][x+1]) #stack = [3, 8, 7, 5]
            print("stack 4", stack)
        
        coord_list = [[y, x+1], [y+1, x], [y, x - 1], [y-1, x]]

        j = 0
        while()
        
        # for i in range(3):
        #     y = coord_list[i][i]
        #     x = coord_list[i][i+1]
        #     break
        
        # i = i + 1
        # if(i >= 3):
        #     i = 0
       
        if(i > 3):
            break

                
    return map


# print("test map", map)
map_2 = dfs(map)
                    
print(map_2)



