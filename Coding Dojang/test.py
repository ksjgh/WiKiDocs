# X,Y = map(int,raw_input().split(' '))
X,Y = map(int,6)
lis = [[-1 for i in xrange(Y)] for j in xrange(X)]
x,y = 0,0
dx,dy = 0,1
count = 0
while lis[x][y] == -1:
    lis[x][y] = count
    count+=1
    x,y = x+dx,y+dy
    if x in [-1,X] or y in [-1,Y] or lis[x][y] != -1:
        x,y = x-dx,y-dy
        dx,dy = dy,-dx
        x,y = x+dx,y+dy
for L in lis:
    for val in L:
        print ('%3d'%val)
    print()
