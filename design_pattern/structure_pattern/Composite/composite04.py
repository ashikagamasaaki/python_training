from abc import ABC, abstractmethod

class Component(ABC):
    @property
    def name(self):
        return self._name
    
    @property
    def size(self):
        return self._size
    
    @property
    def parent(self):
        return self._parent
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @size.setter
    def size(self, size):
        self._size = size
    
    @parent.setter
    def parent(self, parent):
        self._parent = parent
        
    @abstractmethod
    def print_list(self, path):
        pass
    
    def __str__(self):
        return f'{self.name} ({self.size})'
    
    
class File(Component):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None
        
    def print_list(self, path=''):
        return f'{path}/{str(self)}'
    
    
class Directory(Component):
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.children: list[Component] = []
        
    def add_child(self, child: Component):
        self.children.append(child)
        self.size += child.size
        
    def print_list(self, path=''):
        print(path + '/' + str(self))
                
        for child in self.children:
            print('   ' + child.print_list())



root = Directory('root')
var = Directory('var')
usr = Directory('usr')
www = Directory('www')
app = Directory('app')


file1 = File('file1.txt', 10)
file2 = File('file2.txt', 20)
file3 = File('file3.txt', 30)
file4 = File('file4.txt', 40)
file5 = File('file5.txt', 50)
file6 = File('file6.txt', 60)
file7 = File('file7.txt', 70)


root.add_child(file1)
root.add_child(file2)

var.add_child(file3)
var.add_child(file4)

www.add_child(file5)
www.add_child(file6)

app.add_child(file7)


root.add_child(var)
var.add_child(www)
root.add_child(app)

root.print_list()

"""
root
 └ app
 └ var
    └ www
"""