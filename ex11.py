'''
Магические методы __str__, __repr__, __len__, __abs__

__str__() - для отобр. инф. об объекте класса для пользователей
__repr__() - для отобр. инф. об объекте класса в режиме отладки (для разраб-ов)
__len()__ - позволяет применять ф-цию len() к экземпляру класса
__abs__() - позволяет применять ф-цию abs() к экземпляру класса

'''

class Cat:

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str: # должен возвращать строку
        return f'{self.__class__}: {self.name}'

    def __str__(self) -> str: # должен возвращать строку! 
        return f'{self.name}'

cat = Cat('Felix')
print(cat)
str(cat)

class Point:

    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))
        
p = Point(1, -2, 3)
print(len(p))
print(abs(p))

print('*************************************************')

class Book:

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'

book = Book('Скотный двор', 'Дж. Оруэлл', 150)
print(book)

print('*************************************************')

class Model:

    def query(self, **kwargs):
        self.items =  kwargs
        print(self.__dict__)

    def __str__(self) -> str:
        if hasattr(self, 'items'):
            return f'Model: ' + ', '.join(map(lambda x: f'{x[0]} = {x[1]}', self.items.items()))
        else:
            return 'Model'
model = Model()
model.query(id=1, fio='Frank Kliri', old=22)
print(model)

print('*************************************************')

class WordString:

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    def __init__(self, string=''):
        self.string = string

    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx):
        return self.string.split()[indx]

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")

print('*************************************************')

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) in (int, float):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return abs((self.real**2 + self.img**2)**0.5)

cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)

print('*************************************************')

class RadiusVector:

    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0] * args[0]
            
        if len(args) > 1:
            self.coords = args

        self.len = len(self.coords)

    def set_coords(self, *args):
        if all(map(lambda x: type(x) in (int, float), args)):
            if len(args) > 0:
                n = min(len(args), len(self.coords))
                self.coords[:n] = args[:n]          
                
    def get_coords(self):
        return tuple(self.coords)

    def __len__(vector):
        return len(vector.coords)

    def __abs__(vector):
        return sum(map(lambda x: x**2, vector.coords)) ** 0.5

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords()) # (3, -5.6, 8)

a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.get_coords()) # 

vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(res_len, res_abs)

print('*************************************************')

class DeltaClock:

    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self) -> str:
        time = self.__len__()
        h = time // 3600
        m = time % 3600 // 60
        s = time % 3600 % 60
        
        return f'{h:02}: {m:02}: {s:02}'

    def __len__(self):
        diff = self.clock1.get_time() - self.clock2.get_time()
        return diff if diff > 0 else 0

class Clock:

    def __init__(self, hour: int, min: int, sec: int):
        self.hours = hour
        self.minutes = min
        self.seconds = sec

    def get_time(self):
        return self.hours*3600 + self.minutes*60 + self.seconds

dt = DeltaClock(Clock(3, 10, 0), Clock(2, 40, 0))
print(dt) # 00: 30: 00
print(len(dt)) # 1800

print('*************************************************')

class Ingredient:

    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self) -> str:
        return f'{self.name}: {self.volume}, {self.measure}'

class Recipe:

    def __init__(self, *args):
        self.ingredients = list(args)
    
    def add_ingredient(self, ing):
        self.ingredients.append(ing)
    
    def remove_ingredient(self, ing):
        self.ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.ingredients)

    def __len__(self):
        return len(self.ingredients)

recipe = Recipe()
ing1 = Ingredient("Соль", 1, "столовая ложка")
recipe.add_ingredient(ing1)
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3

print(ing1, n, sep='\n')

print('*************************************************')

class PolyLine:

    def __init__(self, *coords):
        self.coords = list(coords)

    def add_coord(self, x=0, y=0):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(5, 5)
poly.remove_coord(3)
print(poly.get_coords()) # (1, 2), (3, 5), (0, 10), (5, 5)
