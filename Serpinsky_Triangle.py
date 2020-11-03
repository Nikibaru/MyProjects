import matplotlib as mpl
import matplotlib.pyplot as plt
from time import sleep
from random import randint
import numpy as np

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def __sub__(self, other):
        return(Point(self.x-other.x, self.y-other.y))
    def __add__(self, other):
        return(Point(self.x+other.x, self.y+other.y))
    def __truediv__(self, num):
        return Point(self.x/num, self.y/num)

def new_point(zero_point, point_A, point_B, point_C, rand_num):
    if rand_num==1 or rand_num==2:
        return(point_A - zero_point)
    if rand_num==3 or rand_num==4:
        return(point_B - zero_point)
    if rand_num==5 or rand_num==6:
        return(point_C - zero_point)

def new_point_square(zero_point, point_A, point_B, point_C, point_D, rand_num):
    if rand_num==1 or rand_num==2:
        return(point_A - zero_point)
    if rand_num==3 or rand_num==4:
        return(point_B - zero_point)
    if rand_num==5 or rand_num==6:
        return(point_C - zero_point)
    if rand_num==7 or rand_num==8:
        return(point_D - zero_point)

point_A = Point(1,1)
point_B = Point(-1,-1)
point_C = Point(-1,1)
point_D = Point(1,-1)
zero_point = Point(0,0)

#plt.ion()
fig= plt.plot()


plt.scatter(point_A.x, point_A.y)
plt.scatter(point_B.x, point_B.y)
plt.scatter(point_C.x, point_C.y)
x=[]
x.append(zero_point.x)
y=[]
y.append(zero_point.y)
for i in range(50000):
    zero_point = zero_point +\
    new_point(zero_point, point_A, point_B, point_C, randint(1,6))/2
    x.append(zero_point.x)
    y.append(zero_point.y)

plt.scatter(x,y, s=0.1)
plt.show() 

