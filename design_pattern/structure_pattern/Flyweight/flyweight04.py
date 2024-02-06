from abc import ABC, abstractmethod

class Character(ABC):
    def display_info(self):
        pass

class SharedCharacter(Character):
    def __init__(self, appearance, skill):
        self._appearance = appearance
        self._skill = skill
    
    def display_info(self):
        print(f'共通キャラクター  Appearance: {self._appearance}, Skill: {self._skill}')
    
class UniqueCharacter(Character):
    def __init__(self, name, appearance, skill):
        self._name = name
        self._appearance = appearance
        self._skill = skill
    
    def display_info(self):
        print(f'ユニークキャラクター  Name: {self._name}, Appearance: {self._appearance}, Skill: {self._skill}')

class CharacterFactory:
    __shared_characters: dict[str, SharedCharacter] = {}
        
    @classmethod
    def get_shared_character(cls, appearance, skill):
        if appearance in cls.__shared_characters:
            cls.__shared_characters[appearance]._skill = skill
            return cls.__shared_characters.get(appearance)
        else:
            shared_character = SharedCharacter(appearance, skill)
            cls.__shared_characters[appearance] = shared_character
            return shared_character
            
    @classmethod
    def create_unique_character(self, name, appearance, skill):
        unique_character = UniqueCharacter(name, appearance, skill)
        return unique_character
    
share_char1 = CharacterFactory.get_shared_character('Human', 'Sword Master')
share_char2 = CharacterFactory.get_shared_character('Elf', 'Archery')
share_char3 = CharacterFactory.get_shared_character('Human', 'Knuckle')

unique_char1 = CharacterFactory.create_unique_character("Alice", "Human", "Magic")
unique_char2 = CharacterFactory.create_unique_character("Bob", "Elf", "Stealth")

share_char1.display_info()
share_char2.display_info()
share_char3.display_info()
unique_char1.display_info()
unique_char2.display_info()