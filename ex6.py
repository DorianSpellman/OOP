'''
Режимы доступа public, private, protected. Сеттеры и геттеры.
'''

#from accessify import private, protected
class Point:

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    #@private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


    def set_coord(self, x, y):  # Setter
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coords is must be digits!')

    def get_coord(self):        # Getter
        return self.__x, self.__y

pt = Point(3, 3)
# print(pt.__x, pt.__y) # AttributeError - нельзя обратиться к private свойствам
pt.set_coord(5, 5) # внутри класса работа разрешена
print(pt.get_coord())

print(dir(pt))
print(pt._Point__x)

print('*************************************************')

class Clock:

    def __init__(self, time=0):
        self.__time = time
    
    @classmethod
    def __check_time(cls, time):
        return type(time) == int and 0 <= time < 100000

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time
        
    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(15)
print(clock.get_time())  #15
clock.set_time(100000)
clock.set_time(-1)
clock.set_time('2')
clock.set_time(0.1)
print(clock.get_time())  #15