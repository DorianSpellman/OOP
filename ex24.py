'''
Коллекция __slots__

С помощью __slots__ мы можем использовать, изменять и удалять только заданные
локальные атрибуты объектов, прописанных в __init__ - и никакие другие. 
Мы не можем создавать другие атрибуты. Если есть коллекция slots, то исчезает 
коллекция dict.

- уменьшается объем памяти, занимаемый объектом класса
- разрешает в экземплярах класса только те имена атрибутов, которые указаны в __slots__
- в объектах класса пропадает коллекция __dict__
- скорость обращения к локальным атрибутам повышается
- коллекция __slots__ накладывает ограничения на атрибуты объектов 
  базового класса, но не дочернего

__slots__ занимает меньше памяти, чем __dict__.

obj.__sizeof__() - измеряет объём памяти в байтах

'''

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(1, 2) # {'x': 1, 'y': 2}

pt.y = 100 # {'x': 1, 'y': 100}
pt.z = 4 # {'x': 1, 'y': 100, 'z': 4}
print(pt.__dict__)

print()

class Point2:

    __slots__ = ('x', 'y', '__length') # локальные атрибуты объектов 

    MAX = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


pt2 = Point2(10, 20)
pt2.x = 5
pt2.y = 10
# pt2.z = 15 AtributeError
print(pt2.__slots__)

print(pt.__sizeof__() + pt.__dict__.__sizeof__()) # 120
print(pt2.__sizeof__()) # 32

print(pt2.length) # 22.360679774997898

print()

class Point3(Point2):
    pass


pt3 = Point3(10, 20)  
pt3.z = 30 # Выполнится без ошибок
print(pt3.x, pt3.y, pt3.z, pt3.length)

print('*************************************************')

class Money:
    __slots__ = '_money',

    def __init__(self, value):
        self._money = value


class MoneyR(Money):
    __slots__ = '_value',


m = MoneyR(10) # m._money = 10
m._money = 100 # m._money = 100
m._value = 20

'''
Программа выполнится без ошибок, так как коллекция __slots__ дочернего 
класса расширяет коллекцию __slots__ базового класса и атрибуты 
с именами _money и _value допустимы.

Если в классе MoneyR прописать __slots__ = '_value', '_money', а 
в базовом классе убрать определение __slots__, то поведение 
объекта m дочернего класса MoneyR не изменится.
'''

print(m._money, m._value) # 100 20

print('*************************************************')

class Person:

     __slots__ = ('_fio', '_old', '_job')

     def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job

persons = [Person('Суворов', 52, 'полководец'),
            Person('Рахманинов', 50, 'пианист, композитор'),
            Person('Балакирев', 34, 'программист и преподаватель'),
            Person('Пушкин', 32, 'поэт и писатель')]

print('*************************************************')

class Planet:

    def __init__(self, name, diametr, period_solar, period):
        'period_solar - период (время) обращения планеты вокруг Солнца; period - период обращения планеты вокруг своей оси'
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:

    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')

    System = None

    def __new__(cls, *args):
        if cls.System is None:
            cls.System = super().__new__(cls)

        return cls.System
        

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)


s_system = SolarSystem()
s = SolarSystem()

for x in s_system.__slots__:
    print(getattr(s_system, x)._name, getattr(s_system, x)._period)


print('*************************************************')

class Star:

    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class WhiteDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

class YellowDwarf (Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

class RedGiant (Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

class Pulsar (Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = list(filter(lambda planet: isinstance(planet, WhiteDwarf), stars))
print(len(white_dwarfs))

print('*************************************************')

class Note:

    _values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, name, value):
        if name == '_name' and value not in self._values:
            raise ValueError('недопустимое значение аргумента')

        if name =='_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')

        object.__setattr__(self, name, value)

class Notes:

    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    _values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __del__(self):
        Notes._instance = None
        

    def __init__(self):
        for attr, value in zip(self.__slots__, self._values):
            setattr(self, attr, Note(value, 0))

    def __getitem__(self, indx):
        if not (0 <= indx < 7):
            raise IndexError('недопустимый индекс')
        
        return getattr(self, self.__slots__[indx])

notes = Notes()

print([(note._name, note._ton) for note in notes])

print('*************************************************')

class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('амплитуда должна быть числом')

        obj = self.__class__(self)
        obj._amplitude *= other
        return obj


class Linear(Function):

    def __init__(self, k=None, b=None):
        super().__init__()
        if type(k) is Linear:
            self._k, self._b = k._k, k._b
        else:
            self._k = k
            self._b = b

    def _get_function(self, x):
        return self._k * x + self._b
    