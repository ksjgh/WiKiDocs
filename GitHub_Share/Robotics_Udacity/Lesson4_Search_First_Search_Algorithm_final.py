# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def find_next_gen(gen,grid_state) :
    ###print('\n\n----- funtion find_next_gen')
    obstacle = 1
    navigable_space = 0
    closed_space = -1
    occupied_space = 2

    next_gen = []

    for pop in gen :
        available_position = []
        g_val , y, x = pop[0] , pop[1][0] , pop[1][1]
        ###print('pop = g , y, x = %s, %s, %s' % (g_val , y, x))
        for [dy,dx] in delta :
            ny , nx =  y + dy , x + dx
            ###print('ny, nx = %s, %s     ' % (ny, nx), end ='')
            if ny>=0 and ny<=len(grid_state)-1 and nx>=0 and nx<=len(grid_state[0])-1:
                ###print('search point is INSIDE',end='     ')
                if grid_state[ny][nx] == navigable_space :
                    available_position.append([ny,nx])
                    grid_state[ny][nx] = occupied_space
                    ###print('ADDED in next_gen ,', end='')
                    ###print('available_position =',end=' ' )
                    ###print(available_position)
                ###else :
                    ###print('NO navigable_space')
            ###else :
                    ###print('search point is OUTSIDE')

        for p in available_position :
            next_gen.append([g_val+1,p])
        grid_state[y][x] = closed_space

    ###print('next_gen = ',end='')
    ###print(next_gen)
    return next_gen , grid_state

def is_goal_exist(gen,goal) :
    ###print('\n\n-----Func. is_goal_exist ')
    g_val = -1
    for p in gen :
        if p[1] == goal :
            g_val = p[0]  ##  g-value
            ###print('goal found , g_val = %s' % g_val)
            break
    if g_val >= 0 :
        return g_val
    else :
        ###print('goal does not exist ')
        return -1


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    import copy
    grid_state = copy.deepcopy(grid)

    gen = [[0,init]] ## [g-value,[ y, x]]
    path = 0
    g = 0

    while(True) :
        next_gen , next_grid_state = find_next_gen(gen,grid_state)

        if len(next_gen) == 0 :
            path = 'fail'
            break
        elif is_goal_exist(next_gen,goal) >=0 :
            ###print('Goal exist case')
            g = is_goal_exist(next_gen,goal)
            path = [g,goal[0],goal[1]]
            ###print('###print path = ', end='')
            ###print(path)
            break
        gen = next_gen
        grid_state = next_grid_state

    return path


result = search(grid,init,goal,cost)
###print('\n\n----- Final Result [g,y,x] = ',end='')
print(result)
