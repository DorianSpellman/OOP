'''
Инструкция raise и пользовательские исключения

Специальная генерация исключения - 
raise <Type of Error>('<comment>')
'''

class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""

class ExceptionPrintSendData(ExceptionPrint): # Пользовательские ислключения
    """Класс исключения при отправке данных принтеру""" 
    
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")
 
    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")
 
    def send_to_print(self, data):
        return 0


p = PrintData()
#p.print("123")

try:
    p.print("123")
except ExceptionPrintSendData as e:
    print(e)
except ExceptionPrint:
    print("Общая ошибка печати")


print('*************************************************')

class StringException(Exception): ...

class NegativeLengthString(StringException): '''длина отрицательная'''

class ExceedLengthString(StringException): '''длина превышает заданное значение'''


try:
    raise ExceedLengthString()
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")

print('*************************************************')

class PrimaryKeyError(Exception):

    def __init__(self, **kwargs):
        if 'id' not in kwargs and 'pk' not in kwargs:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'

        else:
            key, value = tuple(kwargs.items())[0]
            self.message = f'Значение первичного ключа {key} = {value} недопустимо'

    def __str__(self):
        return self.message

try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
