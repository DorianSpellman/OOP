'''
Магический метод __bool__ определения правдивости объектов

__bool__() - вызывается в приоритетном порядке ф-ией bool
__len__() - вызывается ф-ией bool, если не определеён маг.метод __bool__

Для непустых данных True, для пустых - False
'''

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x ** 2 + self.y ** 2

    def __bool__(self): # сработает в приоритете
        return self.x == self.y

p = Point(2, 2)
p2 = Point(0, 0)
print(bool(p), bool(p2)) 
if p:
    print('x == y')
else:
    print('x != y')

class User:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def __len__(self): # bool не вызовет эту ф-цию
        return self.old + 1 

    def __bool__(self):
        return bool(self.old)

user1 = User('Sergey', 45)
user2 = User('Петр', 0)

print(bool(user1), bool(user2)) # True False

print('*************************************************')

class Player:

    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)


lst_in = ['Isak W.; 23; 2000',
        'Joe M.; 27; 0',
        'Ron H.; 18; 5400',
        'Hue O.; 20; 0']
players = list()

for player in lst_in:
    name = player.split(';')[0]
    old = int(player.split(';')[1])
    score = int(player.split(';')[2])
    player = Player(name, old, score)
    players.append(player)

players_filtered = list(filter(lambda p: bool(p), players)) # остаются игроки, с очками > 0
print(len(players_filtered))

print('*************************************************')

class MailBox:

    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = ['intern@work.com; Work; Welcome!',
        'unkown@gmail.com; Summer Sales; Get ready!',
        'greenwich@mail.ru; From Honore; Miss u in the city']

        for msg in lst_in:
            self.inbox_list.append(MailItem(*msg.split(';')))

class MailItem:

    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, flag):
        self.is_read = flag
    
    def __bool__(self):
        return self.is_read

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

for i in mail.inbox_list:
    print(i.is_read)

inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(len(inbox_list_filtered))

print('*************************************************')

class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __len__(self):
        L = ((self.x2 - self.x1) + (self.y2 - self.y1)) ** 0.5
        return int(L) # True if L >= 1 else False

line = Line(2, 2, 5, 5)
print(len(line), bool(line)) # 2 True

print('*************************************************')
    
class Ellipse:

    def __init__(self, *coords):
        if len(coords) > 1:
            self.x1, self.y1, self.x2, self.y2 = coords

    def __bool__(self):
        return all([hasattr(self, 'x1'), hasattr(self, 'y1'), 
                    hasattr(self, 'x2'), hasattr(self, 'y2')])

    def get_coords(self):
        if bool(self):
            return (self.x1, self.y1, self.x2, self.y2)
        else:
            raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(1, 8, 8, 1), Ellipse(3, 6, 6, 3), Ellipse(), Ellipse()]

for figure in lst_geom:
    if figure:
        print(figure.get_coords())

print('*************************************************')

from inspect import CO_VARKEYWORDS
from random import randint

class Cell:

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = True

    @property
    def is_mine(self): return self.__is_mine
    @is_mine.setter
    def is_mine(self, value): 
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def is_open(self): return self.__is_open
    @is_open.setter
    def is_open(self, value): 
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    @property
    def number(self): return self.__number
    @number.setter
    def number(self, value): 
        if type(value) != int or value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    def __bool__(self):
        return not self.is_open

class GamePole:

    __instance = None

    def __new__(cls, *args): # паттерн Синглтон для создания единственного объекта класса
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self): # при удалении объекта его ссылка будет на None
        GamePole.__instance = None

    def __init__(self, N, M, total_mines):
        self._n = N
        self._m = M
        self._total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range (N))
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for row in self.pole:
            for x in row:
                x.is_mine = False
                #x.is_open = False

        m = 0
        while m < self._total_mines: # расставляем мины
            i = randint(0, self._n - 1)
            j = randint(0, self._m - 1)
            if self.__pole_cells[i][j].is_mine: # если мина уже есть
                continue
            self.__pole_cells[i][j].is_mine = True
            m += 1

        indx = (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)

        for x in range(self._n):
            for y in range(self._m):
                if not self.pole[x][y].is_mine: # если нет мины
                    mines = sum((self.pole[x+i][y+j].is_mine for i, j in indx if 0 <= x+i < self._n and 0 <= y+j < self._m))
                    self.pole[x][y].number = mines

    def open_cell(self, i, j):
        if not 0 <= i < self._n or not 0 <= j < self._m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))
        

pole = GamePole(10, 10, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.show_pole()

print('*************************************************')

class Vector:

    def __init__(self, *coords):
        self.coords = list(coords)

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        if len(self) == len(other):
            coords = [self.coords[i] + other.coords[i] for i in range(len(self))]
            return Vector(*coords)
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __sub__(self, other):
        if len(self) == len(other):
            coords = [self.coords[i] - other.coords[i] for i in range(len(self))]
            return Vector(*coords)
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __mul__(self, other):
        if len(self) == len(other):
            coords = [self.coords[i] * other.coords[i] for i in range(len(self))]
            return Vector(*coords)
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __iadd__(self, other):
        if type(other) is int:
            for i in range(len(self)):
                self.coords[i] += other
            return self

        if type(other) is Vector:
            return self + other

    def __isub__(self, other):
        if type(other) is int:
            for i in range(len(self)):
                self.coords[i] -= other

            self.coords = tuple(self.coords)
            return self

        if type(other) is Vector:
            return self - other

    def __eq__(self, other):
        return self.coords == other.coords


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True


