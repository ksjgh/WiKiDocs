import numpy as np

class point_2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def Change_Direction(direction):
    if direction=='right' :
        direction='down'
        return direction
    if direction=='left' :
        direction='up'
        return direction
    if direction=='up' :
        direction='right'
        return direction
    if direction=='down' :
        direction='left'
        return direction

def Find_Next(sa,direction,current_position,array_size):

    limit=array_size
    next_position=point_2D(0,0)
    next_position.x=current_position.x
    next_position.y=current_position.y

    if direction=='right' and (current_position.y+1)<limit and sa[current_position.x,current_position.y+1]==-1:
        next_position.y=current_position.y+1
        return (next_position,direction)
    if direction=='left' and (current_position.y-1)>-1 and sa[current_position.x,current_position.y-1]==-1:
        next_position.y=current_position.y-1
        return (next_position,direction)
    if direction=='up' and (current_position.x-1)>-1 and sa[current_position.x-1,current_position.y]==-1 :
        next_position.x=current_position.x-1
        return (next_position,direction)
    if direction=='down' and (current_position.x+1)<limit and sa[current_position.x+1,current_position.y]==-1 :
        next_position.x=current_position.x+1
        return (next_position,direction)

    direction=Change_Direction(direction)
    next_position=Find_Next(sa,direction,current_position,limit)
    return next_position


def Write_Array(sa,next_position,i) :
    sa[next_position.x,next_position.y]=i

def MakeSpiralArray(array,array_size):
    sa=array
    N=array_size

    direction="right"
    current_position=point_2D(0,0)
    next_position=point_2D(0,0)
    Write_Array(sa,current_position,0)
    for i in range(1,N**2) :
        current_position,direction=Find_Next(sa,direction,current_position,N)
        Write_Array(sa,current_position,i)
        # if i<N**2-1:


def print_array(array,array_size):
    ar=array
    N=array_size
    for i in range(N):
        for j in range(N):
             print("%3d" % ar[i,j],end="")
        print("")

#### main ####
N=6
sa=np.full((N,N),-1,dtype=int)
MakeSpiralArray(sa,N)
print_array(sa,N)


# X,Y = map(int,raw_input().split(' '))
# lis = [[-1 for i in xrange(Y)] for j in xrange(X)]
# x,y = 0,0
# dx,dy = 0,1
# count = 0
# while lis[x][y] == -1:
#     lis[x][y] = count
#     count+=1
#     x,y = x+dx,y+dy
#     if x in [-1,X] or y in [-1,Y] or lis[x][y] != -1:
#         x,y = x-dx,y-dy
#         dx,dy = dy,-dx
#         x,y = x+dx,y+dy
# for L in lis:
#     for val in L:
#         print ('%3d'%val)
#     print()
