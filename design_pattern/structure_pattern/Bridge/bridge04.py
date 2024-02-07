from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self):
        pass
    
class MailSender(MessageSender):
    def __init__(self, msg):
        self.__msg = msg
    
    def send(self):
        return f'メールでメッセージを送信: {self.__msg}'
    
class LineSender(MessageSender):
    def __init__(self, msg):
        self.__msg = msg
    
    def send(self):
        return f'LINEでメッセージを送信: {self.__msg}'
    
class DmSender(MessageSender):
    def __init__(self, msg):
        self.__msg = msg
    
    def send(self):
        return f'DMでメッセージを送信: {self.__msg}'
    

class MessageDevice(ABC):
    def __init__(self, message_sender: MessageSender):
        self._message_sender = message_sender
    
    @abstractmethod
    def message_send(self):
        pass
    
class MessageAndroid(MessageDevice):
    def message_send(self):
        msg = self._message_sender.send()
        return f'{msg}(Androidから送信です。)'
    
class MessageApple(MessageDevice):
    def message_send(self):
        msg = self._message_sender.send()
        return f'{msg}(iphoneから送信です。)'
    

line_msg = LineSender('やっほー。')
android = MessageAndroid(line_msg)
print(android.message_send())