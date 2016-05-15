count={ x:0 for x in range(0,10) }

for x in range(1,1001):
    for i in str(x):
        count[int(i)]+=1

print(count)
