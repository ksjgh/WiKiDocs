# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def find_next_point(init,grid_state) :
    ###print('\n\n----- funtion find_next_gen')
    obstacle = 1
    navigable_space = 0
    closed_space = -1
    occupied_space = 2

    available_position = []
    x1 , y1 = init[0] , init[1]
    ###print('pop = g , y, x = %s, %s, %s' % (g_val , y, x))
    for [dx,dy] in delta :
        y2 , x2 =  y1 + dy , x1 + dx
        ###print('ny, nx = %s, %s     ' % (ny, nx), end ='')
        if x2>=0 and x2<=len(grid_state)-1 and y2>=0 and y2<=len(grid_state[0])-1:
            ###print('search point is INSIDE',end='     ')
            if grid_state[x2][y2] == navigable_space :
                available_position.append([x2,y2])
                grid_state[x2][y2] = occupied_space
                ###print('ADDED in next_gen ,', end='')
                ###print('available_position =',end=' ' )
                ###print(available_position)
            ###else :
                ###print('NO navigable_space')
        ###else :
                ###print('search point is OUTSIDE')
    grid_state[x][y] = closed_space

    ###print('next_gen = ',end='')
    ###print(next_gen)
    return available_position , grid_state


# def find_path(grid,init1,goal,g1):
#
#     if ### first call
#         path = [[init[0],init[1]]]
#         import copy
#         grid_state = copy.deepcopy(grid)
#
#     for init2 in find_next_point(init1,grid_state):
#         if g1 == 0 :
#             if init2 == goal :
#                 ###
#                 return path.append(init2)
#             else :
#                 ### go to mother tree and find other point
#                 find_path(grid,init2,goal,g2)
#         else :
#             g2 = g1 - 1
#             path.append[init2]
#             return path.append(find_path(grid,init2,goal,g2))

def find_path(grid,init1,goal,g1):

    global recursive_count
    recursive_count += 1
    obstacle = 1
    navigable_space = 0
    closed_space = -1
    occupied_space = 2

    if recursive_count == 1 :
        path = [[init[0],init[1]]]
        import copy
        grid_state = copy.deepcopy(grid)

    if g1 == 0 :
        if init1 == goal :
            return path.extend(init1)
        else :
            ### go to mother tree and find other point
            init0 = path.pop()
            find_path(grid,init0,goal,g1-1)
    else :
        g2 = g1 - 1
        path.append[init1]
        grid_state[init[0]][init[1]] = closed_space
        for init2 in find_next_point(init1,grid_state):
            return path.extend(find_path(grid,init2,goal,g2))


def show_path(path,row,col):
    expand = [[' ' for col in range(col)] for row in range(row)]

    p1 = path[0]
    for p2 in path[1:] :
        d = p2 - p1

        if d == delta[0] : expand[p1[1]][p1[2]] = delta_name[0]
        if d == delta[1] : expand[p1[1]][p1[2]] = delta_name[1]
        if d == delta[2] : expand[p1[1]][p1[2]] = delta_name[2]
        if d == delta[3] : expand[p1[1]][p1[2]] = delta_name[3]

        p2=p1

    return expand

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1


    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1


    path = []
	path.extend(find_path(grid,init,goal,g))
    expand = show_path(path,len(grid),len(grid[0]))

    return expand # make sure you return the shortest path

print(search(grid,init,goal,cost)
