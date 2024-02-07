"""
Command(ふるまい)

・命令をメソッドではなく、独立したクラスとして表現する

    Command  ←  Invoker
      ↑
  ConcreteCommand  →  Receiver

・複数の命令をひとまとめに実行したい
・命令を再利用して組み合わせることで１つの命令を生成することが可能
・命令をキューに入れて遅延実行したい
"""

from abc import ABCMeta, abstractmethod

class File:
    def __init__(self, name: str):
        self.__name = name
        
    def open(self):
        print(f'{self.__name}が開かれました')
        
    def compress(self):
        print(f'{self.__name}が圧縮されました')
        
    def close(self):
        print(f'{self.__name}が閉じられました')

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
    
class OpenCommand(Command):
    def __init__(self, file: File):
        self.__file = file
    
    def execute(self):
        self.__file.open()
    
class CompressCommand(Command):
    def __init__(self, file: File):
        self.__file = file
    
    def execute(self):
        self.__file.compress()
    
class CloseCommand(Command):
    def __init__(self, file: File):
        self.__file = file
    
    def execute(self):
        self.__file.close()
        
class Queue:
    def __init__(self):
        self.__commands = []
        
    def add_command(self, command: Command):
        self.__commands.append(command)
        
    def execute_command(self):
        for command in self.__commands:
            command.execute()
            

if __name__ == '__main__':
    
    file = File('command.py')
    queue = Queue()
    queue.add_command(OpenCommand(file))
    queue.add_command(CompressCommand(file))
    queue.add_command(CloseCommand(file))
    
    queue.execute_command()