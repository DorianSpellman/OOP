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
from unicodedata import digit

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

print('*************************************************')

class ImageFileAcceptor:
    
    def __init__(self, extensions: tuple):
        self.extensions = extensions # ('jpg', 'bmp', 'jpeg')

    def __call__(self, filename, *args, **kwargs):
        #print(filename)
        # if filename.split('.')[1] in self.extensions:
        #     return True
        return filename.endswith(self.extensions)


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))

image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

print('*************************************************')

from string import ascii_letters, ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
        
    def post(self, request):
        self.login = request.get('login', "Error")
        self.password = request.get('password', "Error")
        
    def is_validate(self):
        if not self.validators:
            return False
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
            
        return True


class LengthValidator:

    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string):
        return self.min_length <= len(string) <= self.max_length


class CharsValidator:

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return set(string).issubset(set(self.chars))

lv = LengthValidator(5, 15)
cv = CharsValidator(ascii_letters + digits)
res_len = lv('apple123')
res_chars = cv('apple123')
print(res_len, res_chars) # True True


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "apple123"})
print(lg.login, lg.password)
if lg.is_validate():
     print("Дальнейшая обработка данных формы")


print('*************************************************')

class DigitRetrieve:

    def __call__(self, string):
        if string[1:].isdigit() and string[0] == '-':
            return int(string)
        if string.isdigit():
            return int(string)
        return None

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)

print('*************************************************')

class RenderList:

    def __init__(self, type_list):
        self.tl = 'ol' if type_list == 'ol' else 'ul'

    def __call__(self, lst):
        start = f'<{self.tl}>\n'
        finish = f'</{self.tl}>'
        main = ''
        for point in lst:
            main += '<li>' + point + '</li>\n'
        return start + main + finish
 
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)

print('*************************************************')

class HandlerGET:

    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args): # при вызове декор. ф-ии будет вызываться метод call
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'


@HandlerGET
def contact(request):
    return "Page has been loaded"

    
res = contact({"method": "GET", "url": "contact.html"})
print(res)    # GET: Page has been loaded
res = contact({"method": "POST", "url": "contact.html"})
print(res)    # None
res = contact({"url": "contact.html"})
print(res)    # GET: Page has been loaded

print('*************************************************')

class Handler:

    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func): 
        def wrapper(request):
            m = request.get('method', 'GET')
            if m in self.methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper

    def get(self, func, request):
        return f'GET: {func(request)}'

    def post(self, func, request):
        return f'POST: {func(request)}'

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Page has been loaded"

@Handler(methods=('POST'))
def index(request):
    return "index"

print(index({'method':'GET'})) # None
print(contact({'method':'GET'}))

print('*************************************************')

class InputDigits:

    def __init__(self, func):
        self.func = func

    def __call__(self):
        return list(map(int, self.func().split()))

@InputDigits
def input_dg():
    return input()
res = input_dg()

print(res)

print('*************************************************')

class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper():
            return list(map(self.render, func().split()))
        return wrapper
        
class RenderDigit:

    def __call__(self, dig):
        try:
            return int(dig)
        except ValueError:
            return None

@InputValues(render=RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)
