'''
Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__

Магические методы - методы с двумя нижними подчеркиваниями до и 
после имени метода, которые автоматически вызываются 
в определенных для них ситуациях.

__setattr__(self, key, value) - авт вызывается при изменении свойства key класса
__getattribute__(self, item) - авт вызывается при получении свойства класса с именем item
__getattr(self, item) - авт вызывается при получении несуществующего свойства item класса
__delattr__(self, item) - авт вызывается при удалении свойства item
'''

class Point:

    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Доступ к переменной запрещён')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key in ('x', 'y'):
            object.__setattr__(self, key, value)
        else:
            raise AttributeError('Недопустимое имя')            

    def __getattr__(self, item):
        print(f'Несуществующий атрибут "{item}"')

    def __delattr__(self, item):
        object.__delattr__(self, item)
        print(f'{item} успешно удалён!')        


p1 = Point(1, 1)
p2 = Point(2, 2)

#try1 = p1.x #ValueError: Доступ к переменной запрещён
print(p1.y) # OK

p1.x = 5
#p1.z = 0 # AttributeError: Недопустимое имя
p1.yy # Несуществующий атрибут "yy"

del p2.y

print('*************************************************')

class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author') and type(value) is str:
            object.__setattr__(self, key, value)
        elif key in ('pages', 'year') and type(value) is int:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Singing in the thorn', 'Colleen McCullough', 650, 1977)

print(book.__dict__)

print('*************************************************')

class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    
    __ID = 1
    attrs = {'id' : (int,),
             'name' : (str,),
             'weight' : (int, float),
             'price' : (int, float)
             }

    def __init__(self, name, weight, price):
        self.id = Product.__ID
        self.name = name
        self.weight = weight
        self.price = price
        Product.__ID += 1
    
    def __setattr__(self, name, value):
        if type(value) not in self.attrs[name] or (name in ('weight', 'price') and value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, name, value)         

    def __delattr__(self, name):
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

shop = Shop("Book worm")
book = Product("Singing in the thorn", 300, 1000)
shop.add_product(book)
shop.add_product(Product("Magazin", 100, 250))
for p in shop.goods:
    print(f"{p.name} | {p.weight} | {p.price}")
    
print('*************************************************')


