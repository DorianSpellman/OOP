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