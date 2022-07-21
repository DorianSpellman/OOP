"""
Свойства property. Декоратор @property
"""

class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    #old = property(get_old, set_old)

p = Person('Honore', 20)
p.old = 21
print(p.old)
del p.old
print(p.__dict__)

print('*************************************************')

class Car:

    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str and 2 <= len(model) <= 100:
            self.__model = model
        else:
            None
    

car = Car()
car.model = 'BMW'
print(car.__dict__)

print('*************************************************')

class WindowDlg:

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) == int and 0 <= val <= 1000:
            self.__width = val
            self.show()
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) == int and 0 <= val <= 1000:
            self.__height = val
            self.show()


wnd = WindowDlg('Dia', 100, 50)
wnd.height = 100

print('*************************************************')

class RadiusVector2D:

    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__verify(x):
            self.__x = x
        if self.__verify(y):
            self.__y = y        

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if self.__verify(x):
            self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if self.__verify(y):
            self.__y = y
    
    @classmethod
    def __verify(cls, val):
        return type(val) in (int, float) and RadiusVector2D.MIN_COORD <= val <= RadiusVector2D.MAX_COORD

    @staticmethod
    def norm2(vector):
        return vector.x**2 +vector.y**2

r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)

print(r1.__dict__)
print(r2.__dict__)
print(r3.__dict__)


print('*************************************************')

class TreeObj:
    
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            obj = obj_next
        return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.indx] == 1:
            return obj.left
        else:
            return obj.right

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)

print('*************************************************')

class PathLines:

    def __init__(self, *args):
        self.list = list(args)

    def get_path(self):
        return self.list

    def get_length(self): # возвращает суммарную длину пути (сумма длин всех линейных сегментов);
        x0 = y0 = 0
        sum_len = 0
        for point in self.list:
            x1, y1 = point.x, point.y
            dx, dy = abs(x1-x0), abs(y1-y0)
            sum_len += ((dx**2 + dy**2) ** 0.5)
            x0, y0 = x1, y1
        return sum_len
        #g = ((self.list[i-1], self.list[i]) for i in range(1, len(self.list))) # генератор (line0, line1)
        #return sum(map(lambda point: ((point[0].x - point[1].x) ** 2 + (point[0].y - point[1].y) ** 2)**0.5, g))

    def add_line(self, line): 
        self.list.append(line)

class LineTo:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        

p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []