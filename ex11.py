'''
Магические методы __str__, __repr__, __len__, __abs__

__str__() - для отобр. инф. об объекте класса для пользователей
__repr__() - для отобр. инф. об объекте класса в режиме отладки (для разраб-ов)
__len()__ - позволяет применять ф-цию len() к экземпляру класса
__abs__() - позволяет применять ф-цию abs() к экземпляру класса

'''

class Cat:

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str: # должен возвращать строку
        return f'{self.__class__}: {self.name}'

    def __str__(self) -> str: # должен возвращать строку! 
        return f'{self.name}'

cat = Cat('Felix')
print(cat)
str(cat)

class Point:

    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))
        
p = Point(1, -2, 3)
print(len(p))
print(abs(p))

print('*************************************************')

class Book:

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'

book = Book('Скотный двор', 'Дж. Оруэлл', 150)
print(book)
