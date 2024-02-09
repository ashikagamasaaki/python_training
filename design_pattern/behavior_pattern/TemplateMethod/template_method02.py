"""
TemplateMethod
外部からは同じIFを使い、同じような呼び出し方をできるようにして具体的な処理はサブクラスに記述

・AbstractClass: 外部から実行されるテンプレートメソッド。テンプレートメソッドの中で利用される抽象メソッドを宣言
・ConcreteClass: AbstractClassを継承して抽象メソッドを定義
"""

from abc import ABC, abstractmethod

class AbstractDisplay(ABC):
    def display(self):
        self._open()
        for _ in range(5):
            self._print()
        
        self._close()
        self._additional_method()
    
    @abstractmethod
    def _open(self):
        pass
    
    @abstractmethod
    def _print(self):
        pass
    
    @abstractmethod
    def _close(self):
        pass
    
    # 継承先で定義してもいいし、しなくてもいい
    def _additional_method(self):
        pass

class CharDisplay(AbstractDisplay):
    def __init__(self, character):
        self.__character = character
        
    def _open(self):
        print('<<', end='')
    
    def _print(self):
        print(self.__character, end='')
        
    def _close(self):
        print('>>')
    
    def _additional_method(self):
        print('Additional method called')

class StringDisplay(AbstractDisplay):
    def __init__(self, msg):
        self.__msg = msg
        
    def _open(self):
        self.__print_line()
    
    def _print(self):
        print('|' + self.__msg + '|')
        
    def _close(self):
        self.__print_line()
            
    def __print_line(self):
        print('+' + '-' * len(self.__msg) + '+')
    

c_display = CharDisplay('*')
c_display.display()

s_display = StringDisplay('Hello')
s_display.display()