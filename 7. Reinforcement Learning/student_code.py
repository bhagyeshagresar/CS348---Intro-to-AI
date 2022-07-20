import common





def get_x_y_start(map):
    x_y_list = []
    found_1 = False
    for y in range(0, 6):
        for x in range(0, 6):
            # print(map[y][x])
            if(map[y][x] == common.constants.PIZZA):
                found_1 = True
                break
        if(found_1 == True):
            break
    x_y_list.append(y)
    x_y_list.append(x)
    return x_y_list



def vmax_fn(v, values):
    for y in range(6):
        for x in range(6):
            if (v < values[y][x]):
                return False
    
    return True

    
def copy_fn(values):

    new_list = [[0 for i in range(6)] for j in range(6)]

    for i in range(6):
        for j in range(6):
            new_list[i][j] = values[i][j]
    
    return new_list


def next_state_fn(y, x, a):
    # next_state_list = []
    

    if((a == common.constants.SOFF or a == common.constants.SON)):
        
        

        next_state_list = []

        if(y+1 <=5):
            next_state_list.append([y+1, x])
        else:
             next_state_list.append([y, x])
        if(x-1 >= 0):
            next_state_list.append([y, x-1])
        else:
            next_state_list.append([y, x])
        
        if(x+1 <= 5):
            next_state_list.append([y, x+1])
        else:
            next_state_list.append([y, x])
  
  
     
    if((a == common.constants.WON or a == common.constants.WOFF)):


        next_state_list = []

        
        if(x-1 >= 0):
            next_state_list.append([y, x-1])
        else:
            next_state_list.append([y, x])
        
        if(y+1 <= 5):
            next_state_list.append([y+1, x])
        else:
            next_state_list.append([y, x])
        
        if(y-1 >= 0):
            next_state_list.append([y-1, x])
        else:
            next_state_list.append([y, x])

    
    if((a == common.constants.NOFF or a == common.constants.NON)):

        next_state_list = []

        
        if(y-1 >= 0):
            next_state_list.append([y-1, x])
        else:
            next_state_list.append([y, x])

        if(x-1 >= 0):
            next_state_list.append([y, x-1])
        else:
            next_state_list.append([y, x])

        if(x+1 <= 5):
            next_state_list.append([y, x+1])
        else:
            next_state_list.append([y, x])


   

    if((a == common.constants.EOFF or a == common.constants.EON)):


        next_state_list = []

         
        if(x+1 <= 5):
            next_state_list.append([y, x+1])
        else:
            next_state_list.append([y, x])

        if(y-1 >= 0):
            next_state_list.append([y-1, x])
        else:
            next_state_list.append([y, x])

        if(y+1 <= 5):
            next_state_list.append([y+1, x])
        else:
            next_state_list.append([y, x])
        

        
        
    return next_state_list



def reward_fn(y, x, a, discount, values, battery_drop_cost):
    value_next = 0
    reward = 0

    if(a == common.constants.SOFF or a == common.constants.NOFF or a == common.constants.WOFF or a == common.constants.EOFF):
        reward = -battery_drop_cost
        # next_states_list1 = []
        next_states_list1 = next_state_fn(y, x, a)
        value_next += (0.7)*(reward + (discount*values[next_states_list1[0][0]][next_states_list1[0][1]])) #[[]
        value_next += (0.15)*(reward + (discount*values[next_states_list1[1][0]][next_states_list1[1][1]]))
        value_next += (0.15)*(reward + (discount*values[next_states_list1[2][0]][next_states_list1[2][1]]))

   
   
    else:
        reward = -2*battery_drop_cost
        next_states_list2 = []
        next_states_list2 = next_state_fn(y, x, a)
        value_next += (0.8)*(reward + (discount*values[next_states_list2[0][0]][next_states_list2[0][1]]))
        value_next += (0.1)*(reward + (discount*values[next_states_list2[1][0]][next_states_list2[1][1]]))
        value_next += (0.1)*(reward + (discount*values[next_states_list2[2][0]][next_states_list2[2][1]]))



    return value_next

    




def drone_flight_planner(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # access the policies using "policies[y][x]"
    # access the values using "values[y][x]"
    # y between 0 and 5
    # x between 0 and 5
    # function must return the value of the cell corresponding to the starting position of the drone
    
   

    action_list = [common.constants.SOFF, common.constants.WOFF, common.constants.NOFF, common.constants.EOFF,
                    common.constants.SON, common.constants.WON, common.constants.NON, common.constants.EON]

    new_values = [[0 for i in range(6)] for j in range(6)]
    converge = False

    # print(values)

    while (converge == False):
        for y in range(6):
            for x in range(6):
                v_max = -10000000
                if(map[y][x] == common.constants.CUSTOMER):
                    new_values[y][x] = delivery_fee
                    policies[y][x] = common.constants.EXIT
                elif(map[y][x] == common.constants.RIVAL):
                    new_values[y][x] = -dronerepair_cost
                    policies[y][x] = common.constants.EXIT
                else:
                    for a in range(8):
                        value = reward_fn(y, x, action_list[a], discount, values, battery_drop_cost)
                        if value>v_max:
                            new_values[y][x] = value
                            policies[y][x] = action_list[a]
                            v_max = value
        counter = 0
        for y in range(6):
            for x in range(6):
                if(abs(values[y][x] - new_values[y][x])) < 0.001:
                    counter += 1
        
        if counter == 36:
            converge = True
        
        for i in range(6):
            for j in range(6):
                values[i][j] = new_values[i][j]


            
    x_y_list = []
    x_y_list = get_x_y_start(map)

    












    
    return values[x_y_list[0]][x_y_list[1]]
