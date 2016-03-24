import numpy as np

# def MakeSpiralArray(array_size):
#     N=array_size
#
#     return sa


def print_array(array,array_size):
    ar=array
    N=array_size
    for i in range(N):
        for j in range(N):
             print("%3d" % ar[i][j],end="")
        print("")
    #           print(column, end="")
    # print(end="\n")

    # for i in range(N):print(ar[i,:])
            # print('{0}'.format(ar[i,j])+' '*sp)
        #print('\n')

N=6
sa=np.zeros((N,N),dtype=int)
# sa=MakeSpiralArray(N)
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
