class Point:

    color = 'red'
    circle = 2

    def set_coords(self, x=0, y=0):
        #print('**SET COORDS METHOD**')
        self.x = x  # creating local property 
        self.y = y  # of the object

    def get_coords(self):
        return (self.x, self.y) #return tuple with coords



pt = Point()    # creating objects of the class
pt2 = Point()

pt.set_coords(3, 3)
'''
^^^ IS EQUAL vvv
'''
Point.set_coords(pt2, 5, 5)

print('pt:  ', pt.__dict__)
print('pt2: ', pt2.__dict__)

print('pt:  ', pt.get_coords())
print('pt2: ', pt2.get_coords())

f = getattr(pt, 'get_coords') # return attribute
print(f())

# ***************************************

class MediaPlayer:
    
    def open(self, file):
        self.filename = file
        
    def play(self):
        print('Воспроизведение', self.filename) 
        
media1, media2 = MediaPlayer(), MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()

# ***************************************

class Graph:
    
    LIMIT_Y = [0, 10]
    
    def set_data(self, data):
        self.data = data
        
    def draw(self):
        a, b = Graph.LIMIT_Y

        print(*filter(lambda x: a <= x <= b, self.data))

        optim = list()
        for num in self.data:
            if a <= num <= b:
                optim.append(num)
        print(*optim)

graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

# ***************************************

import sys

class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        
        for ind, name in enumerate(fields):
            setattr(self, name, lst_values[ind]) # creating LOCAL property for the object <name> with value <lst_values[ind]>
            
        return True
    

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
