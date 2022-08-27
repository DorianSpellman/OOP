'''
Полиморфизм и абстрактные методы.

Полиморфизм - это возможность работать с совершенно разными объектами единым образом.
Абстрактные методы - методы, которые должны быть переопределены в дочерних классах
'''

class Geom:

    def get_pr(self):
        return NotImplementedError(f'В дочернем классе {self.__class__} должен быть переопределён метод get_pr')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h
 
    def get_pr(self):
        return 2*(self.w+self.h)
 
 
class Square(Geom):
    def __init__(self, a):
        self.a = a
 
    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
 
    # def get_pr(self):
    #     return self.a + self.b + self.c

        
geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)
        ]

for g in geom:
    print(g.get_pr())


print('*************************************************')

class Student:
    def __init__(self, fio, group):
        self._fio = fio  # ФИО студента (строка)
        self._group = group # группа (строка)
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:

    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

    def set_mark(self, student, mark):
        return NotImplementedError('Method hasnt been implemented yet')
        
    def __str__(self):
        return NotImplementedError('Method hasnt been implemented yet')
    
class Lector(Mentor):

    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f'Лектор {self._fio}: предмет {self._subject}'


class Reviewer(Mentor):

    def __init__(self, fio, subject):
        super().__init__(fio, subject)
    
    def set_mark(self, student, mark):
        student.add_house_marks(mark)
    
    def __str__(self):
        return f'Эксперт {self._fio}: предмет {self._subject}'

lector = Lector("Балакирев С.М.", "Информатика")
reviewer = Reviewer("Гейтс Б.", "Информатика")
students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
persons = [lector, reviewer]

lector.set_mark(students[0], 4)
lector.set_mark(students[1], 2)
reviewer.set_mark(students[0], 5)
reviewer.set_mark(students[1], 3)

for p in persons + students: # сначала пройдется по persons, затем по students
    print(p)

print('*************************************************')

class ShopInterface:
    
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')

    
class ShopItem(ShopInterface):

    __ID = 0

    def __init__(self, name, weight, price):
        self.__id = self.set_id()
        self._name = name
        self._weight = weight
        self._price = price
    
    @classmethod
    def set_id(cls):
        cls.__ID += 1
        return cls.__ID
    
    def get_id(self):
        return self.__id

    
item1 = ShopItem("имя1", "вес1", "100")
item2 = ShopItem("имя2", "вес2", "200")
print(item1.get_id())
print(item2.get_id())

print('*************************************************')

class Validator:

    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')
    
class FloatValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        return isinstance(value, float) and self.min_value <= value <= self.max_value

float_validator = FloatValidator(0, 10.5)
print(float_validator(1))  # False (целое число, а не вещественное)
print(float_validator(1.0)) # True
print(float_validator(-1.0))  # False (выход за диапазон [0; 10.5])

print('*************************************************')

'''
В языке Python есть еще один распространенный способ 
объявления абстрактных методов класса через декоратор abstractmethod модуля abc:

from abc import ABC, abstractmethod

Чтобы корректно работал декоратор abstractmethod сам класс 
должен наследоваться от базового класса ABC. Например, так:

class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        """Абстрактный метод класса"""

Мы здесь имеем два абстрактных метода внутри класса Transport, 
причем, первый метод go() - это обычный метод, 
а второй abstract_class_method() - это абстрактный метод уровня класса. Обратите внимание на порядок использования декораторов classmethod и abstractmethod. Они должны быть записаны именно в такой последовательности.

Теперь, если объявить какой-либо дочерний класс, например:

class Bus(Transport):
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    def go(self):
        print("bus go")

    @classmethod
    def abstract_class_method(cls):
        pass
То в нем обязательно нужно переопределить абстрактные методы 
go и abstract_class_method класса Transport. 
Иначе, объект класса Bus не будет создан (возникнет исключение TypeError).
'''

from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def get_pk(self):
        ''

    def get_info(self):
        return "Базовый класс Model"

class ModelForm(Model):

    __ID = 0

    def __init__(self, login, password):
        self._id = self.set_id()
        self._login = login
        self._password = password

    @classmethod
    def set_id(cls):
        cls.__ID += 1
        return cls.__ID

    def get_pk(self):
        return self._id

form = ModelForm("Логин", "Пароль")
print(form.get_pk())
    
print('*************************************************')

class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        '''добавление объекта в конец стека'''

    @abstractmethod
    def pop_back(self):
        '''удаление последнего объекта из стека'''


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None
        

class Stack(StackInterface):

    def __init__(self):
        self._top = None # вершина, начало стека - всегда ссылается на первый элемент стека
        self.__count = 0

    def push_back(self, obj):
        self.__count += 1

        if self._top is None:
            self._top = obj

        else:
            current = self._top
            while current._next is not None:
                current = current._next

            current._next = obj    

    def pop_back(self):
        current = self._top

        if current and current._next is None:
            self._top = None
            self.__count -= 1

        elif current and current._next:
            self.__count -= 1
            last = current
            current = current._next
            while current._next:
                last = current
                current = current._next
            last._next = None

        return current
    
st = Stack()
st.push_back(StackObj("obj 1"))
st.push_back(StackObj("obj 2"))
st.push_back(StackObj("obj 3"))
print(st.__dict__)

print(st.pop_back())

print('*************************************************')

'''
С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства (property). Делается это следующим образом:

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def go(self):
        "Метод для перемещения транспортного средства"

    @property
    @abstractmethod
    def speed(self):
        "Абстрактный объект-свойство"
'''

class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        'название страны (строка)'

    @property
    @abstractmethod
    def population(self):
        'численность населения (целое положительное число)'

    @property
    @abstractmethod
    def square(self):
        'площадь страны (положительное число)'

    @abstractmethod
    def get_info(self):
        'абстрактный метод для получения сводной информации о стране'

    
class Country(CountryInterface):

    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self): return self._name
    @name.setter
    def name(self, val):
        if isinstance(val, str):
            self._name = val
    
    @property
    def population(self): return self._population
    @population.setter
    def population(self, val):
        if isinstance(val, int) and val > 0:
            self._population = val

    @property
    def square(self): return self._square
    @square.setter
    def square(self, val):
        if val > 0:
            self._square = val

    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000

print('*************************************************')

class Track:

    def __init__(self, *args, **kwargs):
        self.__points = []
        
        if len(args) == 2:
            self.__points.append(PointTrack(args[0], args[1]))
        else:
            for a in args:
                self.__points.append(a)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def pop_back(self):
        self.__points.pop()

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:

    def __init__(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.x = x
            self.y = y
        else:
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()

for pt in tr.points:
    print(pt)

print('*************************************************')

class Food:

    def __init__(self, name: str, weight, calories: int):
        self._name = name
        self._weight = weight
        self._calories = calories

class BreadFood(Food):

    def __init__(self, name: str, weight, calories: int, white: bool):
        'white - True для белого хлеба, False - для остальных'
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):

    def __init__(self, name: str, weight, calories: int, dietary: bool):
        'dietary - True для диетического супа, False - для других видов'
        super().__init__(name, weight, calories)
        self._dietary = dietary

class FishFood(Food):

    def __init__(self, name: str, weight, calories: int, fish: str):
        'fish - вид рыбы (семга, окунь, сардина и т.д.)'
        super().__init__(name, weight, calories)
        self._fish = fish


bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Tom-Yam", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "Сёмга")
a = SoupFood()



        

