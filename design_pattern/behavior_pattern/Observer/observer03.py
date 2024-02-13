from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, name:str):
        pass

class StoreObserver(Observer):
    def update(self, name: str):
        print(f'{name}が入荷されました。出荷可能です。')

class PersonalObserver(Observer):
    def update(self, name: str):
        print(f'{name}が入荷されました。購入可能です。')

class ItemSubject(ABC):
    def __init__(self, name: str):
        self.__name = name
        self.__observers: list[Observer] = []

    def attach(self, observer: Observer):
        self.__observers.append(observer)

    def detach(self, observer: Observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self.__name)

    @abstractmethod
    def restock(self):
        pass

class TvGameSubject(ItemSubject):
    def __init__(self, name):
        super().__init__(name)
        self.__in_stock = False

    def restock(self):
        self.notify()
        self.__in_stock = True

tv_game = TvGameSubject('TV Game')
store = StoreObserver()
personal = PersonalObserver()

tv_game.attach(store)
tv_game.attach(personal)

tv_game.notify()
