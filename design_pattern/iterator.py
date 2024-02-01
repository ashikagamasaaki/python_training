"""
Iterator(ふるまい)

コレクションの内部構造を隠ぺいする

Aggregate     →     Iterator
↑                     ↑
ConcreteAggregate ←  ConcreteIterator

・Iterator：コレクションを探索するために必要な操作を定義するIF

・ConcreteIterator：Iteratorの定義を実装する

・Aggregate：探索を行うコレクションを表すIF

・ConcreteAggregate：Aggregateで定義したメソッドを実装

"""
from abc import ABCMeta, abstractmethod

class Patient:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}'
        

class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self):
        pass
        

class IIterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self):
        pass

# ConcreteAggregate
class WaitingRoom(Aggregate):
    def __init__(self):
        self.__patients = []
        
    def get_patients(self) -> list[Patient]:
        return self.__patients

    def get_count(self) -> int:
        return len(self.__patients)
    
    def check_in(self, patient: Patient):
        self.__patients.append(patient)

    def get_iterator(self) -> IIterator:
        return WaitingRoomIterator(self)

# ConcreteIterator
class WaitingRoomIterator(IIterator):
    def __init__(self, aggregate: WaitingRoom):
        self.__aggregate = aggregate
        self.__position = 0
    
    def has_next(self) -> bool:
        return self.__aggregate.get_count() > (self.__position)
    
    def next(self) -> Patient:
        if not self.has_next():
            print('患者がいません')
            return
        
        patient = self.__aggregate.get_patients()[self.__position]
        self.__position += 1
        return patient


if __name__ == '__main__':
    
    p1 = Patient(1, 'Tanaka')
    p2 = Patient(2, 'Sato')
    p3 = Patient(3, 'Suzuki')
    p4 = Patient(4, 'Saito')
    
    patients = []
    patients.append(p1)
    
    waiting_room = WaitingRoom()
    waiting_room.check_in(p1)
    waiting_room.check_in(p2)
    waiting_room.check_in(p3)
    
    
    waiting_room_iterator = waiting_room.get_iterator()
    print(waiting_room_iterator.has_next())
    print(waiting_room_iterator.next())
    print(waiting_room_iterator.next())
    print(waiting_room_iterator.next())
    print(waiting_room_iterator.next())
    
    