'''
Обработка исключений. Блоки finally и else.

Блок else выолняется, если выполнилось try
finally выполняется всегда

Обработка исключений должна происходить в следующем порядке:
try/except/else/finally

'''

try:
    a, b = 5, 10
    c = 2
    res = (a + b) / c
except ZeroDivisionError as z:
    print(z)
except:
    print('Другая ошибка')
else:
    print(res)
finally:
    print('Блок finally выполняется всегда')

print('*************************************************')

def get_values():
    try:
        x, y = 5, 7
        return x, y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print('finally выполняется до return')

x, y = get_values()
print(x, y)

print('*************************************************')

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на ноль')

try:
    a, b = 5, 0
    res = div(a, b)
except ValueError as v:
    print(v)
else:
    print(res)

print('*************************************************')

a, b = 1.0, 3.5#input().split()
try:
    res = int(a) + int(b)
except:
    try: 
        res = float(a) + float(b)
    except:
        res = a + b
finally:
    print(res)

print('*************************************************')

class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

x, y = 5, 10#input().split()

try:
    pt = Point(int(x), int(y))
except:
    pt = Point()
finally:
    print(f'Point: x = {pt._x}, y = {pt._y}')

print('*************************************************')

def get_div(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        res = 100
        return res
    finally:
        res = -1
        print(f"finally: {res}")

# ф-ия возвратит одно, напечатает другое: res не переопределится
print(get_div(1, 2)) 
# finally: -1
# 0.5 (return)
print(get_div(1, 0)) 
# finally: -1
# 100 (return)

print('*************************************************')

def get_loss(w1, w2, w3, w4):
    try:
        x = w1 // w2
    except ZeroDivisionError:
        return f'деление на ноль'
    else:
        y = 10 * x - 5 * w2 * w3 + w4
        return y

print('*************************************************')

class Rect:

    def __init__(self, x, y, width, height):
        if not ( isinstance(x, (int, float)) and isinstance(y, (int, float)) and width > 0 and height > 0):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height
    
        self.lower = self._x + self._width
        self.right = self._y + self._height

    def is_collision(self, rect): 
        if not isinstance(rect, Rect):
            raise TypeError('аргументом должен быть объект класса Rect')

        if not (self.lower < rect._x or rect.lower < self._x or \
            self.right < rect._y or rect.right < self._y ):
            raise TypeError('прямоугольники пересекаются')

lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

def is_collision(rect1, rect2):
    try:
        rect1.is_collision(rect2)
    except TypeError:
        return True
    return False

lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))
                        if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]

print(lst_not_collision)
