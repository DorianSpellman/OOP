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
            setattr(Dialog.obj, 'name', name) # в качестве локального атрибута (свойства) передаём название

        if TYPE_OS != 1:
            Dialog.obj = super().__new__(DialogLinux)
            setattr(Dialog.obj, 'name', name)

        return Dialog.obj

obj = Dialog('Henry')

print(isinstance(obj, DialogWindows)) # True
print(obj.__dict__)



