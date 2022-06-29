class Point:
    "Description of the CLASS"
    
    color = 'red'
    circle = 2

a = Point()
b = Point()

print(Point.__doc__)

a.color, a.circle = 'blue', 4 # local attribute of the object 'a'
print(a.__dict__) # {'color': 'blue', 'circle': 4}
print(b.__dict__) # {} empty local collection

# create new attribute. WAY 1
Point.line = 'bold' 
print(Point.__dict__)

# create new attribute. WAY 2
setattr(Point, 'line', 'thin')
print(Point.__dict__)

# output with correct error if it will appear
print(getattr(Point, 'circle', 'Not found'))
print(getattr(Point, 'type', 'Not found'))

del Point.line
print(Point.__dict__)

print(hasattr(Point, 'line')) # False

delattr(a, 'circle') # delete LOCAL property 'circle' of the object 'a'
print(a.circle) # property 'circle' get value from Point

#create LOCAL property of object
a.x, a.y = 1, 1
b.x, b.y = 4, 4
print(a.__dict__, b.__dict__, sep='\n')


print('*************************************************')


class Person:
    name = 'Dorian'
    job = 'Creator'
    city = 'Neverland'
    
p1 = Person()

print('job' in p1.__dict__)