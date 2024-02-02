"""
Factory Method(生成)


Creator     →      Product
↑                     ↑
ConcreteCreator ←  ConcreteProduct

・Creator：Productを生成する抽象クラス

・ConcreteCreator：製品生成のための具体的な方法を実装、ConcreteProductクラスのインスタンスを返却

・Product：Creatorで生成される抽象クラス、IF

・ConcreteProduct：Productの製品、機能を実装
"""

from abc import ABCMeta, abstractmethod

class CreditCard(metaclass=ABCMeta):
    def __init__(self, owner: str):
        self.__owner = owner
    
    @property
    def owner(self) -> str:
        return self.__owner
    
    @abstractmethod
    def get_card_type(self) -> str:
        pass
    
    @abstractmethod
    def get_annual_charge(self) -> int:
        pass


class Platinum(CreditCard):
    def get_card_type(self) -> str:
        return 'Platinum'

    def get_annual_charge(self) -> int:
        return 30000


class Gold(CreditCard):
    def get_card_type(self) -> str:
        return 'Gold'

    def get_annual_charge(self) -> int:
        return 10000


class CreditCardFactory(metaclass=ABCMeta):
    def create(self, owner: str) -> CreditCard:
        credit_card = self.create_credit_card(owner)
        self.register_credit_card(credit_card)
        return credit_card
    
    @abstractmethod
    def create_credit_card(self, owner: str):
        pass
    
    @abstractmethod
    def register_credit_card(self, credit_card: CreditCard):
        pass


credit_card_database: list[CreditCard] = []


class PlatinumCreditCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str) -> CreditCard:
        return Platinum(owner)
    
    def register_credit_card(self, credit_card: CreditCard):
        credit_card_database.append(credit_card)


class GoldCreditCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str) -> CreditCard:
        return Gold(owner)
    
    def register_credit_card(self, credit_card: CreditCard):
        credit_card_database.append(credit_card)
        
        
if __name__ == '__main__':
    platinum_card_factory = PlatinumCreditCardFactory()
    platinum_card = platinum_card_factory.create('Tanaka')
    print(platinum_card.get_card_type())
    
    gold_card_factory = GoldCreditCardFactory()
    gold_card = gold_card_factory.create('Suzuki')
    print(gold_card.get_card_type())
    
    print(credit_card_database)