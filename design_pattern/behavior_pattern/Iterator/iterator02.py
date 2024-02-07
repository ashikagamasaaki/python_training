"""
Iterator

複雑な構造の集合体をアルゴリズムに沿って探索して返す

・Iterator: インデックスを利用して、要素を順番にスキャンして返すIF
・ConcreteIterator: Iteratorを具体化したクラス
・Aggregate: Iteratorを作成するメソッドを持ったIF
・ConcreteAggregate: Aggregateを具体化したクラス
"""

from abc import ABC, abstractmethod

class Book:
    
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name


class Aggregate(ABC):
    
    @abstractmethod
    def iterator(self):
        pass

# ConcreteAggregate
class BookShelf(Aggregate):

    def __init__(self):
        self.__books = []
        
    def append_book(self, book: Book):
        self.__books.append(book)
    
    def get_book_at(self, index):
        return self.__books[index]
    
    def iterator(self):
        return BookShelfIterator(self)
    
    def __len__(self):
        return len(self.__books)
    
    
class Iterator(ABC):
    
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass
    
# ConcreteIterator
class BookShelfIterator(Iterator):
    
    def __init__(self, book_shelf: BookShelf):
        self.__book_shelf = book_shelf
        self.__index = 0
        
    
    def has_next(self):
        if self.__index < len(self.__book_shelf):
            return True
        else:
            return False
    
    def next(self):
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book


book_shelf = BookShelf()
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ １'))
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ ２'))
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ ３'))
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ ４'))

book_iterator = book_shelf.iterator()

print(book_iterator.next().get_name())
print(book_iterator.next().get_name())
print(book_iterator.next().get_name())
print(book_iterator.next().get_name())