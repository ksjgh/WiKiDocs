# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

# sensor_right = 0.7
# pHit = sensor_right
# pMiss = 1-pHit
#
# p_move = 0.8
# pExact = p_move
# pUndershoot = 1 - pExact
# pOvershoot = 0

def sense_1D(p_1D, Z ,sensor_right , world_1D):

    pHit = sensor_right
    pMiss = 1.0 - pHit
    q=[]
    p = p_1D
    world = world_1D

    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1.0-hit) * pMiss))

    return q

    ## for just 1D case , enable this case
    ## for more than 2D case disable this case, below code causes LOCAL NORMALIZE problem
    # if s == 0 :
    #     return q
    # else :
    #     for i in range(len(q)) : q[i] = q[i] / s
    #     return q


def sense_2D(p_2D, Z ,sensor_right , world_2D):

    q=[]
    s=0.0
    for i in range(len(p_2D)):
        q.append(sense_1D(p_2D[i], Z ,sensor_right , world_2D[i]))
        s = s + sum(q[i])

    if s==0.0 :
        print('Probability Distribution is 0\n')
        print('Check, Motions and measurements Vectors\n')

    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = q[i][j] / s
    return q

def move_1D(p_1D, U ,pExact):
    q = []
    p = p_1D
    pStay = 1.0 - pExact
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pStay * p[(i) % len(p)]
        q.append(s)
    return q


def move_2D(p_2D, motion ,pExact):
    q = []
    stay , right , left, down, up = [0,0] , [0,1] ,[0,-1], [1,0] ,[-1,0]

    if  motion == stay :
        return p_2D
    elif motion == right :
        for i in range(len(p_2D)) :
            q.append(move_1D(p_2D[i], 1 ,pExact))
    elif motion == left :
        for i in range(len(p_2D)) :
            q.append(move_1D(p_2D[i], -1 ,pExact))
    elif motion == down :
        q = [ [] for row in range(len(p_2D))]
        for i in range(len(p_2D[0])) :
            p_1D = [ row[i] for row in p_2D ]
            q_column = move_1D(p_1D, 1 ,pExact)
            for j in range(len(q_column)) :
                q[j].append(q_column[j])
    elif motion == up :
        q = [ [] for row in range(len(p_2D))]
        for i in range(len(p_2D[0])) :
            p_1D = [ row[i] for row in p_2D ]
            q_column = move_1D(p_1D, -1 ,pExact)
            for j in range(len(q_column)) :
                q[j].append(q_column[j])

    ### Normalize q
    s = 0.0
    for i in range(len(p_2D)):
        s = s + sum(q[i])

    if s==0.0 :
        print('Probability Distribution is 0\n')
        print('Check, Motions and measurements Vectors\n')

    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = q[i][j] / s

    return q



#### from here
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

    # >>> Insert your code here <<<

    ### Loop until end of motions
    for i in range(len(motions)) :
        ### moves and update p
        p = move_2D(p, motions[i], pExact=p_move)

        ### check 'measurements' and update p
        p = sense_2D(p, measurements[i] ,sensor_right , colors)

    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print ('[' + ',\n '.join(rows) + ']')

#############################################################
# For the following test case, your output should be
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

# ### Main Test
colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
# ### Main Test, Fail
#
# colors = [['R', 'G'],
#           ['R', 'R'],
#           ['G', 'R'],
#           ['R', 'G'],
#           ['G', 'G']]
#
#
#
# motions = [[0, 0], [-1, 0],[0, 1],[-1, 0],[0,1],[1,0]]
# measurements = ['R','R','G','G','G','R']
#
# sensor_right = 1.0
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right, p_move)

# ### test 1
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'G'],
#           ['G', 'G', 'G']]
# measurements = ['G']
# motions = [[0,0]]
# sensor_right = 1.0
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# ### test 1 end

# test 2
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R']
# motions = [[0,0]]
# sensor_right = 1.0
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# ### test 2 end

# test 3
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R']
# motions = [[0,0]]
# sensor_right = 0.8
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# ### test 3 end

# test 4
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R', 'R']
# motions = [[0,0], [0,1]]
# sensor_right = 0.8
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# # ### test 4 end

# test 5
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R', 'R']
# motions = [[0,0], [0,1]]
# sensor_right = 1.0
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
### test 5 end

### test 6
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R', 'R']
# motions = [[0,0], [0,1]]
# sensor_right = 0.8
# p_move = 0.5
# p = localize(colors,measurements,motions,sensor_right,p_move)
# ### test 6 end

# test 7
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R', 'R']
# motions = [[0,0], [0,1]]
# sensor_right = 1.0
# p_move = 0.5
# p = localize(colors,measurements,motions,sensor_right,p_move)
### test 7 end

show(p) # displays your answer
