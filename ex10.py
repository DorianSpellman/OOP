'''
Магический метод __call__. Функторы и классы-декораторы
dunder-методы (от англ. double underscore - двойное подчеркивание)

При создании объекта класса (написании "()" ) вызывается метод __call__:
__call__(self, *args, **kwargs):
    obj = self.__new__(self, *args, **kwargs)
    self.__init__(obj,  *args, **kwargs)
    return obj


'''

class Counter:

    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwds):
        self.__counter += step
        #print(f'{self}: {self.__counter}')
        return self.__counter

c = Counter() # 0
c2 = Counter() # 0

c() # 1
c(2) # 3

res = c(10) # 13
res2 = c2(-5) # 1
print(res, res2)

print('*************************************************')

class StripChars:

    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')

        return args[0].strip(self.__chars)

s1 = StripChars('?:!.; ')
res = s1(' Hello World!..')
print(res)

print('*************************************************')

from math import *

class Derivate:

    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate    
def f_sin(x):
    return sin(x)

#f_sin = Derivate(f_sin) # теперь f_sin ссылается не на ф-ию f_sin, а на объект класса
print(f_sin(pi/3))

print('*************************************************')

from random import *

class RandomPassword:

    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwds):
        password = ''
        for _ in range(randint(self.min_length, self.max_length)):
            password += choice(self.psw_chars)
        return password

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)

lst_pass = [rnd() for _ in range(3)]
print(lst_pass)


    