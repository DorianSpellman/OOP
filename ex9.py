'''
Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__

Магические методы - методы с двумя нижними подчеркиваниями до и 
после имени метода, которые автоматически вызываются 
в определенных для них ситуациях.

__setattr__(self, key, value) - авт вызывается при изменении свойства key класса
__getattribute__(self, item) - авт вызывается при получении свойства класса с именем item
__getattr(self, item) - авт вызывается при получении несуществующего свойства item класса
__delattr__(self, item) - авт вызывается при удалении свойства item
'''

from calendar import c
from pyrsistent import b


class Point:

    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Доступ к переменной запрещён')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key in ('x', 'y'):
            object.__setattr__(self, key, value)
        else:
            raise AttributeError('Недопустимое имя')            

    def __getattr__(self, item):
        print(f'Несуществующий атрибут "{item}"')

    def __delattr__(self, item):
        object.__delattr__(self, item)
        print(f'{item} успешно удалён!')        


p1 = Point(1, 1)
p2 = Point(2, 2)

#try1 = p1.x #ValueError: Доступ к переменной запрещён
print(p1.y) # OK

p1.x = 5
#p1.z = 0 # AttributeError: Недопустимое имя
p1.yy # Несуществующий атрибут "yy"

del p2.y

print('*************************************************')

class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author') and type(value) is str:
            object.__setattr__(self, key, value)
        elif key in ('pages', 'year') and type(value) is int:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Singing in the thorn', 'Colleen McCullough', 650, 1977)

print(book.__dict__)

print('*************************************************')

class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    
    __ID = 1
    attrs = {'id' : (int,),
             'name' : (str,),
             'weight' : (int, float),
             'price' : (int, float)
             }

    def __init__(self, name, weight, price):
        self.id = Product.__ID
        self.name = name
        self.weight = weight
        self.price = price
        Product.__ID += 1
    
    def __setattr__(self, name, value):
        if type(value) not in self.attrs[name] or (name in ('weight', 'price') and value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, name, value)         

    def __delattr__(self, name):
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

shop = Shop("Book worm")
book = Product("Singing in the thorn", 300, 1000)
shop.add_product(book)
shop.add_product(Product("Magazin", 100, 250))
for p in shop.goods:
    print(f"{p.name} | {p.weight} | {p.price}")
    
print('*************************************************')

class Course:

    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)
    
    def remove_module(self, indx):
        self.modules.pop(indx)

class Module:
    
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)
    
    def remove_lesson(self, indx):
        self.lessons.pop(indx)

class LessonItem:

    attrs = {'title' : (str,),
            'practices' : (int,),
            'duration' : (int,)
            }

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, name, value):
        if type(value) not in self.attrs[name] or (name in ('practices', 'duration') and value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, name, value)
    
    def __getattr__(self, item): # При обращении к несуществующим атрибутам объектов
        return False

    def __delattr__(self, item): # Запрет на удаление
        raise AttributeError(f"Атрибут {item} удалять запрещено.")

course = Course("Python ООП")
module_1 = Module("Часть первая")
lesson_1 = LessonItem("Урок 1", 7, 1000)
#del lesson_1.title
module_1.add_lesson(lesson_1)
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)

print(lesson_1.__dict__)
print(lesson_1.price)

print('*************************************************')

class Museum:

    def __init__(self, name: str):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)
    
    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)
    
    def get_info_exhibit(self, indx):
        exhibit = self.exhibits[indx]
        print(f'Описание экспоната {exhibit.name}: {exhibit.descr}')

class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr

class Mummies:
    def __init__(self, name, location , descr):
        self.name = name
        self.location = location
        self.descr = descr

class Papyri:
    def __init__(self, name, date: str, descr):
        self.name = name
        self.date = date
        self.descr = descr
    

mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Девятый вал", "И.К. Айвазовский", "Вдохновляющая, устрашающая, волнующая картина."))
mus.add_exhibit(Mummies("Фараон", "Древний Египет", "Один из правителей Египта."))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования.")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
mus.get_info_exhibit(0)

print('*************************************************')

class SmartPhone:

    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
    # # кол-во элементов в отфильтрованном списке, содержащем названия одинаковых классов, = 0
        if len(list(filter(lambda x: type(x) == type(app), self.apps))) == 0:  
            self.apps.append(app) 
    
    def remove_app(self, app):
        self.apps.remove(app)

class AppVK:

    def __init__(self):
        self.name = 'ВКонтакте'

class AppYouTube:

    def __init__(self, memory_max):
        self.name = 'YouTube'
        self.memory_max = memory_max

class AppPhone:

    def __init__(self, phone_list: dict):
        self.name = 'Phone'
        self.phone_list = phone_list 

    
sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
app_2 = AppYouTube(1024) 
app_3 = AppPhone({"Zen": 1234567890, "Fia": 234597424, "Work": 5886722}) 
sm.add_app(app_2)
sm.add_app(app_3)
for a in sm.apps:
    print(a.name)

print('*************************************************')

class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
    
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            return object.__setattr__(self, name, value)
        raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
print(x, y)
print(circle.name) # False, т.к. атрибут name не существует
print(circle.__dict__)

print('*************************************************')

class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, val):
        self.__a = val

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, val):
        self.__b = val
    
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, val):
        self.__c = val
    
    def __setattr__(self, name, value):
        if name in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if isinstance(value, (int, float)) and Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION:
            object.__setattr__(self, name, value)
        
        
d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a, b, c)
#d.MAX_DIMENSION = 10  # исключение AttributeError

print('*************************************************')

import time

class Mechanical:

    def __init__(self, date: float):
        if type(date) is float and date > 0:
            self.date = date
        
    def __setattr__(self, name, value):
        if name == 'date' and name in self.__dict__:
            return
        super().__setattr__(name, value)

class Aragon:

    def __init__(self, date: float):
        if type(date) is float and date > 0:
            self.date = date
        
    def __setattr__(self, name, value):
        if name == 'date' and name in self.__dict__:
            return
        super().__setattr__(name, value)

class Calcium:

    def __init__(self, date: float):
        if type(date) is float and date > 0:
            self.date = date

    def __setattr__(self, name, value):
        if name == 'date' and name in self.__dict__:
            return
        super().__setattr__(name, value)

class GeyserClassic:

    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = {(1, 'Mechanical') : None,
                        (2, 'Aragon') : None,
                        (3, 'Calcium') : None
                        }

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):
        for key in self.filters:
            if key[0] == slot_num:
                self.filters[key] = None
        

    def get_filters(self):
        return (self.filters.values())

  
    def water_on(self):
        return all([filter != None and 0 <= time.time() - filter.date <= self.MAX_DATE_FILTER for filter in self.filters.values()])
       

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() 
print(f'Water on (2): {w}') # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() 
print(f'Water on (3): {w}') # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
print(f'Filter 1: {f1} \nFilter 2: {f2} \nFilter 3: {f3}')
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
my_water.remove_filter(3)
print(list(my_water.filters.values())) # [obj, obj, None]


