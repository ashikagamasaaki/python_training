from abc import ABC, abstractmethod

# Product
class Product(ABC):
    @abstractmethod
    def create(self):
        pass
    
class Book(Product):
    def create(self):
        print('コピー')
        print('製本')
        print('陳列')
        
class Electronics(Product):
    def create(self):
        print('設計')
        print('製造')
        print('組み立て')
        print('販売')


class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass
    
    def order_product(self):
        product = self.create_product()
        product.create()

class BookFactory(Factory):
    def create_product(self):
        return Book()

class ElectronicsFactory(Factory):
    def create_product(self):
        return Electronics()


book_factory = BookFactory()
book_factory.order_product()