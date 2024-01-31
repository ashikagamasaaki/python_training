from abc import ABC, abstractmethod

class AbstractSpongeCake(ABC):
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def price(self):
        pass

class ShortCake(AbstractSpongeCake):
    @property
    def name(self):
        return 'ショートケーキ'
    
    @property
    def price(self):
        return 500

class ChocolateCake(AbstractSpongeCake):
    @property
    def name(self):
        return 'チョコレートケーキ'
    
    @property
    def price(self):
        return 700


class CakeDecorator(AbstractSpongeCake, ABC):
    def __init__(self, decorate_cake: AbstractSpongeCake):
        self.decorate_cake = decorate_cake
    
    @property
    def name(self):
        return self.decorate_cake.name
    
    @property
    def price(self):
        return self.decorate_cake.price
    

class StrawberryDecorator(CakeDecorator):
    @property
    def name(self):
        return 'イチゴ' + self.decorate_cake.name
    
    @property
    def price(self):
        return self.decorate_cake.price + 100
    

class BananaDecorator(CakeDecorator):
    @property
    def name(self):
        return 'バナナ' + self.decorate_cake.name
    
    @property
    def price(self):
        return self.decorate_cake.price + 80






short_cake = ShortCake()
print(f'商品名：{short_cake.name}、代金：{short_cake.price}')

choco_cake = ChocolateCake()
print(f'商品名：{choco_cake.name}、代金：{choco_cake.price}')

decorate_cake = CakeDecorator(short_cake)
print(f'商品名：{decorate_cake.name}、代金：{decorate_cake.price}')

strawberry_cake = StrawberryDecorator(short_cake)
print(f'商品名：{strawberry_cake.name}、代金：{strawberry_cake.price}')

banana_strawberry_cake = BananaDecorator(StrawberryDecorator(short_cake))
print(f'商品名：{banana_strawberry_cake.name}、代金：{banana_strawberry_cake.price}')