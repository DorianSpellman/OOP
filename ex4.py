'''
Магический метод __new__. Пример паттерна Singleton
'''

class DataBase:

    '''
    Паттерн проектированя Singleton - контроль над тем, чтобы в классе существовал только 1 экземпляр.
    Если атрибут cls.__instance не существует, то мы создаём новый экземпляр класса.
    Если атрибут не None, то метод возвращает адрес ранее созданного объекта.
    '''
    __instance = None # ссылка на объект класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self): # финализатор класса
        DataBase.__instance = None



    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connectnig with DB: {self.user}, {self.psw}, {self.port}')

db = DataBase('root', '12345', '5000')
db2 = DataBase('root2', '1234567', '1280')
print(id(db), id(db2))

db.connect()
db2.connect()

print('*************************************************')

class AbstractClass:

    def __new__(cls, *args, **kwargs):
        return 'Ошибка: нельзя создавать объекты абстрактного класса'

obj = AbstractClass()
print(obj)

print('*************************************************')

class SingletonFive:

    _obj = None
    cnt = 0

    def __new__(cls, *args, **kwargs):
        
        if cls.cnt < 5:
            cls._obj = super().__new__(cls)

        cls.cnt += 1

        return cls._obj

    def __init__(self, name):
        self.name = name

    
objs = [SingletonFive(str(n)) for n in range(10)]

for i in objs:
    print(id(i))

print('*************************************************')

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    obj = None

    def __new__(cls, name, *args, **kwargs):
        if TYPE_OS == 1: # если тип ОС - 1, то создаём объект класса Windows
            Dialog.obj = super().__new__(DialogWindows)

        if TYPE_OS != 1:
            Dialog.obj = super().__new__(DialogLinux)
        
        setattr(Dialog.obj, 'name', name) # в качестве локального атрибута (свойства) передаём название
        return Dialog.obj

obj = Dialog('Henry')

print(isinstance(obj, DialogWindows)) # True
print(obj.__dict__)

print('*************************************************')

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y) # клонирование объекта


pt = Point(5, 5)
pt_clone = pt.clone()

print(pt.__dict__)
print(pt_clone.__dict__)

print('*************************************************')

class Factory:
    def build_sequence(self):
        return list()
    
    def build_number(self, string):
        return float(string)    

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
print(res)
