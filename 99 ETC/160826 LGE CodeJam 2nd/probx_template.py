import os
import sys
import math

PATH=os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)
input_filename = sys.argv[1]
ouput_filename = os.path.splitext(input_filename)[0] + '.out'


## solution function of problem
def func :
    """

    """

    return pass

#######################  main #######################

with open("test5.in", "r") as f:  ## ON for test
# with open(input_filename, "r") as f: ## ON for final implelementation
    T =  int((f.readline().split())[0]) ## Total test cases
    # print("Test Cases = %d\n " % T)

    for t in range(T) :
        l = list(map(int,f.readline().split()))  ## read parameters
        Ox , Oy , n = l[0], l[1], l[2]           ## set parameters
        # print("\nOx , Oy, n = %s %s %s"  % (Ox , Oy, n) )  ## test code if parameters is read well
        min_length = calc_length(Ox,Oy,n)  ## get solutiion
        # print(min_length) ## ON for test
        # with open("test1.out", "a") as f1: ## ON for test

        ## ON for final implelementation
        with open(ouput_filename, "a") as f1:
            f1.write(str(min_length))
            f1.write("\n")
        ##############################################
