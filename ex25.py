'''
Введение в обработку исключений. Блоки try / except.

Исключения в процессе выполнения
исключения в процессе компиляции (до исполнения кода)

'''

try:
    f = open('Descriptor2.py')
except FileNotFoundError:
    print('Невозможно открыть файл')

    
try:
    x, y = 1, 0#map(int, input().split())
    res = x / y
except ValueError:
    print('Ошибка типа данных')
except ArithmeticError:
    print('Деление на 0!')


print('\nШтатное завершение')

print('*************************************************')

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

pt = Point(1, 2)

try:
    print(pt.z)
except AttributeError:
    # при обращении к несуществующему атрибуту генерируется исключение AttributeError.
    print("Атрибут с именем z не существует")

print('*************************************************')

l = "8 11 abcd -7.5 2.0 -5"
lst_in = list(l.split())

print(sum(map(int, filter(lambda x: x.strip('-').isdigit(), lst_in))))

print('*************************************************')

l = '1 -5.6 True abc 0 23.56 hello'
lst_in = l.split()

def func(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

lst_out = list(map(func, lst_in))
print(lst_out)

print('*************************************************')

class Triangle:

    def __init__(self, a, b, c):
        
        self._a = a
        self._b = b
        self._c = c

        if (a + b < c) or (a + c < b) or (b + c < a):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


    def __setattr__(self, name, value):
        if name in ('_a', '_b', '_c'):
            if type(value) not in (int, float) or value <= 0:
                raise TypeError('стороны треугольника должны быть положительными числами')
            object.__setattr__(self, name, value)


    def __str__(self):
        return f'{self._a}, {self._b}, {self._c}'


def create_triangle(x):
    try:
        return Triangle(*x)
    except:
        return False

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)] 

lst_tr = list(map(lambda x: Triangle(*x), filter(create_triangle, input_data)))

for x in lst_tr:
    print(x)

print('*************************************************')

class FloatValidator:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) is not float or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class IntegerValidator:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) is not int or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    res = []
    for value in lst:
        for valid in validators:
            try:
                valid(value)
                res.append(value)
                break
            except ValueError:
                pass

    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)