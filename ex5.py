'''
Методы класса (classmethod) и статические методы (staticmethod)
'''

class Vector:

    MIN, MAX = 0, 100

    @classmethod # работает только с атрибутами класса
    def check(cls, value):
        return cls.MIN <= value <= cls.MAX

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.check(x) and self.check(y): # classmethod
            self.x = x
            self.y = y
        
        print(self.norm2(5, 2)) # staticmethod

    def get_coord(self):
        return self.x, self.y

    @staticmethod # независимая функция, работает с параметрами, которые в ней определяются
    def norm2(x, y):
        return x*x+y*y

pt = Vector(5, 5)
res = Vector.get_coord(pt)
print(res)


print('Classmethod: ', Vector.check(15)) # classmethod
print('Staticmethod: ', Vector.norm2(5, 2)) # staticmethod

