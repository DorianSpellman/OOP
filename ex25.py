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

