from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self):
        self.__name = None
        self.__age = 0
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
    
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age
        
    @abstractmethod
    def speak(self):
        pass

class Warrior(Character):
    def speak(self):
        print(f'こんにちは！Warriorの{self.name}です。{self.age}歳です。よろしくお願いします。')
        
class Mage(Character):
    def speak(self):
        print(f'おはよう！Mageの{self.name}だよ。{self.age}歳。よろしくね。')
        
class Rogue(Character):
    def speak(self):
        print(f'こんばんは！Rogueの{self.name}だぜ。{self.age}歳だ。よろしくな。')

class CharacterFactory(ABC):
    def __init__(self):
        self.chara_list: list[Character] = []
        
    def create(self, name: str, age: int):
        chara = self.chara_create(name, age)
        self.chara_register(chara)
        return chara
    
    @abstractmethod
    def chara_create(self):
        pass
    
    @abstractmethod
    def chara_register(self, chara: Character):
        pass
    
    def get_list(self):
        for chara in self.chara_list:
            print(f'name: {chara.name}, age: {chara.age}歳')
        
class WarriorFactory(CharacterFactory):
    # def __inin__(self):
    #     super().__init__()
    
    def chara_create(self, name: str, age: int):
        chara = Warrior()
        chara.name = name
        chara.age = age
        return chara
    
    def chara_register(self, chara: Character):
        self.chara_list.append(chara)
        
class MageFactory(CharacterFactory):
    def chara_create(self, name: str, age: int):
        chara = Mage()
        chara.name = name
        chara.age = age
        return chara
    
    def chara_register(self, chara: Character):
        self.chara_list.append(chara)
        
class RogueFactory(CharacterFactory):
    def chara_create(self, name: str, age: int):
        chara = Rogue()
        chara.name = name
        chara.age = age
        return chara
    
    def chara_register(self, chara: Character):
        self.chara_list.append(chara)
        

wfactory = WarriorFactory()
w_tanaka = wfactory.create('Tanaka Taro', 20)
w_saito = wfactory.create('Saito Hajime', 26)
w_suzuki = wfactory.create('Suzuki Shinichi', 17)

w_tanaka.speak()
w_saito.speak()
w_suzuki.speak()

wfactory.get_list()

print('##########################################')

mfactory = MageFactory()
m_tanaka = mfactory.create('Tanaka Taro', 20)
m_saito = mfactory.create('Saito Hajime', 26)
m_suzuki = mfactory.create('Suzuki Shinichi', 17)

m_tanaka.speak()
m_saito.speak()
m_suzuki.speak()

mfactory.get_list()