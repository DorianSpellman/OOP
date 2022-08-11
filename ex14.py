'''
Магические методы __eq__ и __hash__
hash можно вычислить только для неизменяемых объектов

Если объекты a == b, то равны их хэши
Равные хэши: hash(a) == hash(b) не гарантируют равенство объектов
Если хэши не равны: hash(a) != hash(b), то объекты точно не равны
'''

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other): # если определеён этот метод, то hash перестаёт работать
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int: # для этого переопределяется метод hash в классе
        return hash((self.x, self.y)) # вычисляется хэш от координат, если они равны, то равны и хэши

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
print(hash(p1), hash(p2), sep='\n')

d = {}
d[p1] = 1
d[p2] = 2
print(d)

a = 5
b = 5
c = 'string'
print(hash(a) == hash(b))

print('*************************************************')

class Rect:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self) -> int:
        return hash((self.width, self.height))

    
r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2
print(hash(r1), hash(r2), sep='\n')

print('*************************************************')

class ShopItem:

    def __init__(self, name: str, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

lst_in = ['Системный блок: 1500 75890.56', 
        'Монитор Samsung: 2000 34000', 
        'Клавиатура: 200.44 545', 
        'Монитор Samsung: 2000 34000']
shop_items = dict()

for line in lst_in:
    name = str(line.split(':')[0])
    weight = line.split()[-2]
    price = line.split()[-1]
    obj = ShopItem(name, weight, price)
    shop_items.setdefault(obj.name, [obj, 0])[1] += 1
    # total = 1
    # if obj in shop_items: # если такой же объект есть в словаре
    #     shop_items[obj][1] += 1
    # else:         
    #     shop_items[obj] = [obj, total]

print(shop_items, sep='\n')
print(len(shop_items))

print('*************************************************')

class DataBase:

    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        for values in self.dict_db.values():
            for obj in values:
                if obj.pk == pk:
                    return obj

        r = (x for row in self.dict_db.values() for x in row)
        print(r)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None

class Record:
    pk = 0

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.__pk()

    @classmethod
    def __pk(cls):
        cls.pk += 1
        return cls.pk

    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = ['Балакирев С.М.; программист; 33', 
        'Кузнецов А.В.; разведчик-нелегал; 35', 
        'Суворов А.В.; полководец; 42', 
        'Иванов И.И.; фигурант всех подобных списков; 26',
        'Балакирев С.М.; преподаватель; 37']

db = DataBase('database.db')

for line in lst_in:
    args = list(map(str.strip, line.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))

print(db.read(1).__dict__)

print('*************************************************')

class BookStudy:

    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author 
        self.year = year

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.author.lower()))


lst_in = ['Python; Балакирев С.М.; 2020',
        'Python ООП; Балакирев С.М.; 2021',
        'Python ООП; Балакирев С.М.; 2022',
        'Python; Балакирев С.М.; 2021']

lst_bs = list()

for book in lst_in:
    args = list(map(str.strip, book.split(';')))
    args[-1] = int(args[-1])
    book_study = BookStudy(*args)
    lst_bs.append(book_study)

unique_books = len(set(hash(book) for book in lst_bs))

print(unique_books)

print('*************************************************')

class Dimensions:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))

    def __setattr__(self, name, value):
        if value <= 0:
            raise ValueError("Габаритные размеры должны быть положительными числами")
        object.__setattr__(self, name, value)
        

s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"

lst_dims = [(Dimensions(*map(float, dim.split())) for dim in s_inp.split(';'))]
lst_dims.sort(key=hash)
for i in lst_dims:
    print(*i)

print('*************************************************')

class Triangle:

    def __init__(self, a, b, c):
        if not (a < b + c) and (b < a + c) and (c < a + b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        else:
            self.a = a
            self.b = b
            self.c = c
    
    def __setattr__(self, name, value):
        if type(value) in (int, float) and value > 0:
            object.__setattr__(self, name, value)
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __len__(self):
        P = self.a + self.b + self.c
        return int(P)

    def __call__(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

tr = Triangle(3, 4, 5)
print(len(tr)) # perimeter
print(tr()) # square
    