"""
Composite(構造)

・ツリー構造を持つデータに再帰的な処理を行う
・任意の枝葉に対して、共通の手順でアクセス

Client  →   Component
            ↑       ↑
           Leaf     Composite

・複雑なツリー構造を簡単に扱える
・新しい枝葉を追加できる
・ディレクトリツリー、組織図、DOMツリー
"""

from abc import ABCMeta, abstractmethod

class Entry(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def remove(self):
        pass
    
    
class Directory(Entry):
    def __init__(self, name: str):
        super().__init__(name)
        self.__children:list[Entry] = []
        
    def get_size(self) -> int:
        size = 0
        for child in self.__children:
            size += child.get_size()
        return size
    
    def remove(self):
        for child in self.__children:
            child.remove()
        print(f'{self.name}を削除しました。')
        
    def add(self, child: Entry):
        self.__children.append(child)
        

class File(Entry):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.__size = size
        
    def get_size(self) -> int:
        return self.__size
    
    def remove(self):
        print(f'{self.name}を削除しました。')
        
def client(entry: Entry):
    print(entry.name)
    print(entry.get_size())
    entry.remove()
    
if __name__ == '__main__':
    dir1 = Directory('design_pattern')
    dir2 = Directory('composite')
    file1 = File('composite.py', 100)
    file2 = File('composite.png', 150)
    
    dir2.add(file1)
    dir2.add(file2)
    dir1.add(dir2)
    
    client(dir1)
    