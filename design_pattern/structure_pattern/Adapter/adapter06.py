from abc import ABC, abstractmethod

# Target
class MessageService(ABC):
    @abstractmethod
    def new_send(self):
        pass

# Adaptee
class MailMessage:
    def __init__(self, msg):
        self.__msg = msg
    
    def send(self):
        return f'メッセージを送信(メール): {self.__msg}'

# Adapter
class MessageServiceAdapter(MailMessage, MessageService):
    def __init__(self, msg):
        super().__init__(msg)
    
    def new_send(self):
        message = self.send()
        return message + ' **Adapter経由で送信'
    
adapter = MessageServiceAdapter('おはようございます。今から業務を始めます。')
print(adapter.new_send())