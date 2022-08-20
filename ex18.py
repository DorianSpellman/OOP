'''
Наследование
- это когда один класс (дочерний) расширяет функциональность другого (базового) класса
'''

from cmd import IDENTCHARS


class Geom: # Базовый (родительский) класс

    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Line(Geom):# Подкласс (дочерний класс)

    name = 'Line' # переопределение атрибута

    def draw(self):
        print('Drawing line')

class Rect(Geom):# Подкласс (дочерний класс)

    def draw(self):
        print('Drawing rectangle')


l = Line()
r = Rect()
print(l.name) # Line
print(r.name) # Geom
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)

print('*************************************************')

class Animal:

    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old

class Cat(Animal):

    def __init__(self, name: str, old: int, color: str, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"
    
class Dog(Animal):

    def __init__(self, name: str, old: int, breed: str, size: tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"

cat = Cat('Felix', 8, 'Orange', 4.9)
dog = Dog('Yuki', 3, 'white', (1.0, 0.7))
print(cat.get_info(), dog.get_info(), sep='\n')

print('*************************************************')

class Thing:

    ID = 1

    def __init__(self, name: str, price: float, weight: float=None, dims: float=None, memory:int=None, frm:str=None):
        self.id = Thing.ID
        Thing.ID += 1
        self.name = name
        self.price = price

        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm
    
    def get_data(self):
        #return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)
        ret = []
        for key, value in self.__dict__.items():
            if value is not None:
                        ret.append(value)
        return tuple(ret)

class Table(Thing):

    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight=weight, dims=dims)

class ElBook(Thing):

    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory=memory, frm=frm)

table = Table("Circle", 1024, 812.55, (100, 100, 100))
book = ElBook("Поющие в терновнике", 150, 24, 'txt')
print(*table.get_data())
print(*book.get_data())

print('*************************************************')

class GenericView:

    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):

    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request: dict, method: str):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

        func = getattr(self, method.lower(), False)
        if func:
            return func(request)

    def get(self, request):
        if type(request) is not dict:
            raise TypeError('request не является словарем')
        
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')

        return f"url: {request['url']}" # возвращение значение из словаря request по ключу 'url'

dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
print(html)

print('*************************************************')

class Singleton:

    _object = None
    _object_base = None

    def __new__(cls, *args):
        if cls._object is None and cls != Singleton:
            cls._object = object.__new__(cls)
        return cls._object

class Game(Singleton):

    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name 

s = Singleton()
g = Game('game1')
g2 = Game('game2')
print(id(g) == id(g2)) # True

print('*************************************************')

class Validator:

    def _is_valid(self, data):
        if self.__class__ == IntegerValidator:
            return type(data) is int and self.min_value <= data <= self.max_value
        if self.__class__ == FloatValidator:
            return type(data) is float and self.min_value <= data <= self.max_value

    def __call__(self, data):
        if self._is_valid(data):
            self.data = data
        else:
            raise ValueError('данные не прошли валидацию')

class IntegerValidator(Validator):
    
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        
class FloatValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
integer_validator(10)  # data = 10. исключение не генерируется (проверка проходит)
#float_validator(10)    # исключение ValueError
print(integer_validator.__dict__)

print('*************************************************')

class Layer:

    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None

    def __call__(self, layer, *args):
        self.next_layer = layer
        return layer

class Input(Layer):

    def __init__(self, inputs: int):
        super().__init__(name='Input')
        self.inputs = inputs

class Dense(Layer):

    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__(name='Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:

    def __init__(self, network):
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)

print('*************************************************')

class Vector:

    types = (int, float)

    def __init__(self, *coords):
        self.check(coords)
        self.coords = coords

    def check(self, coords):
        if not all(type(x) in self.types for x in coords):
            raise ValueError('неверный тип координат')

    def get_coords(self):
        return tuple(self.coords)

    @staticmethod
    def is_v(obj):
        if not isinstance(obj, Vector):
            raise TypeError('операнд должен быть класса Vector')

    def check_v(self, other):
        if len(self.coords) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def make_v(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.is_v(other)
        self.check_v(other)

        coords = tuple(a+b for a, b in zip(self.coords, other.get_coords()))
        return self.make_v(coords)

    def __sub__(self, other):
        self.is_v(other)
        self.check_v(other)

        coords = tuple(a-b for a, b in zip(self.coords, other.get_coords()))
        return self.make_v(coords)

class VectorInt(Vector):

    types = (int, )
 
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 
print(v.__dict__)

