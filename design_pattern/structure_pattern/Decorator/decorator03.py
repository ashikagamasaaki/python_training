from abc import ABC, abstractmethod

# Component
class INotifier(ABC):
    def __init__(self, send_method=None):
        self.__send_method = send_method
    
    @abstractmethod
    def notify(self, msg: str):
        pass
    
    @property
    def sendMethod(self):
        return self.__send_method
    
# ConcreteComponent
class Notifier(INotifier):
    def notify(self, msg: str):
        return msg
        
# BaseDecorator
class INotifyDecorator(INotifier, ABC):
    def __init__(self, send_method: str, component: INotifier):
        super().__init__(send_method)
        self._component = component
    
    @abstractmethod
    def notify(self, msg: str):
        pass

# ConcreteDecorator
class MailNotifyDecorator(INotifyDecorator):
    def __init__(self, component):
        super().__init__('Mail', component)
        
    def notify(self, msg: str):
        notify_msg = self._component.notify(msg)
        return f'{self.sendMethod}通知: {notify_msg}'

# ConcreteDecorator
class SnsNotifyDecorator(INotifyDecorator):
    def __init__(self, component):
        super().__init__('SNS', component)
        
    def notify(self, msg: str):
        notify_msg = self._component.notify(msg)
        return f'{self.sendMethod}通知: {notify_msg}'

# ConcreteDecorator
class LineNotifyDecorator(INotifyDecorator):
    def __init__(self, component):
        super().__init__('LINE', component)
        
    def notify(self, msg: str):
        notify_msg = self._component.notify(msg)
        return f'{self.sendMethod}通知: {notify_msg}'
    
notifier = Notifier()
print(notifier.notify('本日はシステムメンテナンスのため休止します'))

mail_notifier = MailNotifyDecorator(notifier)
print(mail_notifier.notify('本日はシステムメンテナンスのため休止します'))

sns_mail_notifier = SnsNotifyDecorator(mail_notifier)
print(sns_mail_notifier.notify('本日はシステムメンテナンスのため休止します'))

line_sns_mail_notifier = LineNotifyDecorator(SnsNotifyDecorator(mail_notifier))
print(line_sns_mail_notifier.notify('本日はシステムメンテナンスのため休止します'))