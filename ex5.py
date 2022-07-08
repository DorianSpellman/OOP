'''
Методы класса (classmethod) и статические методы (staticmethod)
'''

class Vector:

    MIN, MAX = 0, 100

    @classmethod # работает только с атрибутами класса
    def check(cls, value):
        return cls.MIN <= value <= cls.MAX

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.check(x) and self.check(y): # classmethod
            self.x = x
            self.y = y
        
        print(self.norm2(5, 2)) # staticmethod

    def get_coord(self):
        return self.x, self.y

    @staticmethod # независимая функция, работает с параметрами, которые в ней определяются
    def norm2(x, y):
        return x*x+y*y

pt = Vector(5, 5)
res = Vector.get_coord(pt)
print(res)


print('Classmethod: ', Vector.check(15)) # classmethod
print('Staticmethod: ', Vector.norm2(5, 2)) # staticmethod

print('*************************************************')

class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)
        

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)

print('*************************************************')

from string import ascii_lowercase, digits

from pyrsistent import s

class TextInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        res = (3 <= len(name) <= 50) and all(map(lambda x: x in cls.CHARS_CORRECT, name))
        if res == False:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

#-----------------------------------------
class PasswordInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        res = (3 <= len(name) <= 50) and all(map(lambda x: x in cls.CHARS_CORRECT, name))
        if res == False:
            raise ValueError("Некорректное поле name")

#-----------------------------------------

class FormLogin:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)

print('*************************************************')

class CardCheck:

    @staticmethod
    def check_card_number(number):
        # return bool(re.fullmatch(r"\d{4}(?:-\d{4}){3}", number))
        num = number.split('-')

        if type(number) != str or len(num) != 4:
            return False
        
        if not all(map(lambda x: len(x) == 4, num)):
            return False

        return all(map(lambda x: x.isdigit(), num))

    @classmethod
    def check_name(cls, name):
        #return bool(re.fullmatch(r"[A-Z\d]+ [A-Z\d]+", name))
        if type(name) != str or len(name.split()) != 2:
            return False

        return all(map(lambda n: set(n) < set(ascii_lowercase.upper()), name.split()))


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("WILLIAM GOLDING")

print(f'Number is correct: {is_number}'
    f'\nName is correct: {is_name}')

print('*************************************************')

class Video:

    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"Воспроизведение '{self.name}'")

class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.videos[video_indx].play()

v1 = Video('Lesson 1')
v2 = Video('Lesson 2')


YouTube.add_video(v1)
YouTube.add_video(v2)

YouTube.play(0)
YouTube.play(1)

print('*************************************************')

class AppStore:

    def __init__(self, applist=[]):
        self.applist = applist

    def add_application(self, app):
        self.applist.append(app)   

    def remove_application(self, app):
        self.applist.remove(app)

    @staticmethod
    def block_application(app):
        app.blocked = True

    def total_apps(self):
        return len(self.applist)

class Application:

    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")

store.add_application(app_youtube)
print(store.applist)
store.remove_application(app_youtube)
print(store.applist)

print('*************************************************')

class Viber:

    msg_list = []

    @classmethod
    def add_message(cls, msg):
        cls.msg_list.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.msg_list.remove(msg)

    def set_like(msg):
        msg.fl_like = not msg.fl_like            

    @classmethod
    def show_last_message(cls, count):
        print(*[msg.text for msg in cls.msg_list[-count:]])
        
    @classmethod
    def total_messages(cls):
        return len(cls.msg_list)


class Message:

    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))

Viber.set_like(msg)
Viber.show_last_message(2)
Viber.remove_message(msg)
