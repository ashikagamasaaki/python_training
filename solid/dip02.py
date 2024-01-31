from abc import ABC, abstractmethod

class User:
    def __init__(self, name: str):
        self.name = name
    
class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

class SQLiteUserRepository(UserRepository):
    def add(self, user: User) -> None:
        # DB接続
        query = f"INSERT INTO users (name) VALUES ('{user.name}')"
        # クエリ発行、DB開放

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []
        
    def add(self, user: User) -> None:
        self.users.append(user)
    
class UserApplicationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
    def register_user(self, name: str) -> None:
        user = User(name)
        self.user_repository.add(user)