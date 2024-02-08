"""
Strategy
様々な戦略を実装して選択して利用する

・Strategy: 戦略を利用するためのIF
・ConcreteStrategy: Strategyの実装
・Context: 状況に合わせてStrategyを設定して実行する
"""

from abc import ABC, abstractmethod
from enum import Enum
from random import randint

class Hand_Type(Enum):
    
    GUU = 0
    CHOKI = 1
    PAA = 2
    
    
class Hand:
    
    def __init__(self, hand_index):
        if not hand_index in (0, 1, 2):
            raise Exception('値が誤っています。')
        
        self.hand_index = hand_index
        
        
    def is_win(self, other):
        if any((
            (self.hand_index == Hand_Type.GUU.value and other.hand_index == Hand_Type.CHOKI.value),
            (self.hand_index == Hand_Type.CHOKI.value and other.hand_index == Hand_Type.PAA.value),
            (self.hand_index == Hand_Type.PAA.value and other.hand_index == Hand_Type.GUU.value)
        )):
            return True
        return False
    
    
    def is_lose(self, other):
        if any((
            (self.hand_index == Hand_Type.GUU.value and other.hand_index == Hand_Type.PAA.value),
            (self.hand_index == Hand_Type.CHOKI.value and other.hand_index == Hand_Type.GUU.value),
            (self.hand_index == Hand_Type.PAA.value and other.hand_index == Hand_Type.CHOKI.value)
        )):
            return True
        return False
    

class Strategy:
    
    @abstractmethod
    def next_hand(self):
        pass
    
    @abstractmethod
    def study(self, is_win):
        pass

# 勝った場合は同じ手を出す
class SimpleStrategy(Strategy):
    
    def __init__(self):
        self.hand = None
        self.is_win = False
        
    def next_hand(self):
        if not self.is_win:
            self.hand = Hand(randint(0, 2))
        return self.hand
    
    def study(self, is_win):
        self.is_win = is_win
        

# 前回出した手から、次に出す手のうち最も買っているものを考えて出す
class ComplexStrategy(Strategy):
    def __init__(self):
        self.current_hand = None
        self.prev_hand = None
        self.histories = [[0,0,0],[0,0,0],[0,0,0]]
    
    def next_hand(self):
        if self.current_hand:
            self.prev_hand = self.current_hand
        self.current_hand = self.__get_most_winning_hand()
        return self.current_hand
    
    def __get_most_winning_hand(self):
        if not self.prev_hand:
            return Hand(randint(0, 2))
        tmp_hand = 0
        if self.histories[self.prev_hand.hand_index][1] > self.histories[self.prev_hand.hand_index][tmp_hand]:
            tmp_hand = 1
        if self.histories[self.prev_hand.hand_index][2] > self.histories[self.prev_hand.hand_index][tmp_hand]:
            tmp_hand = 2
        return Hand(tmp_hand)
        
    
    def study(self, is_win):
        if not self.prev_hand:
            return
        if is_win:
            self.histories[self.prev_hand.hand_index][self.current_hand.hand_index] += 1
        else:
            self.histories[self.prev_hand.hand_index][(self.current_hand.hand_index + 1) % 3] += 1
            self.histories[self.prev_hand.hand_index][(self.current_hand.hand_index + 2) % 3] += 1
            

class Player:
    
    def __init__(self, name, strategy: Strategy):
        self.name = name
        self.strategy = strategy
        self.win_count = 0
        self.lose_count = 0
        self.game_count = 0
        
    def next_hand(self):
        return self.strategy.next_hand()
    
    def win(self):
        self.strategy.study(True)
        self.win_count += 1
        self.game_count += 1
        
    def lose(self):
        self.strategy.study(False)
        self.win_count += 1
        self.game_count += 1
        
    def even(self):
        self.game_count += 1
        
    def __str__(self):
        return f'{self.name}: {self.game_count}, games: {self.win_count} win, {self.lose_count} lose.'

hand1 = Hand(0)
hand2 = Hand(2)

print(hand1.is_win(hand2))