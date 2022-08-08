'''
Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие
Главное реализовать методы eq, lt, le - другие будут работать в инверсном режиме
__eq__ - equal - ==
__ne__ - not equal to - !=
__gt__ - greater  - >
__ge__ - greater or equal - >=
__lt__ - little - <
__le__ - less or equal - <=
'''

from ctypes import c_void_p
from msilib.schema import MsiAssembly
from unicodedata import name


class Clock:

    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Опернад справа должен иметь тип  int/Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        s = self.__verify(other)
        return self.seconds == s

    def __lt__(self, other):
        s = self.__verify(other)
        return self.seconds < s

    def __le__(self, other):
        s = self.__verify(other)
        return self.seconds <= s

c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == 1000)
print(c1 != 2000) # вызовется метод not(__gt__)
print(c1 < c2)
print(c2 > c1) # __gt__ не реализован, поэтому вызовется __lt__, только операнды поменяются местами между собой
print(c1 <= c2)

print('*************************************************')

class Track:


    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.track = []

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    def __len__(self):
        x_1 = (self.start_x - self.track[0].x) ** 2
        y_1 = (self.start_y - self.track[0].y) ** 2
        len_1 = (x_1 + y_1) ** 0.5
        return int(len_1 + sum(self.__get_len(i) for i in range(1, len(self.track))))

    def __get_len(self, i):
        x = (self.track[i-1].x - self.track[i].x) ** 2
        y = (self.track[i-1].y - self.track[i].y) ** 2
        return (x + y) **0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)
    

class TrackLine:

    def __init__(self, to_x, to_y, max_speed: int):
        self.x = to_x
        self.y = to_y
        self.max_speed = max_speed


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
    
print('*************************************************')

class Desc:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.varify(instance, value):
            setattr(instance, self.name, value)

    @staticmethod
    def varify(instance, value):
        return instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION

class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    a, b, c = Desc(), Desc(), Desc()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    def __lt__(self, other):
        v1 = self.volume()
        v2 = other.volume()
        return v1 < v2

    def __le__(self, other):
        v1 = self.volume()
        v2 = other.volume()
        return v1 <= v2

class ShopItem:

    def __init__(self, name: str, price, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim

trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))

lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda item: item.dim.volume())

for obj in lst_shop_sorted:
    print(f'{obj.name:12} {obj.dim.a * obj.dim.b * obj.dim.c}')

print('*************************************************')

class StringText:
    
    def __init__(self, lst):
        self.lst_words = list(lst)

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)
        
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

strip_chars = "–?!,.;"
lst_text = [StringText(x.strip(strip_chars) for x in line.split() if len(x.strip(strip_chars)) > 0) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]

print(lst_text_sorted)

print('*************************************************')

class Morph:

    def __init__(self, *words):
        self.words = list(map(lambda x: x.strip(' !?.,:;()-').lower(), words))

    def add_word(self, word):
        word = word.lower()
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, word):
        if type(word) != str:
            raise ValueError('Операнд должен быть строкой')
        return word.lower() in self.words

def verify(text, dct):
    text_list = list(word.strip(' !?.,:;()-').lower() for word in text.split())
    count = sum(word == morph for word in text_list for morph in dct)
    print(count)


w1 = Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях')
w2 = Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах')
w3 = Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах')
w4 = Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах')
w5 = Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')

dict_words = (w1, w2, w3, w4, w5)

text = 'Мы будем устанавливать связь завтра днем.'
verify(text, dict_words)

print('*************************************************')

class FileAcceptor:

    def __init__(self, *extensions: str):
        self.extensions = set(extensions)

    def __add__(self, other):
        return FileAcceptor(*self.extensions | other.extensions)
        
    def __call__(self, filename):
        return filename.split('.')[-1] in self.extensions                
            

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filters = acceptor_images + acceptor_docs
print(filters.extensions)

filenames = list(filter(filters, filenames))
print(filenames)

print('*************************************************')

class CentralBank:

    rates = {'rub': 1.0, 'dollar': 60.58, 'euro': 61.7}

    def __new__(cls, *args):
        return 

    @classmethod
    def register(cls, money):
        money.cb = cls

class Money:

    type_money = None
    EPS = 0.1

    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self): return self.__cb
    @cb.setter
    def cb(self, value): self.__cb = value

    @property
    def volume(self): return self.__volume
    @volume.setter
    def volume(self, value): self.__volume = value

    def get_volumes(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        if self.type_money is None:
            raise ValueError('Неизвестен тип кошелька.')

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]

        return v1, v2
    
    def __eq__(self, other):
        v1, v2 = self.get_volumes(other)
        return abs(v1-v2) < self.EPS

    def __lt__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 <= v2    

class MoneyR(Money):
    type_money = 'rub'

class MoneyD(Money):
    type_money = 'dollar'

class MoneyE(Money):
    type_money = 'euro'    

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("Возьми рубли")
else:
    print("Возьми доллары")

print('*************************************************')

class Body:

    def __init__(self, name: str, ro, volume):
        self.name = name
        self.ro = ro # плотность
        self.volume = volume # объем

    def __eq__(self, other):
        m1 = self.ro * self.volume
        m2 = other
        if type(other) is Body:
            m2 = other.ro * other.volume
        return m1 == m2

    def __lt__(self, other):
        m1 = self.ro * self.volume
        m2 = other
        if type(other) is Body:
            m2 = other.ro * other.volume
        return m1 < m2

b1 = Body('Figure 1', 150, 3)
b2 = Body('Figure 2', 80, 5)
print(b1 > b2, b1 == b2, b1 < 425, b2 < 425)

print('*************************************************')

class Box:

    def __init__(self):
        self.box = list()

    def add_thing(self, obj):
        self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        # k = 0
        # for b1 in self.box:
        #     for b2 in other.box:
        #         if b1 == b2:
        #             k += 1
        # return k == len(self.box) == len(other.box)

        return all(b1 in self.box for b1 in other.box)

class Thing:

    def __init__(self, name: str, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

print(b1 == b2) # True

