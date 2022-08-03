'''
Режимы доступа public, private, protected. Сеттеры и геттеры.
'''

#from accessify import private, protected
from ast import arg


class Point:

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    #@private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


    def set_coord(self, x, y):  # Setter
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coords is must be digits!')

    def get_coord(self):        # Getter
        return self.__x, self.__y

pt = Point(3, 3)
# print(pt.__x, pt.__y) # AttributeError - нельзя обратиться к private свойствам
pt.set_coord(5, 5) # внутри класса работа разрешена
print(pt.get_coord())

print(dir(pt))
print(pt._Point__x)

print('*************************************************')

class Clock:

    def __init__(self, time=0):
        self.__time = time
    
    @classmethod
    def __check_time(cls, time):
        return type(time) == int and 0 <= time < 100000

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time
        
    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(15)
print(clock.get_time())  #15
clock.set_time(100000)
clock.set_time(-1)
clock.set_time('2')
clock.set_time(0.1)
print(clock.get_time())  #15

print('*************************************************')

class Money:

    def __init__(self, money):
        if self.__check_money(money):
            self.__money = money

    @staticmethod
    def __check_money(money):
        return type(money) is int and money >= 0


    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money
    
    def add_money(self, obj):
        self.__money += obj.__money

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
print(m1, m2)

print('*************************************************')

class Book:

    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title
        
    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

book1 = Book('W.Golding', 'The Lord of the Flies', 0)
book1.set_price(500)
print(book1.get_author(), book1.get_title(), book1.get_price(), sep=' | ')


print('*************************************************')

class Line:

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def draw(self):
        print(*[self.__x1, self.__y1, self.__x2, self.__y2])

line = Line(0, 0, 5, 5)
line.set_coords(5, 5, 7, 7)
print(line.get_coords())
line.draw()

print('*************************************************')

class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def get_coords(self):
        return (self.__x, self.__y)

class Rectangle:

    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]


    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(f'Прямоугольник с координатами: {self.get_coords()}')

rect = Rectangle(0, 0, 20, 34)
rect.draw()

print('*************************************************')

from string import *
from random import randint
class EmailValidator:

    SYMBOLS = ascii_letters + digits + '_.@'
    ADDRESS = ascii_letters + digits + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False

        if not set(email) < set(cls.SYMBOLS): # если в email входят НЕразрешённые символы
            return False

        mail = email.split('@') # только 1 символ @
        if not len(mail) == 2:
            return False

        if len(mail[0]) > 100 or len(mail[1]) > 50: # длина email до символа @ не должна превышать 100, после - 50
            return False

        if '.' not in mail[1]: # после символа @ обязательно должна идти хотя бы одна точка
            return False

        if email.count('..') > 0: # не должно быть двух точек подряд
            return False

        return True

        
    @classmethod
    def get_random_email(cls):
        before = randint(5, 20) # количество симоволов до @
        length = len(cls.ADDRESS) - 1
        return ''.join(cls.ADDRESS[randint(0, length)] for i in range(before)) + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

print(EmailValidator.get_random_email())
