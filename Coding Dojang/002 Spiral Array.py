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


N=6
sa=np.zeros((N,N),dtype=int)
sa=MakeSpiralArray(N)
print_array(sa,N,2)
