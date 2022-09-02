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