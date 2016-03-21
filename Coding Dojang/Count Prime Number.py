def IsPrimeNumber(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

counter=0
for n in range(2,1001):
    if IsPrimeNumber(n):counter+=1

print("Prime Number in 2-1000 = %d" % counter)
