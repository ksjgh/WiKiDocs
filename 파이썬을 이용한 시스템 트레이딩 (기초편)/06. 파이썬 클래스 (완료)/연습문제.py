class Point:

    def __init__(self, x, y):
        #super(Point, self).__init__()
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y=y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        newx=self.x+dx
        newy=self.y+dy
        return (newx,newy)


# Create instance
p1=Point(10,20)
# p2=Point(30,40)
# print("x={0} y={1}".format(p1.x,p1.y))

# setx , sety method
p1.setx(30)
p1.sety(40)
print("x={0} y={1}".format(p1.x,p1.y))

# get method
sp=p1.get()
print("x={0} y={1}".format(sp[0],sp[1]))

# move method
sp1=p1.move(1,2)
print("x={0} y={1}".format(sp1[0],sp1[1]))
