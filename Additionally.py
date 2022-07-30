'''
Замыкания
'''

# Example 1

def say_name(name: str): # возвращает say_goodbye, сохраяняя в локальное окружение name

    def say_goodbye(): # печатает строку, используя name внешнего окружения
        print("Don't say me goodbye, " + name + "!")

    return say_goodbye

f = say_name('Ralf')
f2 = say_name('Meggi')
f()
f2()
print(f'-------------- \nExample 2 \n--------------')

# Example 2

def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step

c1 = counter(10)
c2 = counter()
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())

print(f'-------------- \nExample 3 \n--------------')

def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip

strip1 = strip_string()
strip2 = strip_string(" !&,.")

print(strip1('  Hello, Jerry!'))
print(strip2('..Hello, Jerry!'))
print(f'-------------- \nДекораторы: \n--------------')

'''
Декораторы функций
'''

from doctest import testfile
import time

def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs) # get_nod(2, 100000)
        et = time.time()
        dt = et - st
        print(f'Время работы: {dt} сек')

        return res

    return wrapper

@test_time
def get_nod(a, b): # Наим. Общ. Делит.
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a

@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    
    return a

#get_nod = test_time(get_nod)
#get_fast_nod = test_time(get_fast_nod)

res = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)
print(res)
print(res2)

