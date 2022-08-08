'''
Магические методы __add__, __sub__, __mul__, __truediv__
__add__() - +
__sub__() - -
__mul__() - *
__truediv__() - /
__floordiv__() - //
__mod__() - %
__i...__() - += -= ...
'''

class Clock:

    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds % self.__DAY # чтобы кол-во секунд не превысило кол-во секунд в 1 дне

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}'

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть int/Clock')
        s = other # ссылается на число или экз. класса
        if isinstance(other, Clock):
            s = other.seconds 
        return Clock(self.seconds + s) # создаётся новый экземпляр класса

    def __radd__(self, other): # сложение число + объект (число справа)
        return self + other # переход в __add__()

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть int/Clock')
        s = other 
        if isinstance(other, Clock):
            s = other.seconds 

        self.seconds += s
        return self

c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
c4 = c1 + c2 + c3
print(c4.get_time())

c1 = c1 + 100 # c1 присваивается новый экземпляр класса, прежний объект автоматически удаляется сборщиком мусора
c1 += 10
print(c1.get_time())

print('*************************************************')

class Way:
    def __init__(self, length):
        self.length = length

    def __add__(self, other):
        return Way(self.length + other.length)

    def __str__(self) -> str:
        return f'{self.length}'

w1 = Way(5)
w2 = Way(10)
w = w1 + w2 + w1
print(w)
w1 += w2 # Если метод __iadd__ не определён, то используется __add__ для +=
print(w1)

print('*************************************************')

class NewList:

    def __init__(self, list=[]):
        self.list = list

    def __sub__(self, value):
        v = value
        new_list = list()

        if isinstance(v, NewList):
            v = value.list.copy()

        for i in self.list:
            if str(i) not in list(map(str, v)):
                new_list.append(i)
            else: # если значение есть в обоих списках
                v.remove(i)
                
        return NewList(new_list)

    def __rsub__(self, value):
        sub_list = self.list.copy()

        if type(value) is list:
            new_list = list()
            
            for i in value:
                if str(i) not in list(map(str, sub_list)):
                    new_list.append(i)
                else:
                    sub_list.remove(i)
                
        return NewList(new_list)

    
    def get_list(self):
        return self.list

    def __str__(self):
        return f'{self.list}'


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 
print(res_1) # NewList: [-4, 6, 10, 11, 15, False]

lst1 -= lst2 
print(lst1) # NewList: [-4, 6, 10, 11, 15, False]

res_2 = lst2 - [0, True] 
print(res_2) # NewList: [1, 2, 3]

res_3 = [1, 2, 3, 4.5] - res_2 
print(res_3) # NewList: [4.5]

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4)

print('*************************************************')

class ListMath:

    def __init__(self, lst=[]):
         self.lst_math = list(filter(lambda x: type(x) in (int, float), lst))

    def __str__(self) -> str:
        return f'{self.lst_math}'

    @staticmethod
    def __verify(value):
        if type(value) not in (int, float):
            raise ArithmeticError('Операнд должен быть числом')

    ###### add ######

    def __add__(self, value): # сложение каждого числа списка с определенным числом
        self.__verify(value)
        new = [i + value for i in self.lst_math]
        return ListMath(new)

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        self.__verify(value)
        self.lst_math = [i + value for i in self.lst_math]
        return self

    ###### sub ######

    def __sub__(self, value): # вычитание из каждого числа списка определенного числа
        self.__verify(value)
        new = [i - value for i in self.lst_math]
        return ListMath(new)

    def __rsub__(self, value):
        new = [value - i for i in self.lst_math]
        return ListMath(new)

    def __isub__(self, value):
        self.__verify(value)
        self.lst_math = [i - value for i in self.lst_math]
        return self

    ###### mul ######

    def __mul__(self, value): # умножение каждого числа списка на указанное число
        self.__verify(value)
        new = [i * value for i in self.lst_math]
        return ListMath(new)

    def __rmul__(self, value):
        return self * value

    def __imul__(self, value):
        self.__verify(value)
        self.lst_math = [i * value for i in self.lst_math]
        return self

    ###### div ######

    def __truediv__(self, value): # деление каждого числа списка на указанное число
        self.__verify(value)
        new = [i / value for i in self.lst_math]
        return ListMath(new)

    def __rtruediv__(self, value):
        new = [value / i for i in self.lst_math]
        return ListMath(new)

    def __itruediv__(self, value):
        self.__verify(value)
        self.lst_math = [i / value for i in self.lst_math]
        return self



lst = ListMath([1, "abc", -2, 3.5, True]) # [1, -2, 3.5]

lst = lst + 10 # [11, 8, 13.5]
lst = 5 + lst # [16, 13, 18.5]
lst += 4 # [20, 17, 22.5]

lst = lst - 4 # [16, 13, 18.5]
lst = 20.0 - lst # [4.0, 7.0, 1.5]
lst -= 1 # [3.0, 6.0, 0.5]

lst = lst * 2 # [6.0, 12.0, 1.0]
lst = 2 * lst # [12.0, 24.0, 2.0]
lst *= 10.5 # [126.0, 252.0, 21.0]

lst = lst / 10.5 # [12.0, 24.0, 2.0]
lst = 36 / lst # [3.0, 1.5, 18.0]
lst /= 0.5 # [6.0, 3.0, 36.0]

print(lst)

print('*************************************************')

# односвязный список

class StackObj:

    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:

    def __init__(self, top=None):
        self.top = top
        self.__last = None # ссылка на последний объект списка

    def push_back(self, obj): # добавление объекта класса StackObj в конец односвязного списка
        if self.top is None:
            self.top = obj

        if self.__last: # если последний объект есть
            self.__last.next = obj # следующий за последним объектом
        
        self.__last = obj

    def pop_back(self): # удаление последнего объекта из односвязного списка
        top = self.top
        if top is None: # если в списке нет объектов
            return
        
        while top.next and top.next != self.__last: # пока ссылка на следующий объект != None И следующий != последнему (доходим до предпоследнего объекта)
            top = top.next

        if self.top == self.__last: # если это ед. объект в списке (первый и последний совпадают)
            self.top = self.__last = None

        else:
            top.next = None
            self.__last = top

    def __add__(self, obj):
        self.push_back(obj)
        return self

    def __iadd__(self, obj):
        return self.__add__(obj)

    def __mul__(self, obj):
        for x in obj:
            self.push_back(StackObj(x))
        return self

    def __imul__(self, obj):
        return self.__mul__(obj)

    def show(self):
        outs = ''
        current = self.top
        if not current: return None

        while current.next:
            outs += f'{current.data} -> '
            current = current.next
        outs += current.data
        print(outs)



h = StackObj('5')
print(h._StackObj__data) # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st.show() # 1 -> 2 -> 3
st = st + StackObj('4')
st += StackObj('5')
st.show() # 1 -> 2 -> 3 -> 4 -> 5
st = st * [str(i) for i in range(6, 9)]
st *= [str(i) for i in range(9, 12)]
st.show() # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11


print('*************************************************')

class Book:

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f'"{self.title}"'

class Lib:

    def __init__(self):
        self.book_list = list()

    def __add__(self, book):
        self.book_list.append(book)
        return self

    def __sub__(self, book):
        if isinstance(book, Book):
            if book in self.book_list:
                self.book_list.remove(book)
                                        
        if isinstance(book, int):
            if book < self.__len__():
                self.book_list.pop(book)
        
        return self

    def __len__(self):
        return len(self.book_list)

    def __str__(self) -> str:
        books = ''
        for i in self.book_list:
            books += i.title + ' | '
        return books + f'\n------'

lib = Lib()
book1 = Book('Процесс', 'Кафка', 2020)
book2 = Book('Три товарища', 'Ремарк', 2021)
book3 = Book('Бесы', 'Достоевский', 2022)
book4 = Book('1984', 'Оруэлл', 2022)

lib = lib + book1 # добавление новой книги в библиотеку
lib += book2
lib += book3
lib += book4
print(lib)

lib = lib - book1 # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book2
print(lib)

lib = lib - 1 # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= 0
print(lib)

print('*************************************************')

class Item:

    def __init__(self, name, money):
        self.name = name
        if type(money) in (int, float):
            self.money = money
    
    def __add__(self, item):
        if type(item) == Item:
            return self.money + item.money
            
        if type(item) in (int, float):
            return item + self.money              

    def __radd__(self, item):
        return self + item

class Budget:

    def __init__(self):
        self.budget = []
    
    def add_item(self, item):
        self.budget.append(item)

    def remove_item(self, indx):
        del self.budget[indx]

    def get_items(self):
        return self.budget

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)

print('*************************************************')

class Box3D:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __str__(self) -> str:
        return f'w={self.width} h={self.height} d={self.depth}'

    def __add__(self, other):
        w = self.width + other.width
        h = self.height + other.height
        d = self.depth + other.depth
        return Box3D(w, h, d)

    def __sub__(self, other):
        w = self.width - other.width
        h = self.height - other.height
        d = self.depth - other.depth
        return Box3D(w, h, d)

    def __mul__(self, num):
        w = self.width * num
        h = self.height * num
        d = self.depth * num
        return Box3D(w, h, d)

    def __rmul__(self, num):
        return self * num

    def __floordiv__(self, num):
        w = self.width // num
        h = self.height // num
        d = self.depth // num
        return Box3D(w, h, d)

    def __mod__(self, num):
        w = self.width % num
        h = self.height % num
        d = self.depth % num
        return Box3D(w, h, d)    

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9
print(box)
box = box2 - box1 # Box3D: width=1, height=2, depth=3
box = box1 * 2    # Box3D: width=2, height=4, depth=6
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box1 // 2   # Box3D: width=0, height=1, depth=1 
box = box2 % 3    # Box3D: width=2, height=1, depth=0
print(box)

print('*************************************************')

class MaxPooling:

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step # шаг смещения окна по Г и В
        self.size = size  # размер окна

    def __call__(self, matrix):
        if not all(map(lambda x: len(x) == len(matrix), matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")
        for i in matrix:
            for j in i:
                if type(j) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")
        else:
            row_step = self.step[0] # 2 
            col_step = self.step[1] # 2

            row_size = self.size[0] # 2
            col_size = self.size[1] # 2
 
            result_table = list()

            for i in range(0, len(matrix), row_step):
                result_row = list()

                for j in range(0, len(matrix[0]), col_step): # проходимся по строкам
                    if i+row_size <= len(matrix) and j+col_size <= len(matrix[0]): 
                        window = [x for row in matrix[i:i+row_size] for x in row[j:j+col_size]] # матрицу подгоняем под удобную для работы с нужным размером окна
                        #print(max(window))
                        result_row.append(max(window)) # добавляем наибольшее значение в окне в список строки
                if result_row:
                    #print(result_row)
                    result_table.append(result_row)

            return result_table
                    

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 8, 7, 6], 
          [5, 4, 3, 2]])    

print(res) # [[6, 8], [9, 7]]


