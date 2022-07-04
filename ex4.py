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