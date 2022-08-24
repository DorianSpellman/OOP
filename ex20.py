'''
Наследование. Функция super() и делегирование

Делегирование - вызов методов через вызов super()/

Расширение (extended) базового класса и переопределение (overriding) методов
'''

class Geom:
    name = 'Geom'
 
    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Line(Geom):
 
    def draw(self):
        print("Рисование линии")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2) # делигирование
        print("инициализатор Rect")
        self.fill = fill
 
    def draw(self):
        print("Рисование прямоугольника")

l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
print(r.__dict__)

print('*************************************************')

class Book:

    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    
class DigitBook(Book):

    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm

db = DigitBook('Три товарища', 'Ремарк Э.М.', 350, 1936, 15, 'txt')
print(db.__dict__)

print('*************************************************')

class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class ArtObject(Thing):

    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date
    
class Computer (Thing):

    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu

class Auto(Thing):

    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims

class Mercedes(Auto):

    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old

class Toyota(Auto):

    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel

print('*************************************************')

class SellItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class House(SellItem):

    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat (SellItem):

    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land (SellItem):

    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square

class Agency:

    def __init__(self, name):
        self.name = name
        self.lst = []

    def add_object(self, obj):
        self.lst.append(obj)

    def remove_object(self, obj):
        self.lst.remove(obj)

    def get_objects(self):
        return self.lst

print('*************************************************')

class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func
    
class Callback:

    def __init__(self, path, router_cls):
        self.__path = path
        self.__router_cls = router_cls

    def __call__(self, func):
        self.__router_cls.add_callback(self.__path, func)

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'

route = Router.get('/')
if route:
    ret = route()
    print(ret)

print('*************************************************')

def integer_params_decorated(func):

    def wrapper(self, *args, **kwargs):
        if not all(type(x) is int for x in args):
            raise TypeError("аргументы должны быть целыми числами")
        if not all(type(x) is int for x in kwargs.values()):
            raise TypeError("аргументы должны быть целыми числами")

        #print(f'{func}: {args}')
        return func(self, *args, **kwargs)
    
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
vector.set_coords(2, 5)

print('*************************************************')

def decorator(func):
    def set_name(name):
        print('~~~~~~~')
        func(name)
        print('~~~~~~~')
    
    return set_name

@decorator
def hello_world(name):
    print('Hello world, ' + name)

hello_world('Leo')

print('*************************************************')

class SoftList(list):

    def __getitem__(self, indx):
        try: 
            return super().__getitem__(indx)
        except:
            return False


sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False

print('*************************************************')

class StringDigit(str):

    def __init__(self, string):
        if isinstance(string, str) and string.isdigit():
            self.string = string
        else:
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        if type(other) is str:
            other = StringDigit(other)
        return StringDigit(self.string + other.string)

    def __radd__(self, other):
        if type(other) is str:
            other = StringDigit(other)
        return StringDigit(other.string + self.string)


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)
#sd = sd + "12f" # ValueError

print('*************************************************')

class ItemAttrs:

    def check(self, indx):
        if indx <= len(self.__dict__): 
            for n, key in enumerate(self.__dict__.keys()):
                if n == indx:
                    return key
        else:
            raise IndexError("Индекс превышает")

    def __getitem__(self, indx):
        key = self.check(indx)
        return self.__dict__[key]

    def __setitem__(self, indx, value):
        key = self.check(indx)
        self.__dict__[key] = value
            
class Point(ItemAttrs):

    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(1, 2.5)
x = pt[0]   # 1
print(x)
y = pt[1]   # 2.5
print(y)
pt[0] = 10
print(pt[0]) # 10

