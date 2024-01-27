class UserId:
    def __init__(self, id):
        if id is None:
            raise ValueError('IDは必須です。')
        elif len(id) > 20:
            raise ValueError('IDは20文字以内で設定してください。')
        
        self.__id = id

    @property
    def Id(self):
        return self.__id
    
    @Id.setter
    def Id(self, id):
        self.__id = id
    
class UserName:
    def __init__(self, name):
        if name is None:
            raise ValueError('Nameは必須です。')
        elif len(name) > 100:
            raise ValueError('Nameは100文字以内で設定してください。')
        
        self.__name = name

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, name):
        self.__name = name

class User:
    def __init__(self, userId: UserId, userName: UserName) -> None:
        if type(userId) is not UserId:
            raise TypeError('ユーザIDにはUserIdクラスを代入してください')
        
        if type(userName) is not UserName:
            raise TypeError('ユーザ名にはUserNameクラスを代入してください')
        
        self.__userId = userId
        self.__userName = userName

    @property
    def UserId(self):
        return self.__userId
    
    @UserId.setter
    def UserId(self, id: UserId):
        self.__userId = id
    
    @property
    def UserName(self):
        return self.__userName
    
    @UserName.setter
    def UserName(self, name: UserName):
        self.__userName = name

def createUser(id: str, name: str) -> User:
    user_id = UserId(id)
    user_name = UserName(name)
    user = User(user_id, user_name)
    return user

def updateUser(new_id: str, new_name: str, user: User) -> None:
    user.UserId.Id = new_id
    user.UserName.Name = new_name


user_id_1 = UserId('10001')
user_name_1 = UserName('Tanaka Taro')
user_1 = User(user_id_1, user_name_1)
# user_1 = User(user_name_1, user_id_1)

print('UserIdクラスのid = ', user_id_1.Id)
print('UserNameクラスのname = ', user_name_1.Name)
print(f'UserクラスのUserID.Id = {user_1.UserId.Id}, UserクラスのUserName.Name = {user_1.UserName.Name}')

user_2 = createUser('10002', 'Sato Shiori')
print(f'UserクラスのUserID.Id = {user_2.UserId.Id}, UserクラスのUserName.Name = {user_2.UserName.Name}')

updateUser('10003', 'Fujiwara Michizane', user_2)
print(f'UserクラスのUserID.Id = {user_2.UserId.Id}, UserクラスのUserName.Name = {user_2.UserName.Name}')