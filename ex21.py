''''
Наследование. Атрибуты private и protected

_attr - обращение внутри класса и в дочерних
__attr - обращение только внутри класса

если перед именем метода и после него стоят два подчеркивания
(например, __abc__()), то такой метод является публичным
'''

class Geom:
    name = 'Geom'
 
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1 # private
        self.__x2 = x2
        self.__y2 = y2

    def _verify(self, coord): # protected
        return 0 <= coord < 100
    
    def get__coords(self):
        print(self.__x1, self.__y1)

    def __check__(self):    # public
        return self.name is not None


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2) 
        self._fill = fill
        
    
r = Rect(0, 0, 10, 20, 'green')
r.get__coords()
print(r.__dict__)
print(r.__check__())

print('*************************************************')

class Animal:

    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, val): self.__name = val

    @property
    def kind(self): return self.__kind
    @kind.setter
    def kind(self, val): self.__kind = val

    @property
    def old(self): return self.__old
    @old.setter
    def old(self, val): self.__old = val

animals = [Animal('Васька', 'дворовый кот', 5),
            Animal('Рекс', 'немецкая овчарка', 8),
            Animal('Кеша', 'попугай', 2)]

print(animals[0].name)

print('*************************************************')

class Furniture: # Мебель

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        
    def __verify_weight(self, weight):
        if not weight > 0:
            raise TypeError('вес должен быть положительным числом')

    def __setatt__(self, key, value):
        if key == 'name':
            self.__verify_name(value)
            self._name = value

        if key == 'weight':
            self.__verify_weight(value)
            self._weight = value

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture): # Шкафы

    def __init__(self, name, weight, tp: bool, doors: int):
        # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей 
        super().__init__(name, weight)
        self._tp = bool(tp)
        self._doors = doors


class Chair(Furniture):

    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture): 

    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    
cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
        
print('*************************************************')

class Observer:

    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность

class TemperatureView(Observer):

    def update(self, data):
        if data:
            print(f'Текущая температура {data.temp}')

class PressureView(Observer):

    def update(self, data):
        if data:
            print(f'Текущее давление {data.press}')

class WetView(Observer):

    def update(self, data):
        if data:
            print(f'Текущая влажность {data.wet}')

subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))
# выведет строчки:
# Текущая температура 23
# Текущее давление 150
# Текущая влажность 83
subject.remove_observer(wet)
print()
subject.change_data(Data(24, 148, 80))
# выведет строчки:
# Текущая температура 24
# Текущее давление 148

print('*************************************************')

class Aircraft:

    def __init__(self, model: str, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == '_model' and not isinstance(value, str) \
            or key in ('_mass', '_speed', '_top') and not value > 0:
            raise TypeError('неверный тип аргумента')
        else:
            object.__setattr__(self, key, value)      


class PassengerAircraft(Aircraft):

    def __init__(self, model, mass, speed, top, chairs: int):
        # chairs - число пассажирских мест
        super().__init__(model, mass, speed, top)
        if not isinstance(chairs, int) or chairs <= 0:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):

    def __init__(self, model, mass, speed, top, weapons: dict):
        super().__init__(model, mass, speed, top)
        # weapons - вооружение (словарь); ключи - название оружия, значение - количество
        if not isinstance(weapons, dict):
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons
            

PasAir_1 = PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140)
PasAir_2 = PassengerAircraft('SuperJet', 1145, 8640, 11034, 80)
WarPlane_1 = WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10})
WarPlane_2 = WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})

print(f'МС-21 chairs: {PasAir_1._chairs}')
print(f'Миг-35 weapons: {WarPlane_1._weapons}')

print('*************************************************')

def class_log(log_lst):

    def log_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_method_decorator(v))
        return cls

    
    def log_method_decorator(func):
        def wrapper(*args, **kwargs):
            log_lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper


    return log_methods


vector_log = []


@class_log(vector_log) # == Vector = class_log(vector_log)(Vector)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)

print('*************************************************')

CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:

    def __new__(cls, title, path, exts, *args, **kwargs):

        dlg_cls = {'windows': WindowsFileDialog, 'linux': LinuxFileDialog}
        
        return dlg_cls[CURRENT_OS](title, path, exts)

        # if CURRENT_OS.lower() == 'windows':
        #     return cls.create_windows_filedialog(title, path, exts)
    
        # if CURRENT_OS.lower() == 'linux':
        #     return cls.create_linux_filedialog(title, path, exts)


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg.__dict__)

