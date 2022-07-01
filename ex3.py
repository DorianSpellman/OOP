from random import *
import string


class Point:

    color = 'red'
    circle = 2
    i = 1

    def __init__(self, x=0, y=0, color='black'): # initialization when creating an object
        self.x = x
        self.y = y
        self.color = color
    
    # def __del__(self):
    #     print(Point.i, 'object has deleted successful')
    #     Point.i += 1
        

    def set_coords(self, x, y):
        self.x = x  # creating local property 
        self.y = y  # of the object

    def get_coords(self):
        return (self.x, self.y) # return tuple with coords


pt = Point(1, 1, 'red')    # creating objects of the class
pt2 = Point(y=5)

print('pt:  ', pt.__dict__)         # pt:   {'x': 3, 'y': 3}
print('pt2: ', pt2.__dict__)        # pt2:  {'x': 5, 'y': 5}

print('pt:  ', pt.get_coords())     # pt:   (3, 3)
print('pt2: ', pt2.get_coords())    # pt2:  (5, 5)


points = [Point(i, i) for i in range(1, 10, 2)]

points[1].color = 'yellow'

for pt in points:
    print(pt.__dict__)

print('*************************************************')

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
    
class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
    
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
    
'''
Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (Line или Rect или Ellipse). 
Координаты также генерируются случайным образом.
'''
classes = [Line, Rect, Ellipse]
elements = [choice(classes)(*list(map(int, sample(string.digits, 4)))) for i in range (5)]

for el in elements:
    if isinstance(el, Line):
        el.ep = (0, 0)
        el.sp = (0, 0)

for q in elements:
    print(q.__dict__)

print('*************************************************')

# class TriangleChecker:
    
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def is_triangle(self):
#         if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
#             return 1 # any side is not digit
#         if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
#             return 1 # any side is < or = 0

#         if (self.a + self.b) <= self.c or (self.a + self.c) <= self.b or (self.b + self.c) <= self.a:
#             return 2 # not triangle

#         return 3 # True

# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())

print('*************************************************')

# class Graph:

#     def __init__(self, data, is_show=True):
#         self.data = data.copy()
#         self.is_show = is_show

#     def set_data(self, data): # - для передачи нового списка данных в текущий график
#         self.data = data
                
#     def show_table(self): # - для отображения данных в виде строки из списка чисел (числа следуют через пробел)
#         if self.is_show is False:
#             print('Отображение данных закрыто')
#         else:
#             print(*self.data)

#     def show_graph(self): # - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
#         if self.is_show is False:
#             print('Отображение данных закрыто')
#         else:
#             print('Графическое отображение данных:', *self.data)
    
#     def show_bar(self): #- для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
#         if self.is_show is False:
#             print('Отображение данных закрыто')
#         else:
#             print('Столбчатая диаграмма:', *self.data)
    
#     def set_show(self, fl_show): #- метод для изменения локального свойства is_show на переданное значение fl_show.
#         self.is_show = fl_show

         
# data_graph = list(map(int, input().split()))
# gr_1 = Graph(data_graph)
# gr_1.show_bar()
# gr_1.set_show(False)
# gr_1.show_table()

print('*************************************************')

class CPU:

    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
     
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu #link to object of the class CPU
        self.total_mem_slots = 4
        self.mem_slots = mems[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: ' + '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]

mb = MotherBoard('Gerald', CPU('Intel', 2000), Memory('Jojo', 256), Memory('Siao', 512))

print(mb.get_config())

print('*************************************************')

class Cart:

    def __init__(self, goods=[]):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, ind):
        self.goods.pop(ind)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]

    
class Table:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook :

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup :

    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()

tv1 = TV("Samsung", 50000)
tv2 = TV("LG", 25000)
table = Table("IKEA", 5000)
n1= Notebook("Acer", 60000)
n2 = Notebook("Apple", 100000)
c = Cup("Luminarc", 500)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)

print(cart.get_list())

print('*************************************************')

class ListObject:

    def __init__(self, data, next_obj = None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj

lst_in = ['1 string', '2 string', '3 string']

head_obj = ListObject(lst_in[0])
obj = head_obj
lst = []

for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    lst.append(obj)
    obj = obj_new
    

for i in lst:
    print(i.__dict__)
