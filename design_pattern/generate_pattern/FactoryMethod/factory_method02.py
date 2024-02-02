"""
FactoryMethod
大量の製品を作成するとき

・Product：作成するオブジェクトの構成要素を定義するIF（作成される側）
・ConcreteProduct：Productを具体化
・Creator：Productを生成するIF
・ConcreteCreator：Creatorを具体化（ConcreteProductを作成）
"""

from abc import ABC, abstractmethod, abstractproperty

class IFactory(ABC):
    def __init__(self):
        self.registered_owners = []
    
    def create(self, owner):
        self._owner = owner
        product = self._create_product()
        self._register_product(product)
        return product
    
    @abstractmethod
    def _create_product(self):
        pass
    
    @abstractmethod
    def _register_product(self, product):
        pass
    
class CarFactory(IFactory):
    def _create_product(self):
        return Car(self._owner)
    
    def _register_product(self, product):
        self.registered_owners.append(product.owner)
        
    
class ShipFactory(IFactory):
    def _create_product(self):
        return Ship(self._owner)
    
    def _register_product(self, product):
        self.registered_owners.append(product.owner)
        
class IProduct(ABC):
    def __init__(self, owner):
        self._owner = owner
    
    @abstractmethod
    def use(self):
        pass
    
    @abstractproperty
    def owner(self):
        pass
    
class Car(IProduct):
    def use(self):
        print(f'{self.owner}: 車を運転します')
        
    @property
    def owner(self):
        return self._owner
    
class Ship(IProduct):
    def use(self):
        print(f'{self.owner}: 船を運転します')
        
    @property
    def owner(self):
        return self._owner

car_factory = CarFactory()
yamada_car = car_factory.create('山田')
sato_car = car_factory.create('佐藤')

yamada_car.use()
sato_car.use()

print(car_factory.registered_owners)