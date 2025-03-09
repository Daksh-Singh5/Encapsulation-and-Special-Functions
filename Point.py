#Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x)+","+str(self.y)
    
    def __add__(self,other):
        totalx = self.x+other.x
        totaly = self.y+other.y
        return(Point(totalx,totaly))
    def __sub__(self,other):
        diffx = self.x-other.x
        diffy = self.y-other.y
        return(Point(diffx,diffy))
    def __mul__(self,other):
        diffx = self.x*other.x
        diffy = self.y*other.y
        return(Point(diffx,diffy))
    def getdis(self,other):
        diffx = (self.x-other.x)**2
        diffy = (self.y-other.y)**2
        print((diffx+diffy)**0.5)
    
    
point1 = Point(2,5)
point2 = Point(8,5)
print(point1)
print(point1+point2)
print(point1-point2)
print(point1*point2)
point1.getdis(point2)
        