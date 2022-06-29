from random import *
import string


class Point:

    color = 'red'
    circle = 2
    i = 1

    def __init__(self, x=0, y=0, color='black'): # initialization when creating an object
        self.x = x
        self.y = y
        self.color = color
    
    def __del__(self):
        print(Point.i, 'object has deleted successful')
        Point.i += 1
        

    def set_coords(self, x, y):
        self.x = x  # creating local property 
        self.y = y  # of the object

    def get_coords(self):
        return (self.x, self.y) # return tuple with coords


pt = Point(1, 1, 'red')    # creating objects of the class
pt2 = Point(y=5)

print('pt:  ', pt.__dict__)         # pt:   {'x': 3, 'y': 3}
print('pt2: ', pt2.__dict__)        # pt2:  {'x': 5, 'y': 5}

print('pt:  ', pt.get_coords())     # pt:   (3, 3)
print('pt2: ', pt2.get_coords())    # pt2:  (5, 5)


points = [Point(i, i) for i in range(1, 10, 2)]

points[1].color = 'yellow'

for pt in points:
    print(pt.__dict__)

print('*************************************************')

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
    
class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
    
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
    
'''
Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (Line или Rect или Ellipse). 
Координаты также генерируются случайным образом.
'''
classes = [Line, Rect, Ellipse]
elements = [choice(classes)(*list(map(int, sample(string.digits, 4)))) for i in range (5)]

for q in elements:
    print(q.__dict__)


