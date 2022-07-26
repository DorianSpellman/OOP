"""
Дескрипторы (data descriptor и non-data descriptor).

С помощью дескрипторов можно упростить функционал и избежать
повторения кода при создании локальных свойств внутри объектов класса.

В одном классе дескриптора можно единожды описать логику 
взаимодействия с внутренними (приватными или защищенными) 
переменными.

Один класс дескриптора способен заменить множество 
однотипных объектов-свойств.

Дескриптор данных (data descriptor), 
когда в классе присутствуют методы __get__ и __set__.

Дескриптор не данных (non-data descriptor), когда в классе 
присутствует метод __get__, но отсутствует метод __set__.
"""

from jinja2 import pass_context
from jsonschema import Validator


class Integer: # data desctriptor

    @classmethod
    def verify(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class ReadIntX: # non-data descriptor

    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    

class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
       
    
p = Point3D(1, 2, 3)

p.__dict__['xr'] = 5 
print(f'p.xr: {p.xr}')
'''Будет выведено 5, так как ReadIntX - это дескриптор не данных 
и в инициализаторе будут созданы локальные свойства x, y. 
Затем, в строчке p.xr идет обращение к локальному свойству x 
со значением 5.
'''
p.__dict__['x'] = 10
print(f'p.x: {p.x}')
'''
Будет выведено '10, так как Integer - это дескриптор данных и он имеет 
наибольший приоритет при обращении к атрибутам, поэтому в строчке p.x будет 
обращение к дескриптору, а не к локальному свойству.
'''
print(p.__dict__)

print('*************************************************')

class FloatValue:

    @classmethod
    def verify(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Cell:

    value = FloatValue()

    def __init__(self, start=0.0):
        self.start = start

class TableSheet:

    def __init__(self, N, M):
        self.row = N
        self.column = M
        self.cells = [[Cell() for m in range(M)] for n in range(N)]


table = TableSheet(5, 3)
n = 1.0
for i in range(table.row):
    for j in range(table.column):
        table.cells[i][j].value = n
        n += 1.0

print(table.cells)

print('*************************************************')

class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class StringValue:

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class RegisterForm:

    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, log, pas, email):
        self.login = log
        self.password = pas
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')


rf = RegisterForm('Bazzy_Krol', 'Bazzy123', 'rabbit@grab.com')
print(rf.__dict__)
rf.show()
print(rf.get_fields())
rf = RegisterForm('B0', 42, 'BuzFuz')
print(rf.__dict__)

print('*************************************************')

class StringVal:

    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class PriceValue:

    def __init__(self, max_value):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:

    name = StringVal(min_length=2, max_length=50)
    price = PriceValue(max_value=10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")

print('*************************************************')

class Bag:
    
    @property  # объект-свойство для доступа к локальному приватному атрибуту __things (только для считывания, не записи)
    def things(self):
        return self.__things

    def __init__(self, max_weight):
        if type(max_weight) == int:
            self.max_weigth = max_weight
            self.__things = []

    def add_thing(self, thing):
        # добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит)
        if self.get_total_weight() + thing.weight <= self.max_weigth:
            self.things.append(thing)
        
    def remove_thing(self, indx):
        self.things.pop(indx)
        
    def get_total_weight(self):
        s = 0
        for thing in self.things:
            s += thing.weight
        return s

    
class Thing:

    def __init__(self, name, weight):
        if type(name) == str and type(weight):
            self.name = name
            self.weight = weight

bag = Bag(1000)
bag.add_thing(Thing("Книга", 100))
bag.add_thing(Thing("Свитер", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")

print('*************************************************')

class TVProgram:

    def __init__(self, name):
        if type(name) is str:
            self.name = name
            self.items = []

    def add_telecast(self, title):
        self.items.append(title)
    
    def remove_telecast(self, indx):
        for telecast in self.items:
            if telecast.id == indx:
                self.items.remove(telecast)
        
class Telecast:

    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if type(id) is int:
            self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name
    
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

pr = TVProgram("National Geographic")
pr.add_telecast(Telecast(1, "New Zeland", 10000))
pr.add_telecast(Telecast(2, "Brazil", 2000))
pr.add_telecast(Telecast(3, "The Earth", 20))
pr.remove_telecast(3)
for t in pr.items:
    print(f"{t.name}: {t.duration}")

    
    
