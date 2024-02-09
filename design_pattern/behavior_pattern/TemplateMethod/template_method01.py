"""
Template Method（ふるまい）

AbstractClass
↑
ConcreteClass

〇共通処理を親クラスにまとめることができる
〇処理全体の流れは変えずに、子クラスごとで一部の処理を変更できる
×親クラスに処理全体の流れが決められるため、子クラスの拡張は制限される
×子クラスで親クラスのメソッドの振る舞いを変えると、LSPに違反する
"""

from abc import ABCMeta, abstractmethod

class TestTemplate(metaclass=ABCMeta):
    def test(self):
        self.setup()
        self.execute()
        self.teardown()
    
    @abstractmethod
    def setup(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    def teardown(self):
        print('teardown')


class ItemServiceTest(TestTemplate):
    def setup(self):
        print('setup: ItemServiceTest')
        
    def execute(self):
        print('execute: ItemServiceTest')
        


class UserServiceTest(TestTemplate):
    def setup(self):
        print('setup: UserServiceTest')
        
    def execute(self):
        print('execute: UserServiceTest')
        
        
if __name__ == '__main__':
    itemServiceTest = ItemServiceTest()
    userServiceTest = UserServiceTest()
    
    itemServiceTest.test()
    print('')
    userServiceTest.test()