from __future__ import annotations
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, mediator: Mediator, name):
        self._mediator = mediator
        mediator.register_user(self)
        self._name = name
    
    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass

class ChatUser(User):
    def send(self, msg):
        print(f'メッセージ送信: {msg} FROM {self._name} -----> ')
        self._mediator.send_message(msg, self)

    def receive(self, msg):
        print(f'------> メッセージ受信(TO {self._name}): {msg}')


class Mediator(ABC):
    @abstractmethod
    def register_user(self, user:User):
        pass

    @abstractmethod
    def send_message(self, msg:str, sendUser: User):
        pass


class ChatRoom(Mediator):
    def __init__(self):
        self.__members: list[User] = []

    def register_user(self, user: User):
        self.__members.append(user)

    def send_message(self, msg: str, sendUser: User):
        for member in self.__members:
            if member != sendUser:
                member.receive(msg)


chat_room = ChatRoom()
tanaka = ChatUser(chat_room, 'Tanaka')
yamada = ChatUser(chat_room, 'Yamada')
suzuki = ChatUser(chat_room, 'Suzuki')


tanaka.send('Hello World!!!')