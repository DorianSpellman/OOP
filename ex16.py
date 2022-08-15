''''
Магические методы __getitem__, __setitem__ и __delitem__

__getitem__(self, item) - получение значения по ключу item
__setitem__9self, key, value) - запись значения value по ключу key
__delitem__(self, key) - удаление элемента по ключу key
'''

from calendar import c
from tabnanny import check
from turtle import st
from typing import Type


class Student:

    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise Type('Индекс должен быть целым положительным числом')

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        del self.marks[key]

s1 = Student('Noel', [5, 5, 4, 3, 5])
#print(s1.marks[2]) # 4
print(s1[2])
s1[3] = 4
s1[10] = 5
print(s1.marks)
del s1[5:10]
print(s1.marks)

print('*************************************************')

class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs) # создаём лок. атрибуты с соотв. значениями

    def check_indx(self, indx):
        if type(indx) != int or abs(indx) < 0 or indx >= len(self.__dict__):
            raise IndexError('неверный индекс поля')
            
    def __setitem__(self, indx, value):
        self.check_indx(indx)
        keys = list(self.__dict__.keys()) # ['pk', 'title', 'author']
        self.__dict__[keys[indx]] = value

    def __getitem__(self, indx):
        self.check_indx(indx)
        keys = list(self.__dict__.keys())
        return self.__dict__[keys[indx]]

    

r = Record(pk=1, title='Book 1', author='Author 1')
print(r.title) # Book 1

r[0] = 2 # доступ к полю pk
r[1] = 'Book 2' # доступ к полю title
r[2] = 'Author 2' # доступ к полю author
print(r.__dict__)
print(r[1]) # Book 2
#r[3] # генерируется исключение IndexError

print('*************************************************')

class Track:

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def add_point(self, x, y, speed):
        item = [(x, y), speed]
        self.tracks.append(item)
    
    def __getitem__(self, indx):
        self.validate(indx)
        return self.tracks[indx]

    def __setitem__(self, key, speed_value):
        self.validate(key)
        self.tracks[key][1] = speed_value

    def validate(self, i):
        if i < 0 or i >= len(self.tracks):
            raise IndexError('некорректный индекс')

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
print(tr.__dict__)
tr[2] = 60
coords, speed = tr[2]
print(f'coords: {coords} - speed: {speed}')

print('*************************************************')

class Integer:

    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self): return self.__value
    @value.setter
    def value(self, val): 
        if not isinstance(val, int):
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self) -> str:
        return str(self.__value)

class Array:

    def __init__(self, max_length: int, _cls):
        self.max_length = max_length
        self._cls = _cls
        self.array = [self._cls() for _ in range(self.max_length)]

    def check(self, i):
        if not isinstance(i, int) or i < 0 or i >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, indx):
        self.check(indx)
        return self.array[indx].value

    def __setitem__(self, indx, val):
        self.check(indx)
        self.array[indx].value = val

    def __repr__(self):
        return ' '.join(map(str, self.array))

ar_int = Array(10, _cls=Integer)
print(ar_int[3])

ar_int[0] = 1
ar_int[4] = 5 
ar_int[9] =  10
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел

print('*************************************************')

class IntegerValue:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

class CellInteger:

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

class TableValues:

    def __init__(self, rows: int, cols: int, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')

        self.rows = rows
        self.cols = cols
        self.cell = cell
        
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))
        
    def check(self, indx):
        i, j = indx
        if type(i) != int or not (0 <= i < self.rows) \
            or type(j) != int or not (0 <= j < self.cols):
            raise IndexError()

    def __getitem__(self, indx):
        self.check(indx)
        i, j = indx
        return self.cells[i][j].value

    def __setitem__(self, indx, value):
        self.check(indx)
        i, j = indx
        self.cells[i][j].value = value

table = TableValues(2, 3, cell=CellInteger)
table[1, 1] = 10
table[0, 0] = 1 # row: 0 col: 0
table[0, 1] = 2 # row: 0 col: 1
table[0, 2] = 3 # row: 0 col: 2
print(table[0, 1]) # 2
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' | ')
    print('\n'+ '- '*len(row)*2)

print('*************************************************')

class StackObj:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.stack = []
        if self.stack == []:
            self.top = None

    def push(self, obj):
        self.stack.append(obj)
        self.top = self.stack[0]
        if len(self.stack) > 1:      
            self.stack[-2].next = obj     

    def pop(self):
        if len(self.stack) >= 2:
            self.stack[-2].next = None
            return self.stack.pop(-1)

        if len(self.stack) == 1:
            head = self.stack.pop(0)
            self.top = None
            return head

        if len(self.stack) == 0:
            return None

    def __getitem__(self, indx):
        self.verify(indx)
        return self.stack[indx]

    def __setitem__(self, indx, value):
        self.verify(indx)
        self.stack[indx-1].next = value # ссылку на следующий у предыдущего обновляем
        
        next = self.stack[indx].next # запоминаем следующий за текущим

        self.stack[indx] = value # обновляем текущий

        self.stack[indx].next = next # обновляем ссылку на следующий

    def verify(self, i):
        if not isinstance(i, int) or i < 0 or i >= len(self.stack):
            raise IndexError('неверный индекс')

st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))

st[1] = StackObj("obj2-new")

obj = st.pop()

print(st.__dict__)
n = 0
h = st.top
for i in st.stack:
    print(i.__dict__)

print('*************************************************')

class RadiusVector:

    def __init__(self, *coords):
        self.coords = list(coords)

    '''При передаче среза в магических методах __setitem__() и __getitem__() 
    параметр индекса становится объектом класса slice. 
    Его можно указывать непосредственно в квадратных скобках 
    упорядоченных коллекций (списков, кортежей и т.п.)'''

    def __getitem__(self, indx):
        if type(indx) is int:
            return self.coords[indx]
        if type(indx) is slice:
            return tuple(self.coords[indx])

    def __setitem__(self, indx, value):
        self.coords[indx] = value

v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5
print(v[:])

print('*************************************************')

class TicTacToe:

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = '*'

    def check(self, indx):
        if type(indx) != tuple or len(indx) != 2:
            raise IndexError('неверный индекс клетки')
        i, j = indx          

    def __setitem__(self, indx, value):
        self.check(indx)
        i, j = indx
        if self.pole[i][j]:
            self.pole[i][j].value = value
            self.pole[i][j].is_free = False
        else:
            raise ValueError('клетка уже занята')
        
    def __getitem__(self, indx):
        self.check(indx)
        i, j = indx
        if type(i) == slice:
            return tuple(self.pole[x][j].value for x in range(3))
        if type(j) == slice:
            return tuple(self.pole[i][x].value for x in range(3))

        return self.pole[i][j].value

class Cell:

    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return bool(self.is_free)

game = TicTacToe()
game.clear()
game[0, 0] = 'X'
game[1, 0] = '0'
game[1, 1] = 'X'

for row in game.pole:
    for i in row:
        print(i.value, end=' | ')
    print()
# формируется поле:
# X | * | * |
# 0 | X | * |
# * | * | * |

v1 = game[0, :]  # ('X', '*', '*')
v2 = game[:, 0]  # ('X', '0', '*')
print(v1, v2)

print('*************************************************')

class Thing:

    def __init__(self, name: str, weight):
        self.name  = name 
        self.weight = weight

class Bag:

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.total_weight = 0
        self.things = []
    
    def __check_weight(self, new, old=None):
        if old is None:
            total_weight = self.total_weight + new.weight
        else:
             total_weight = self.total_weight - old.weight + new.weight
        if total_weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов') 

    def __check_index(self, indx):
        if  not (0 <= indx < len(self.things)):
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        self.__check_weight(thing)
        self.things.append(thing)
        self.total_weight += thing.weight

    def __getitem__(self, indx):
        self.__check_index(indx)
        return self.things[indx]

    def __setitem__(self, indx, new):
        self.__check_index(indx)
        old = self.things[indx]
        self.__check_weight(new, old)
        self.things[indx] = new
        self.total_weight += new.weight

    def __delitem__(self, indx):
        self.__check_index(indx)
        self.total_weight -= self.things[indx].weight
        del self.things[indx]

    def __call__(self):
        for thing in self.things:
            print(thing.name, end=' ')
        print(f'| total weight: {self.total_weight}')
            
        

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag() # книга носки рубашка | total weight: 800
#bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[1].name) # носки
bag[1] = Thing('наушники', 100)
bag() # книга наушники рубашка | total weight: 900
del bag[0]
bag() # наушники рубашка | total weight: 800

print('*************************************************')

class Cell:

    def __init__(self, value):
        self.value = value

class SparseTable:

    def __init__(self):
        self.table = {}

    @property
    def rows(self):
        return max(i[0] for i in self.table) + 1 if self.table else 0

    @property
    def cols(self):
        return max(i[1] for i in self.table) + 1 if self.table else 0

    def add_data(self, row, col, data):
        self.table[(row, col)] = data

    def remove_data(self, row, col):
        if not (row, col) in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.table[(row, col)]
        
    def __getitem__(self, indx):
        if not indx in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.table[indx].value            

    def __setitem__(self, key, value):
        self.table.setdefault(key, Cell(0)).value = value

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError