"""
Bridge

機能拡張を容易にする（拡張時にほかのクラスに影響がないようにする）

・Implementer：基本的な機能を記述したIF
・ConcreteImplementer：Implementerを継承して処理を具体的に記述するクラス
・Abstraction：追加として実装される機能をImplementerと切り離して作成する抽象クラス
・RefinedAbstraction：Abstractionの実装
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @abstractmethod
    def create_shape_str(self):
        pass


class RectangleShape(Shape):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        
    def create_shape_str(self):
        rectangle = '*' * self._width + '\n'
        for _ in range(self._height -2):
            rectangle += '*' + ' ' * (self._width -2) + '*' + '\n'
        rectangle += '*' * self._width + '\n'
        return rectangle


class SquareShape(Shape):
    
    def __init__(self, width, height=None):
        super().__init__(width, height)
        
    def create_shape_str(self):
        square = '*' * self._width + '\n'
        for _ in range(self._width -2):
            square += '*' + ' ' * (self._width -2) + '*' + '\n'
        square += '*' * self._width + '\n'
        return square


class WriteAbstraction(ABC):
    
    def __init__(self, shape: Shape):
        self._shape = shape
        
    def read_shape(self):
        return self._shape.create_shape_str()

    @abstractmethod
    def write_to_text(self, file_name):
        pass
    
    
    

class WriteShape(WriteAbstraction):
    def write_to_text(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as fh:
            fh.write(self.read_shape())

rectangle = RectangleShape(6, 4)
# print(rectangle.create_shape_str())

square = SquareShape(10)
# print(square.create_shape_str())

write_shape = WriteShape(square)
write_shape.write_to_text('tmp.txt')