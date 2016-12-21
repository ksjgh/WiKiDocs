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
        [1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
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
    grid_state[x1][y1] = closed_space

    ###print('next_gen = ',end='')
    ###print(next_gen)
    return available_position , grid_state


def find_path(init,goal,grid,directions):
    print('--------- Func find_path')
    import copy
    grid_state = copy.deepcopy(grid)

    path = [[init[0],init[1]]]
    p1 = init
    for d in directions :
        print('p1 = ',end='')
        print(p1)

        print('d = ',end='')
        print(d)

        p2 = [0,0]
        p2[0] = p1[0] +  delta[d][0]
        p2[1] = p1[1] +  delta[d][1]

        print('p2 = ',end='')
        print(p2)

        available_position , grid_state = find_next_point(p1,grid_state)

        print('available_position = ',end='')
        print(available_position)

        if p2 in available_position :
            path.append(p2)
            p1 = p2
            print('path = ',end='')
            print(path)
        else :
            break

    return path

def show_path(path,grid):
    row , col = len(grid) , len(grid[0])
    import copy
    expand = copy.deepcopy(grid)

    for row in range(len(expand)):
        for col in range(len(expand[0])):
            expand[row][col] = ' '

    p1 = path[0]
    for p2 in path[1:] :
        d = [0,0]
        d[0] = p2[0] - p1[0]
        d[1] = p2[1] - p1[1]

        if d == delta[0] : expand[p1[0]][p1[1]] = delta_name[0]
        if d == delta[1] : expand[p1[0]][p1[1]] = delta_name[1]
        if d == delta[2] : expand[p1[0]][p1[1]] = delta_name[2]
        if d == delta[3] : expand[p1[0]][p1[1]] = delta_name[3]

        p1=p2

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


    print('g-value = %s' % g )
    import itertools as it

    for j in it.product((3,1,2,0),repeat = g):
        print('directions = ' , j)
        directions = list(j)
        path = find_path(init,goal,grid,directions)
        print('Path = ' , path)
        if len(path) == g+1 :
            if path[-1] == goal :
                break

    # ### test
    # directions = list((3, 2, 3, 3, 3, 3, 2, 2, 2))
    # path = find_path(init,goal,grid,directions)
    # print('-------- Solution Path = ' , path)
    # ### test


    expand = show_path(path,grid)
    expand[goal[0]][goal[1]] = '*'
    return expand # make sure you return the shortest path

for row in search(grid,init,goal,cost) :
    print(row)
