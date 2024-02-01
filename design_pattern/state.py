"""
State(ふるまい)

・複数の状態を別個のクラスとして定義
・状態が変化したときにふるまいを変える

Context  →    State
              ↑      ↑
ConcreteState1    ConcreteState2


"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod

class LightState(metaclass=ABCMeta):
    @abstractmethod
    def switch(self) -> LightState:
        pass

class OffState(LightState):
    def switch(self) -> LightState:
        print('ライトを点灯します。')
        return OnState()

class OnState(LightState):
    def switch(self) -> LightState:
        print('ライトを消灯します。')
        return OffState()
    
class LightSwitch:
    def __init__(self):
        self.__state = OffState()
    
    def swith(self):
        self.__state = self.__state.switch()

if __name__ == '__main__':
    light_switch = LightSwitch()
    light_switch.swith()
    light_switch.swith()
    light_switch.swith()