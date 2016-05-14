s=0
for i in range(10,1001):
    m=1
    for j in str(i):
        m=m*int(j)
    s+=m

print("sum = %d" % s)
