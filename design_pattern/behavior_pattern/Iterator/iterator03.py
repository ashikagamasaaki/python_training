from collections.abc import Iterator, Iterable

class Book:
    
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

class BookShelf(Iterable):
    
    def __init__(self):
        self.__books = []
        
    def append_book(self, book: Book):
        self.__books.append(book)
    
    def get_book_at(self, index):
        return self.__books[index]
    
    def __iter__(self):
        print('Iteratorを作成しました。')
        return BookShelfIterator(self)
    
    def get_iterator(self):
        return BookShelfIterator(self)
    
    def get_reverse_iterator(self):
        return BookShelfIterator(self, reverse=True)
    
    
class BookShelfIterator(Iterator):
    
    def __init__(self, book_shelf: BookShelf, reverse=False):
        self.__book_shelf = book_shelf
        self.__index = -1 if reverse else 0
        self.__reverse = reverse
        
    def __next__(self):
        try:
            print(f'TRY: {self.__index}')
            book = self.__book_shelf.get_book_at(self.__index)
            self.__index += -1 if self.__reverse else 1
        except IndexError:
            raise StopIteration()
        return book
    

book_shelf = BookShelf()
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ １'))
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ ２'))
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ ３'))
book_shelf.append_book(Book('Ｄｒａｇｏｎ　Ｂａｌｌ ４'))

for book in book_shelf:
    print(book.get_name())
    
    
    
print('-' * 100)
book_iterator = book_shelf.get_iterator()
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())


reverse_iterator = book_shelf.get_reverse_iterator()
print('*' * 100)

for book in reverse_iterator:
    print(book.get_name())