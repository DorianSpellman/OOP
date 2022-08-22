'''
Функция issubclass(). Наследование от встроенных типов и от object.

Любой класс автоматически наследуется от базового класса object,
чтобы обеспечить стандартный функционал
'''

class Geom:
    pass

class Line(Geom):
    pass

g = Geom()
l = Line()
# issubclass() - в кач-ве аргументов только классы
print(issubclass(Line, Geom)) # True
print(issubclass(Geom, object)) # True
print(issubclass(dict, object)) # True
# isinstance() - в кач-ве аргументов что угодно
print(isinstance(l, Line))
print(isinstance(Geom, object))

class List(list):

    def __str__(self):
        return ' | '.join(map(str, self))

v = List([1, 2, 3])
print(v)

print('*************************************************')

class ListInteger(list):

    @staticmethod
    def check(x):
        if type(x) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, lst):
        for x in lst:
            self.check(x)
        super().__init__(lst)

    def __setitem__(self, indx, value):
        self.check(value)
        super().__setitem__(indx, value)
                
    def append(self, value):
        self.check(value)
        super().append(value)


s = ListInteger((1, 2, 3))
print(s)
s[1] = 20
s.append(4)
print(s)
#s[0] = 10.5 # TypeError

print('*************************************************')

class Thing:

    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self) -> int:
        return hash((self.name, self.price, self.weight))

class DictShop(dict):

    def __init__(self, dct={}):
        if isinstance(dct, dict):
            if all(isinstance(key, Thing) for key in dct.keys()):
                super().__init__(dct)
            else:
                raise TypeError('ключами могут быть только объекты класса Thing')
        else:
            raise TypeError('аргумент должен быть словарем')

    def __setitem__(self, key, value):
        if isinstance(key, Thing):
            return super().__setitem__(key, value)
        else:
            raise TypeError('ключами могут быть только объекты класса Thing')


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

#dict_things[1] = th_1 # исключение TypeError

print('*************************************************')

class Protists: # протисты
    pass

class Plants(Protists):
    pass

class Animals(Protists):
    pass

class Mosses(Plants): # мхи
    pass 

class Flowering(Plants):
    def __init__(self, name: str, weight: float, old: int):
        self.name = name
        self.weight = weight
        self.old = old

class Flower(Flowering):
    pass

class Worms(Animals):
    def __init__(self, name: str, weight: float, old: int):
        self.name = name
        self.weight = weight
        self.old = old

class Worm(Worms):
    pass

class Mammals(Animals): # млекопитающие
    pass

class Human(Mammals):
    def __init__(self, name: str, weight: float, old: int):
        self.name = name
        self.weight = weight
        self.old = old

class Person(Human):
    pass

class Monkeys(Mammals):
    def __init__(self, name: str, weight: float, old: int):
        self.name = name
        self.weight = weight
        self.old = old

class Monkey(Monkeys):
    pass

m1 = Monkey("мартышка", 30.4, 7)
m2 = Monkey("шимпанзе", 24.6, 8)
p1 = Person("Балакирев", 88, 34)
p2 = Person("Верховный жрец", 67.5, 45)
f1 = Flower("Тюльпан", 0.2, 1)
f2 = Flower("Роза", 0.1, 2)
w1 = Worm("червь", 0.01, 1)
w2 = Worm("червь 2", 0.02, 1)

lst_objs = [m1, m2, p1, p2, f1, f2, w1, w2]

lst_animals = [animal for animal in lst_objs if isinstance(animal, Animals)]
lst_plants  = [plant for plant in lst_objs if isinstance(plant, Plants)]
lst_mammals = [mammal for mammal in lst_objs if isinstance(mammal, Mammals)]

print(lst_animals, lst_plants, lst_mammals, sep='\n')

print('*************************************************')

class Tuple(tuple):

    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))
        
t = Tuple([1, 2, 3])
print(t)
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')

print('*************************************************')

class VideoItem:

    def __init__(self, title: str, descr: str, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

class VideoRating:

    def __init__(self):
        self.__rating = 0

    @property
    def rating(self): return self.__rating
    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and 0 <= value <= 5:
            self.__rating = value
        else:
            raise ValueError('неверное присваиваемое значение')

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5

print('*************************************************')

class IteratorAttrs:

    def __iter__(self):
        for attr in self.__dict__.items():
            yield attr

class SmartPhone(IteratorAttrs):

    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone('Samsung A51', (6, 2), 128)

for attr, value in phone:
    print(f'{attr}: {value}')