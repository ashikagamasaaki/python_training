from abc import ABC, abstractmethod
from datetime import datetime

class Memento(ABC):
    @abstractmethod
    def get_memo(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, memo):
        self.__memo = memo
        self.__date = datetime.now()

    def get_memo(self):
        return self.__memo

    def __str__(self):
        return f'Memo: {self.__memo} ({self.__date})'


class Notepad:
    def __init__(self, memo=''):
        self.__memo = memo
    
    def get_memo(self):
        return self.__memo
    
    def add_memo(self, memo):
        self.__memo = memo

    def save(self):
        return ConcreteMemento(self.get_memo())
    
    def restore(self, memento: Memento):
        self.add_memo(memento.get_memo())

class CareTaker:
    def __init__(self, notepad):
        self.__notepad = notepad
        self.__mementos: list[Memento] = []

    def backup(self):
        self.__mementos.append(notepad.save())

    def undo(self):
        if len(self.__mementos) == 0:
            print('保存したメモはない')
            return
        
        self.__notepad.restore(self.__mementos.pop())
        # self.__notepad.add_memo(self.__mementos.pop().get_memo())
        # return self.__notepad
    
    def show_history(self):
        for memento in self.__mementos:
            print(memento)



notepad = Notepad()
care_taker = CareTaker(notepad)

notepad.add_memo('Test memo')
care_taker.backup()
notepad.add_memo('First memo')
care_taker.backup()
notepad.add_memo('Second memo')
care_taker.backup()
notepad.add_memo('Third memo')
care_taker.backup()

print("Notepad value(Before Undo) : ", notepad.get_memo())
care_taker.undo()
care_taker.undo()

print("Notepad value(After Undo) : ", notepad.get_memo())
print("---------------------------------")
care_taker.show_history()