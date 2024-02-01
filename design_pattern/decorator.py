"""
Decorator(構造)

・基本となるOBJに対して、柔軟に機能を追加
・継承よりも柔軟（不要な機能は追加しない）

             Component
              ↑     ↑
ConcreteComponent   Decorator
                     ↑
                     ConcreteDecorator

・機能追加が簡単
・複数の機能を組み合わせることも可能
×組み合わせた機能から特定の機能を削除することは難しい
"""

from abc import ABCMeta, abstractmethod
from datetime import datetime

class Component(metaclass=ABCMeta):
    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass
    
    
class Decorator(Component, metaclass=ABCMeta):
    def __init__(self, component: Component):
        self._component = component
    
    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass
    
    
class Logger(Component):
    def get_log_message(self, msg: str) -> str:
        return msg

    
class TimestampDecorator(Decorator):
    def __init__(self, component: Component):
        super().__init__(component)
    
    def get_log_message(self, msg: str) -> str:
        now = datetime.now()
        return self._component.get_log_message(f'{msg}: timestamp is = [{now}]')

    
class LogLevelDecorator(Decorator):
    def __init__(self, log_level: str, component: Component):
        super().__init__(component)
        self.__log_level = log_level
        
    def get_log_message(self, msg: str) -> str:
        return self._component.get_log_message(f'{msg}: log_level = [{self.__log_level}]')
    
    
if __name__ == '__main__':
    logger = Logger()
    log_level_logger = LogLevelDecorator('INFO', logger)
    timestamp_logger = TimestampDecorator(log_level_logger)
    print(logger.get_log_message('Design Pattern!'))
    print(log_level_logger.get_log_message('Design Pattern!'))
    print(timestamp_logger.get_log_message('Design Pattern!'))
    