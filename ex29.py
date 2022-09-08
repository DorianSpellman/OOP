'''
Менеджеры контекстов. Оператор with

Менеджер контекста – это класс, в котором реализованы два магических метода:
__enter__() - Когда происходит создание менеджера контекста
__exit__() - когда менеджер контекста завершает свою работу (программа внутри него выполнилась или произошло исключение)
'''

class DefenderVector:

    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        'exc_type - тип возникшего исключения (None, если не произошло)'
        'exc_val - объект класса возникшего исключения (None, если не произошло)'
        'exc_tb - трассировка стека возникшего исключения (None, если не произошло)'
        if exc_type is None:
            self.__v[:] = self.__temp

        return False

v1 = [1, 2 ,3]
v2 = [2, 3]

try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print('Error...')
finally:
    print(v1)


print('*************************************************')

