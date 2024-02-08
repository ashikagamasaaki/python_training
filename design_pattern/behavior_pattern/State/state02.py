"""
State

状態を表すクラスを作成して、状態に応じた処理を実行して拡張性を高める

・State: 状態を表し、状態ごとに異なるふるまいをするIF
・ConcreteState: Stateの実装
・Context: ConcreteStateを利用し、Stateパターンに必要な処理を実装
"""


from abc import ABC, abstractmethod
from datetime import datetime

class State(ABC):
    @abstractmethod
    def begin(self):
        pass
    
    @abstractmethod
    def write_log(self):
        pass
    
    @abstractmethod
    def end(self):
        pass

class DayState(State):
    def begin(self):
        print('昼の処理を開始')
        
    def write_log(self):
        with open('tmp.txt', 'w', encoding='utf-8')as fh:
            fh.write('昼のログ')
    
    def end(self):
        print('昼の処理を終了')
        
class NightState(State):
    def begin(self):
        print('夜の処理を開始')
        
    def write_log(self):
        with open('tmp2.txt', 'w', encoding='utf-8')as fh:
            fh.write('夜のログ')
    
    def end(self):
        print('夜の処理を終了')



class Context:
    def __init__(self):
        self.__state = DayState()
        
    def do(self):
        self.change_state_by_time()
        self.__state.begin()    # stateで処理を実行して、stateの中に処理を書く
        self.__state.write_log()
        self.__state.end()
        
        
    def change_state(self, state: State):
        self.__state = state
    
    
    def change_state_by_time(self):
        now = datetime.now()
        if (now.hour < 6) or (now.hour >= 19):
            self.__state = NightState()
        else:
            self.__state = DayState()



context = Context()
# context.change_state(NightState())
context.do()
