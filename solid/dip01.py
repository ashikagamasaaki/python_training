from abc import ABC, abstractmethod

class ISwimming(ABC):
    @abstractmethod
    def swim(self) -> str:
        pass

class FastSwimming(ISwimming):
    def swim(self) -> str:
        return '速く泳ぐ'
    
class SlowSwimming(ISwimming):
    def swim(self) -> str:
        return 'ゆっくり泳ぐ'
    
    
class Fish(ISwimming):
    def __init__(self, swimming: ISwimming) -> None:
        self.swimming = swimming
    
    def swim(self) -> None:
        print(f'魚が{self.swimming.swim()}')
        

fast_swim = FastSwimming()
slow_swim = SlowSwimming()


fast_fish = Fish(fast_swim)
fast_fish.swim()
slow_fish = Fish(slow_swim) 
slow_fish.swim()