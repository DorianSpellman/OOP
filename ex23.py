'''
Множественное наследование
- когда один дочерний класс наследуется от нескольких базовых.

Порядок следования имеет важное значение!
'''


from string import digits


class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # перейдёт в инициализатор следующего базового класса
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price
 
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0
 
    def __init__(self): # в базовых доп. классах принято использовать иниц. без параметров
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID
 
    def print_info(self):
        print(f"{self.id}")


class NoteBook(Goods, MixinLog):

    def print_info(self):   # переопределение метода, который есть в обоих базовых классах
        Goods.print_info(self)
        #MixinLog.print_info(self)

n = NoteBook("Acer", 1.5, 30000)
n.print_info() 

#print(NoteBook.__mro__) # цепочка обхода

print('*************************************************')

class A:
    def __init__(self, name, old):
        super().__init__()
        self.name = name
        self.old = old


class B:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class C(B, A):
    def __init__(self, name, old, weight, height):
        super().__init__(name, old)
        self.weight = weight
        self.height = height

person = C("Balakirev", 33, 80, 185)
print(C.__mro__)

print('*************************************************')

class Digit:

    def __init__(self, value):
        if self.check(value):
            self.value = value
        else:
            raise TypeError('значение не соответствует типу объекта')

    def check(self, value):
        return type(value) in (int, float)


class Integer(Digit):

    def check(self, value):
        return type(value) == int


class Float(Digit):

    def check(self, value):
        return type(value) == float


class Positive(Digit):

    def check(self, value):
        return value >= 0


class Negative(Digit):

    def check(self, value):
        return value < 0


class PrimeNumber(Integer, Positive):
    
    def check(self, value):
        return Integer.check(self, value) and Positive.check(self, value)

class FloatPositive(Float, Positive):

    def check(self, value):
        return Float.check(self, value) and Positive.check(self, value)


pn1 = PrimeNumber(1)
pn2 = PrimeNumber(2)
pn3 = PrimeNumber(5)

fp1 = FloatPositive(1.0)
fp2 = FloatPositive(2.3)
fp3 = FloatPositive(3.8)
fp4 = FloatPositive(4.6)
fp5 = FloatPositive(5.7)

digits = [pn1, pn2, pn3, fp1, fp2, fp3, fp4, fp5]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits)) 

print(lst_positive, lst_float, sep='\n\n')

print('*************************************************')

class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:

    def  __repr__(self):
        return '\n'.join(map(lambda item: f'{item[0]}: {item[1]}', list(self.__dict__.items())))
    # два варианта решения (сверху и снизу)
    def __str__(self) -> str:
        out = []
        for key, value in self.__dict__.items():
            out.append(f'{key}: {value}')
        return '\n'.join(out)


class ShopUserView:
    
    def __repr__(self) -> str:
        out = []
        for key, value in self.__dict__.items():
            if key == '_id': continue
            out.append(f'{key}: {value}')
        return '\n'.join(out)
    # два варианта решения (сверху и снизу)
    def  __str__(self):
        return '\n'.join(map(lambda item: f'{item[0]}: {item[1]}', list(self.__dict__.items())[1:]))


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

book = Book("Book", "Author", 2022)
print(book)

print('*************************************************')

class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:

    allowed_methods = ('GET', 'POST', 'PUT')

    def render_request(self, request):
        method = request['method'].upper() # PUT

        if method not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")

        method_req = self.__getattribute__(method.lower())
        if method_req:
            return method_req(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )

view = DetailView()
html = view.render_request({'url': 'https://google.com', 'method': 'PUT'})
print(html)

print('*************************************************')

class Money:

    def __init__(self, value):
        self.money = value

    @property
    def money(self): return self._money
    @money.setter
    def money(self, value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = value


class MoneyOperators:

    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)
            # С помощью __class__ можно создавать объекты того же класса, что и self

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)
            

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"

m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
#m = m1 + m2  # TypeError