import matplotlib.pyplot as plt
class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def __sub__(self, other):
        return(Point(self.x-other.x, self.y-other.y))
    def __add__(self, other):
        return(Point(self.x+other.x, self.y+other.y))
    def __mul__(self, other):
        return Point(self.x*other, self.y*other)

    def __truediv__(self, num):
        return Point(self.x/num, self.y/num)

def new_point(point1, point2, num):
    new_point = point1+(point2 - point1)*num
    return new_point



num = 49/50
point_A = Point(-2, 0)
point_B = Point(-0,0.5)
point_C = Point(2, 0)


points_list = [point_A, point_B, point_C]
x_list=[]
y_list=[]
fig= plt.figure()
plt.axis([-2,2,0,1])
ax=plt.axes()
for t in range(100):
    print(point_A.x, point_B.x, point_C.x)
    print(point_A.y, point_B.y, point_C.y)
    for i in points_list:
        x_list.append(i.x)
        y_list.append(i.y)
    x_list.append(x_list[0])
    y_list.append(y_list[0])
    ax.plot(x_list,y_list)
    point_A, point_B, point_C= new_point(point_A, point_B, num),\
        new_point(point_B, point_C, num), new_point(point_C, point_A, num)
    points_list = [point_A, point_B, point_C]
    x_list=[]
    y_list=[]    

plt.show() 
