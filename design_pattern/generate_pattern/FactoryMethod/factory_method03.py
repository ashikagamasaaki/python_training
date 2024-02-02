"""
あるアプリケーションには、複数の通信プロトコルが存在します。
それぞれのプロトコルはメッセージの送信と受信を行いますが、実際の通信手段やメッセージのフォーマットは異なります。
Communicator インターフェースを使用し、具象クラスである EmailCommunicator および SMSCommunicator を作成してください。
また、これらの通信クラスのインスタンスを生成するための CommunicatorFactory クラスを実装してください。

・Product: 通信手段(ICommunicator)
・ConcreteProduct: EmailCommunicator、SMSCommunicator
・Factory: ICommunicatorFactory
・ConcreteFactory: CommunicatorFactory
"""
from abc import ABC, abstractmethod, abstractproperty

class ICommunicator(ABC):
    def __init__(self):
        self.__owner = None
        
    @property
    def owner(self):
        return self.__owner
        
    @owner.setter
    def owner(self, owner):
        self.__owner = owner
    
    @abstractmethod
    def getMsg(self):
        pass
    
    @abstractmethod
    def sendMsg(self):
        pass
    
class EmailCommunicator(ICommunicator):
    def getMsg(self):
        print(f'{self.owner}がメールを受信しました。')
        
    def sendMsg(self):
        print(f'{self.owner}がメールを送信しました。')
    
class LineCommunicator(ICommunicator):
    def getMsg(self):
        print(f'{self.owner}がLINEを受信しました。')
        
    def sendMsg(self):
        print(f'{self.owner}がLINEを送信しました。')
        
        
class ICommunicatorFactory(ABC):
    def create(self, communicate_owner: str):
        self._communicate_owner = communicate_owner
        communicator = self._createCommunicator()
        self._registerCommunicator(communicator)
        return communicator
    
    @abstractmethod
    def _createCommunicator(self):
        pass
    
    @abstractmethod
    def _registerCommunicator(self, communicator: ICommunicator):
        pass


class EmailCommunicatorFactory(ICommunicatorFactory):
    def _createCommunicator(self):
        return EmailCommunicator()
    
    def _registerCommunicator(self, communicator: ICommunicator):
        communicator.owner = self._communicate_owner



class LineCommunicatorFactory(ICommunicatorFactory):
    def _createCommunicator(self):
        return LineCommunicator()
    
    def _registerCommunicator(self, communicator: ICommunicator):
        communicator.owner = self._communicate_owner
        


email = EmailCommunicatorFactory()
email_communicator = email.create('田中')
email_communicator2 = email.create('佐藤')
email_communicator.sendMsg()
email_communicator2.getMsg()

line = LineCommunicatorFactory()
line_communicator = line.create('加藤')
line_communicator2 = line.create('山田')
line_communicator.sendMsg()
line_communicator2.getMsg()