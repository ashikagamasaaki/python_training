from abc import ABC, abstractmethod

# 形状インターフェース
class ImageShape(ABC):
    def __init__(self):
        self.__shape = None
    
    @property
    def shape(self):
        return self.__shape
        
    @shape.setter
    def shape(self, shape):
        self.__shape = shape
    
    @abstractmethod
    def draw(self):
        pass
    
    def __str__(self):
        return f'形は{self.shape}です。'


# 具体的な形状クラス
class RectangleShape(ImageShape):
    def draw(self):
        self.shape = 'Rectangle'

class CircleShape(ImageShape):
    def draw(self):
        self.shape = 'Circle'

# 表示形式インターフェース
class ImageDisplay(ABC):
    def __init__(self):
        self.__size = None
    
    @property
    def size(self):
        return self.__size
        
    @size.setter
    def size(self, size):
        self.__size = size
    
    @abstractmethod
    def display(self):
        pass

# 具体的な表示形式クラス
class NormalDisplay(ImageDisplay):
    def display(self):
        self.size = 'Normal'

class EnlargedDisplay(ImageDisplay):
    def display(self):
        self.size = 'Large'


# Image クラスとそのサブクラスを Bridge パターンで実装してください
class Image:
    def __init__(self, shape: ImageShape, display :ImageDisplay):
        self._shape = shape
        self._display = display

    @abstractmethod
    def display_image(self):
        pass


class JPEGImage(Image):
    def __init__(self, shape: ImageShape, display :ImageDisplay):
        super().__init__(shape, display)
    
    def display_image(self):
        self._shape.draw()
        self._display.display()
        print(f'JPEGで画像を表示します。形は{self._shape.shape}で、サイズは{self._display.size}です。')


class PNGImage(Image):
    def __init__(self, shape: ImageShape, display :ImageDisplay):
        super().__init__(shape, display)
    
    def display_image(self):
        self._shape.draw()
        self._display.display()
        print(f'PNGで画像を表示します。形は{self._shape.shape}で、サイズは{self._display.size}です。')


# 使用例
rectangle = RectangleShape()
circle = CircleShape()

normal_display = NormalDisplay()
enlarged_display = EnlargedDisplay()

jpeg_image = JPEGImage(rectangle, normal_display)
png_image = PNGImage(circle, enlarged_display)

jpeg_image.display_image()
png_image.display_image()