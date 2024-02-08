"""
Memento

オブジェクトの状態保存

・Originator: オブジェクトの状態を保存するクラス
・Memento: オブジェクトの状態の保存を行うIF
・ConcreteMemento: Mementoを具体化したクラス。特定のOriginatorに対しての状態を保存
・CareTaker: 特定のOriginatorに対してのバックアップや元に戻す処理を行う
"""

from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Originator:
    
    def __init__(self, state, name):
        self._state = state
        self._name = name
    
    def change_state(self, new_state):
        print(f'Change State 実行: {new_state}')
        self._state = new_state
        
    def change_name(self, name):
        print(f'Change Name 実行: {name}')
        self._name = name
        
    def __str__(self):
        return f'State: {self._state}, name: {self._name}'
    
    def save(self):
        return ConcreteMemento(self._state, self._name)
    
    def restore(self, memento):
        self._state = memento.state
        self._name = memento.name
        print(f'Originator: State Change to: {self._state}')


class Memento(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractproperty
    def date(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, state, name):
        self._state = state
        self._name = name
        self._date = datetime.now()

    @property
    def state(self):
        return self._state

    @property
    def name(self):
        return self._name
    
    @property
    def date(self):
        return self._date

    def get_name(self):
        return f'{self.date} / ({self.state})'


class CareTaker:
    def __init__(self):
        self._mementos = []
        
    def backup(self, memento: Memento):
        print(f'Originalの状態を保存: {memento.get_name()}')
        self._mementos.append(memento)
        
    def undo(self):
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        return memento
    
    def show_history(self):
        print('変更履歴')
        for memento in self._mementos:
            print(memento.get_name())


originator = Originator('FirstState', 'Originator 1')

care_taker = CareTaker()
backup_instance = originator.save()     # ConcreteMemento
care_taker.backup(backup_instance)      # CareTakerに保存

originator.change_state('Second Status')
originator.change_name('New Originator 1')

backup_instance = originator.save()
care_taker.backup(backup_instance)      # CareTakerに保存

care_taker.show_history()

originator.change_state('Third Status')
originator.change_name('New Originator 2')

undo_instance = care_taker.undo()
originator.restore(undo_instance)
print(originator)
