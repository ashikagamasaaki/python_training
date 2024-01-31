from abc import ABC, abstractmethod

#　ユーザーを表現するクラス
class User:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name
        
    @property
    def id(self):
        return self._id
        
    @property
    def name(self):
        return self._name
    

class UserRepository(ABC):
    def save(self, user: User) -> None:
        pass
    
    def get(self, id: int) -> User:
        pass

# RDBへのアクセスを担当するクラス
class RDBUserRepository(UserRepository):
    def save(self, user: User) -> None:
        print(f'Save {user.name} to the RDB')  # 疑似的なRDBへの保存処理

    def get(self, id: int) -> User:
        print(f'Get user from the RDB by id {id}')  # 疑似的なRDBからの取得処理
        return User(id, 'user_name')
    
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}
    
    def save(self, user: User) -> None:
        self.users[user.id] = user
    
    def get(self, id: int) -> User:
        return self.users.get(id, 'Not Found!!!!')

# ユーザーに関するユースケースを実現するクラス
class UserApplicationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, id: int, name: str):
        user = User(id, name)
        self.user_repository.save(user)


user1 = User(1, 'Tanaka Taro')
user2 = User(2, 'Suzuki Jiro')

print(f'ID: {user1.id}, Name: {user1.name}')
print(f'ID: {user2.id}, Name: {user2.name}')
