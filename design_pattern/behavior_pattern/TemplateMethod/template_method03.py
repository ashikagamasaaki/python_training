from abc import ABC, abstractmethod

class AbstractPost(ABC):
    def _post(self):
        self.before_post()
        self.posting()
        self.after_post()
        self.additional_post()
        
    @abstractmethod
    def before_post(self):
        pass
        
    @abstractmethod
    def posting(self):
        pass
        
    @abstractmethod
    def after_post(self):
        pass
        
    def additional_post(self):
        pass
    

class TwitterPost(AbstractPost):
    def __init__(self, user, content):
        self.__user = user
        self.__contet = content
    
    def before_post(self):
        before_content = '-' * 10 + '↓ 投稿内容 ↓' + '-' * 10
        print(before_content)
        
    def posting(self):
        print(self.__contet)
    
    def after_post(self):
        after_content = '-' * 10 + self.__user + '-' * 10
        print(after_content)

    

class InstagramPost(AbstractPost):
    def __init__(self, user, content, photo):
        self.__user = user
        self.__contet = content
        self.__photo = photo
    
    def before_post(self):
        before_content = '*' * 20 + ' this is posts ' + '*' * 20
        print(before_content)
        
    def posting(self):
        print(self.__photo)
        print(self.__contet)
        
    def after_post(self):
        after_content = '*' * 20 + ' post by ' + self.__user + '-' * 20
        print(after_content)
    
twitter = TwitterPost('Taro', 'hogehoge. fugafuga.')
twitter._post()

print('')

instagram = InstagramPost('Hanako', 'pikopiko. nullnull.', 'hanako.png')
instagram._post()