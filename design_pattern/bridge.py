"""
Bridge(構造)

・機能を提供するクラスと、実装を提供するクラスを独立させる
・目的と手段を分離する（委譲で「機能」と「実装」の橋渡しをする）

Abstraction      →     Implementor
     ↑                    ↑    
RefinedAbstraction    ConcreteImplementor
"""

from abc import ABCMeta, abstractmethod

class MessageApp(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass
        
class Line(MessageApp):
    def send(self):
        print('Lineからメッセージ送信')
    
class Twitter(MessageApp):
    def send(self):
        print('Twitterからメッセージ送信')
    
class Facebook(MessageApp):
    def send(self):
        print('Facebookからメッセージ送信')
        
        
class OS(metaclass=ABCMeta):
    def __init__(self):
        self._app = None
    
    def set_app(self, app: MessageApp):
        self._app = app

    @abstractmethod
    def send_message(self):
        pass
    
class IOS(OS):
    def send_message(self):
        print('IOSでメッセージ送信')
        
        if self._app:
            self._app.send()
        else:
            raise Exception('アプリが指定されていません')
    
class Android(OS):
    def send_message(self):
        print('Androidでメッセージ送信')
        
        if self._app:
            self._app.send()
        else:
            raise Exception('アプリが指定されていません')



if __name__ == '__main__':
    ios = IOS()
    android = Android()
    
    line = Line()
    twitter = Twitter()
    facebook = Facebook()
    
    ios.set_app(line)
    android.set_app(twitter)
    
    ios.send_message()
    android.send_message()