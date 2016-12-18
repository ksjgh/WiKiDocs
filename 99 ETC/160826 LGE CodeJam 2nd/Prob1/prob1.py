import os
import sys
import math

PATH=os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)
input_filename = sys.argv[1]
ouput_filename = os.path.splitext(input_filename)[0] + '.out'

def calc_length(Ox,Oy,n) :
    """
    return minimum needed length
    Ox : Center x of circle
    Oy : Center y of circle
    n  : Right position of string
    """
    R , l1, l2, l3 = Oy, Ox, 0, (n-Ox)
    theta1 = 2 * math.atan(l1/R)
    theta3 = 2 * math.atan(l3/R)
    theta2 = 2 * math.pi - (theta1 + theta3)
    l2 = R * theta2
    total_length = l1 + l2 +l3

    min_length = math.ceil(total_length)
    return min_length

#######################  main #######################

# with open("test1.in", "r") as f:
with open(input_filename, "r") as f:
    T =  int((f.readline().split())[0]) # Total test cases
    # print("Test Cases = %d\n " % T)

    for t in range(T) :
        l = list(map(int,f.readline().split()))
        Ox , Oy , n = l[0], l[1], l[2]
        # print("\nOx , Oy, n = %s %s %s"  % (Ox , Oy, n) )
        min_length = calc_length(Ox,Oy,n)
        # print(min_length)
        # with open("test1.out", "a") as f1:
        with open(ouput_filename, "a") as f1:
            f1.write(str(min_length))
            f1.write("\n")
