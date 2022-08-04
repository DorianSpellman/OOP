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


