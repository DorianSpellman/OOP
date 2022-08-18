"""
Магические методы __iter__ и __next__

__iter__(self) - получение итератора для перебора объекта
__next__(self) - переход к следующему значению и его считывание

Итератор:

- это объект, который обеспечивает стандартный интерфейс 
    для перебора элементов коллекции в заданном порядке
- в общем случае, для каждого типа коллекции создается свой итератор, 
    но взаимодействие с ним (итератором) происходит по единому алгоритму
- для полноценной работы с объектом-итератором в нем должны быть 
    определены магические методы __iter__() и __next__()
- это объект, который контролирует перебор элементов некоторой
     коллекции в заданном порядке
"""

print(list(range(5))) # [0, 1, 2, 3, 4]
print()

a = iter(range(3))
print(next(a)) # 0
print(next(a)) # 1
print(next(a)) # 2
#print(next(a)) # (nothing)

print()

class FRange:

    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(0, 2, 0.5)
# print(next(fr)) # 0.0
# print(next(fr)) # 0.5
# print(next(fr)) # 1.0
# print(next(fr)) # 1.5
# print(fr.__next__()) # StopIteration

for x in fr:
    print(x)

print()

class FRange2D:

    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration

fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=' ')
    print()

class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration


g = GeomRange(1, 1.2, 2)

res = next(g)
print(res)
res = next(g)
print(res)

print('*************************************************')

class Person:
     
    def __init__(self, fio: str, job: str, old: int, salary, year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.data = tuple(self.__dict__)
        self.indx = 0

    def check_indx(self, i):
        if not (isinstance(i, int) and 0 <= abs(i) <= 4):
            raise IndexError('неверный индекс')

    def __getitem__(self, indx):
        self.check_indx(indx)
        return getattr(self, self.data[indx])

    def __setitem__(self, indx, value):
        self.check_indx(indx)
        setattr(self, self.data[indx], value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indx < len(self.data):
            ret_i = self.indx
            self.indx += 1
            return getattr(self, self.data[ret_i])
        raise StopIteration

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)

print('*************************************************')

class TriangleListIterator:

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j] # почти то же, что и return, только для итераторов

ls = [['1', 0], [2, 3,], [4, 5, 6], ['7', 8, '9', 10]]
ls_one = [x for row in ls for x in row]

t = TriangleListIterator(ls)
it = iter(t)
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3

print('*************************************************')

class IterColumn:

    def __init__(self, lst, column: int):
        self.lst = lst
        self.col = column

    def __iter__(self):
        for row in range(len(self.lst)):
            yield self.lst[row][self.col]


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:
    print(x)

print('*************************************************')

class StackObj:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Stack:

    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __iter__(self):
        top = self.top
        while top:
            yield top
            top = top.next

    def __len__(self):
        return sum(1 for _ in self)

    def obj(self, indx):
        if not (type(indx) is int and 0 <= indx < len(self)):
            raise IndexError('неверный индекс')
        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, indx):
        return self.obj(indx).data

    def __setitem__(self, indx, value):
        self.obj(indx).data = value

st = Stack()
st.push_back(StackObj("2"))
st.push_front(StackObj("2"))
st.push_back(StackObj("3"))

st[0] = 1 # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[1]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека
print(data, n)

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

print('*************************************************')

class Cell:
    
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self): return self.__data
    @data.setter
    def data(self, value): self.__data = value

class TableValues:

    def __init__(self, rows, cols, type_data=int):
        self.type_data = type_data
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))

    def check_indx(self, i):
        i, j = i
        if not (0 <= i < self.rows) or not (0 <= j < self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, indx):
        self.check_indx(indx)
        i, j = indx
        return self.cells[i][j].data

    def __setitem__(self, indx, value):
        self.check_indx
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        i, j = indx
        self.cells[i][j].data = value

    def __iter__(self):
        for row in self.cells:
            yield (x.data for x in row)

table = TableValues(2, 2)
table[0, 0] = 1
table[0, 1] = 2
table[1, 0] = 3
table[1, 1] = 4
for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()

print('*************************************************')

class Matrix:

    def __init__(self, rows_or_lst, cols=0, fill_value=0):
        if type(rows_or_lst) == list:
            self.rows = len(rows_or_lst)
            self.cols = len(rows_or_lst[0])
            if not all(len(r) == self.cols for r in rows_or_lst) or \
                not all(self.is_digit(x) for row in rows_or_lst for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')

            self.lst = rows_or_lst
        else:
            if type(rows_or_lst) != int or type(cols) != int or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self.rows = rows_or_lst
            self.cols = cols
            self.lst = [[fill_value for _ in range(cols)] for _ in range(rows_or_lst)]
    
    @staticmethod
    def is_digit(x):
        return type(x) in (int, float)        

    def check_indx(self, indx):
        i, j = indx
        if not (0 <= i < self.rows) or not (0 <= j < self.cols):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, indx):
        self.check_indx(indx)
        i, j = indx
        return self.lst[i][j]

    def __setitem__(self, indx, value):
        self.check_indx(indx)
        if not self.is_digit(value):
            raise TypeError('значения матрицы должны быть числами')

        i, j = indx
        self.lst[i][j] = value

    def check_dim(self, m):
        rows, cols = m.rows, m.cols
        if self.rows != rows or self.cols != cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if type(other) == type(self):
            self.check_dim(other)
            return Matrix([[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(other) == type(self):
            self.check_dim(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.is_digit(other)
            return Matrix([[self[i, j] - other for j in range(self.cols)] for i in range(self.rows)])

mt = Matrix([[1, 2], [3, 4]])
print(mt[0, 0]) # 1
print(mt[0, 1]) # 2
print(mt[1, 0]) # 3
print(mt[1, 1]) # 4

print('*************************************************')

from random import randint

class TicTacToe:

    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    def __init__(self):
        self.size = 3
        self.win = 0 # 0 - игра; 1 - победа чел; 3 - победа комп; 4 - ничья
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

        self.win = 0

    def check(self, indx):
        if type(indx) not in (tuple, list) or len(indx) != 2:
            raise IndexError('некорректно указанные индексы')

        i, j = indx
        if not (0 <= i < self.size) or not (0 <= j < self.size):
            raise IndexError('некорректно указанные индексы') 

    def update_win_status(self):
        # проверка по строкам
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self.win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self.win = 2
                return

        # проверка по столбцам
        for i in range(self.size): 
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self.win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self.win = 2
                return  

        # проверка по диагоналям
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self.size)) or \
            all(self.pole[i][-1-i].value == self.HUMAN_X for i in range(self.size)):
            self.win = 1
            return

        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self.size)) or \
            all(self.pole[i][-1-i].value == self.COMPUTER_O for i in range(self.size)):
            self.win = 2
            return

        # проверка на ничью
        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self.win = 3
         
    def __setitem__(self, indx, value):
        self.check(indx)
        i, j = indx
        self.pole[i][j].value = value

        self.update_win_status()
        
    def __getitem__(self, indx):
        self.check(indx)
        i, j = indx
        return self.pole[i][j].value

    # отображение текущего состояния игрового поля (как именно - на свое усмотрение)
    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if x.value == 0 else x.value, row))
        print()

    # реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик)
    def human_go(self):
        if not self:
            return

        while True:
            i, j = map(int, input('Введите координаты клетки: ').split())
            if not (0 <= i < self.size) or not (0 <= j < self.size):
                continue
            if self[i, j] == self.FREE_CELL:
                self[i, j] = self.HUMAN_X
                break
    
    # реализация хода компьютера (ставит случайным образом нолик в свободную клетку)
    def computer_go(self): 
        if not self:       
            return

        while True:
            i = randint(0, self.size-1)
            j = randint(0, self.size-1)
            if self[i, j] != self.FREE_CELL:
                continue
            self[i, j] = self.COMPUTER_O
            break


    @property # возвращает True, если победил человек
    def is_human_win(self):
        return self.win == 1

    @property #  возвращает True, если победил компьютер
    def is_computer_win (self):
        return self.win == 2

    @property # возвращает True, если ничья
    def is_draw (self):
        return self.win == 3

    # возвращает True, если игра не окончена 
    # (никто не победил и есть свободные клетки) 
    def __bool__(self):
        return self.win == 0 and self.win not in (1, 2, 3)

class Cell:

    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0



game = TicTacToe()
game.init()
step_game = 0

while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")