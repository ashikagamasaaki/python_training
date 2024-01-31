from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

class GasolineEngine(Engine):
    def start(self) -> None:
        print('ガソリンエンジンが始動しました')
        
class ElectricEngine(Engine):
    def start(self) -> None:
        print('電気モーターが始動しました')


class Tire(ABC):
    def is_inflated(self) -> bool:
        if self._pressure >= 1:
            return True
        else:
            print('タイヤに空気を入れてください')
            return False
    
    @abstractmethod
    def use_air(self) -> None:
        pass
    
    
class NormalTires(Tire):
    def __init__(self) -> None:
        self._pressure: int = 100

    def use_air(self) -> None:
        self._pressure -= 1
        
    
class AllSeasonTires(Tire):
    def __init__(self) -> None:
        self._pressure: int = 150

    def use_air(self) -> None:
        self._pressure -= 5


class Car:
    def __init__(self, engine: Engine, tires: Tire) -> None:
        self.engine = engine
        self.tires = tires

    def start(self) -> None:
        if self.tires.is_inflated():
            self.engine.start()
            self.tires.use_air()
            print('車が発進しました')


car1 = Car(GasolineEngine(), NormalTires())
car2 = Car(ElectricEngine(), AllSeasonTires())

car1.start()
car2.start()
