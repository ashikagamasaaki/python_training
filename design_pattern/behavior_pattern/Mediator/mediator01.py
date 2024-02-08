"""
Mediator(ふるまい)

関連するOBJのやり取りを仲介する
やり取りを制限することでOBJ同士の結びつきを弱める

                       Mediator
               ↑                        ↑
ConcreteMediator → ConcreteColleague1 → Colleague
               ↓                        ↑
                   ConcreteColleague2

"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def register_user(self, user: User):
        pass
    
    @abstractmethod
    def send_message(self, msg: str, sendUser: User):
        pass
    
class ChatRoom(Mediator):
    def __init__(self):
        self.__members: [User] = []
        
    def register_user(self, user: User):
        self.__members.append(user)
    
    def send_message(self, msg: str, send_user: User):
        for member in self.__members:
            if member != send_user:
                member.receive(msg)
        

class User(metaclass=ABCMeta):
    def __init__(self, mediator: Mediator, name: str):
        self._mediator = mediator
        self._name = name
    
    @abstractmethod
    def send(self, msg: str):
        pass
    
    @abstractmethod
    def receive(self, msg: str):
        pass
    
    
class ChatUser(User):
    def __init__(self, mediator: Mediator, name: str):
        super().__init__(mediator, name)
    
    def send(self, msg: str):
        print(f'{self._name} -> メッセージ送信')
        self._mediator.send_message(f'{msg} from {self._name}', self)
        
    def receive(self, msg: str):
        print(f'{self._name} -> メッセージ受信: {msg}')



if __name__ == '__main__':
    chat_room = ChatRoom()
    tanaka = ChatUser(chat_room, 'Tanaka')
    sato = ChatUser(chat_room, 'Sato')
    goto = ChatUser(chat_room, 'Goto')
    
    chat_room.register_user(tanaka)
    chat_room.register_user(sato)
    chat_room.register_user(goto)
    
    
    tanaka.send('こんにちは')
    sato.send('こんばんは')
    