'''
Распространение исключений (propagation exceptions)

Распространение исключений происходит на всех этапах исполнения. 
Перехватывать исключения правильнее на глобальном уровне, не мешая внутренней структуре 
'''

def func1():
    try:
        return 1 / 0
    except:
        print('Error 1')

def func2():
    try:
        return func1()
    except:
        print('Error 2')

try:
    func2()
except:
    print('Error 3')

print('*************************************************')

class Geom:
    def __init__(self, width, color):
        if type(width) not in (int, float) or type(color) != str or width < 0:
            raise ValueError('неверные параметры фигуры')

        self._width = width
        self._color = color


class Ellipse(Geom):
    def __init__(self, x1, y1, x2, y2, width=1, color='red'):
        super().__init__(width, color)

        if not self._is_valid(x1) or not self._is_valid(y1) or not self._is_valid(x2) or not self._is_valid(y2):
            raise ValueError('неверные координаты фигуры')

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def _is_valid(self, x):
        return type(x) in (int, float)

try:
    x1, y1, x2, y2, w = 1, 2, 3, 4, '5'#map(float, input().split())
    el = Ellipse(x1, y1, x2, y2, w)
except ValueError as e:
    print(e)

print('*************************************************')

def input_int_numbers():
    return tuple(map(int, input().split()))

while True:
    try:
        print(*input_int_numbers())
        break
    except:
        continue

print('*************************************************')

class ValidatorString:

    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if not self.min_length <= len(string) <= self.max_length or \
            self.chars and not any(char in self.chars for char in string):
                raise ValueError('недопустимая строка')
        return string
    
class LoginForm:

    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = self._password = None

    def form(self, request):
        if not request.get('login') or not request.get('password'):
            raise TypeError('в запросе отсутствует логин или пароль')
        
        self._login = self.login_validator.is_valid(request.get('login'))
        self._password = self.password_validator.is_valid(request.get('password'))



login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(8, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)

login, password = input().split()

try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)