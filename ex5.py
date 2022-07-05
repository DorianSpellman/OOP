'''
Методы класса (classmethod) и статические методы (staticmethod)
'''

class Vector:

    MIN, MAX = 0, 100

    @classmethod
    def check(cls, value):
        return cls.MIN <= value <= cls.MAX

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Vector.check(15))