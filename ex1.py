class Point:
    color = 'red'
    circle = 2

a = Point()
b = Point()

a.color, a.circle = 'blue', 4 # local attribute of the object 'a'
print(a.__dict__)
print(b.__dict__) # empty collection

Point.line = 'bold'
print(Point.__dict__)

setattr(Point, 'line', 'thin')
print(Point.__dict__)

print(getattr(Point, 'circle', 'Not found'))
print(getattr(Point, 'type', 'Not found'))

del Point.line
print(Point.__dict__)

print(hasattr(Point, 'line')) # False

delattr(a, 'circle') # delete LOCAL property 'circle' of the object 'a'
print(a.circle) # property 'circle' get value from Point


