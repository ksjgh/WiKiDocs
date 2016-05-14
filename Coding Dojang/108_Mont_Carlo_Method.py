import random
import math

N=100000
N_in_C=0

for i in range(N):
    x=random.random()
    y=random.random()
    if (x**2+y**2)<1 : N_in_C+=1

Pi_cal=((N_in_C/N)*4)
error=(abs(Pi_cal-math.pi)/math.pi)*100
print("Pi is %f" % Pi_cal)
print("Error rate = %f%%" % error)
