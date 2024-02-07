"""
ChainOfResponsibility

複数の処理をつなげて処理したい
ブラウザでユーザが入力した処理に対して、
名前の綴りは適切か → パスワードは大文字、小文字を含むか → 確認用のパスワードと一致するか など

・Handler: 要求を処理するIF
・ConcreteHandler: Handlerを具体化したもの。自分で処理できる場合は処理して、処理できない場合は別のクラスに処理を回す。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    gender: str


class Handler(ABC):
    _next = None
    
    def set_next(self, handler):
        self._next = handler
        return handler
    
    def handle(self, user: User):
        if self.filter(user):
            return self.done(user)
        if self._next:
            return self._next.handle(user)
        return self.end(user)
    
    @abstractmethod
    def filter(self, user: User):
        pass
    
    def done(self, user: User):
        print(f'{user}は{self.__class__.__name__}でフィルタリングされました')
        return False

    def end(self, user: User):
        print(f'{user}の確認は完了しました')
        return True
    
class NameCheckHandler(Handler):
    def filter(self, user: User):
        if user.name in ['', None, 'Nanashi']:
            return True
        return False
    
class AgeCheckHandler(Handler):
    def filter(self, user: User):
        if (user.age < 0) or (user.age > 100):
            return True
        return False
    
class GenderCheckHandler(Handler):
    def filter(self, user: User):
        if user.gender not in ['Man', 'Woman']:
            return True
        return False



user1 = User('Taro', 18, 'Man')
user2 = User('Nanashi', 18, 'Man')
user3 = User('Taro', 200, 'Man')
user4 = User('Taro', 20, 'None')
name_handler = NameCheckHandler()
age_handler = AgeCheckHandler()
gender_handler = GenderCheckHandler()

# name_handler.set_next(age_handler).set_next(gender_handler)
# name_handler.handle(user1)
# name_handler.handle(user2)
# name_handler.handle(user3)
# name_handler.handle(user4)




valid_users = []

for user in [user1, user2, user3, user4]:
    if name_handler.handle(user):
        valid_users.append(user)
        
print(valid_users)