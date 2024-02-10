from abc import ABC, abstractmethod

# Product
class CreditCard(ABC):
    def __init__(self, owner):
        self.__owner = owner
    
    def get_owner(self):
        return self.__owner
    
    @abstractmethod
    def get_card_type(self):
        pass
    
    @abstractmethod
    def get_annual_charge(self):
        pass
    
    def __str__(self):
        return f'{self.__owner}様のカード: カードタイプは {self.get_card_type()}, 限度額は {self.get_annual_charge()}'
    
class Platinum(CreditCard):
    def get_card_type(self):
        return 'Platinum'
    
    def get_annual_charge(self):
        return 100000
    
class Gold(CreditCard):
    def get_card_type(self):
        return 'Gold'
    
    def get_annual_charge(self):
        return 50000
    

class CreditCardFactory(ABC):
    def create(self, owner: str):
        product = self.create_credit_card(owner)
        self.register_credit_card(product)
        return product
        
    @abstractmethod
    def create_credit_card(self, owner: str):
        pass
    
    @abstractmethod
    def register_credit_card(self, product: CreditCard):
        pass

credit_card_database: list[CreditCard] = []

class PlatinumCreditCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str):
        return Platinum(owner)

    def register_credit_card(self, platinum_card: CreditCard):
        credit_card_database.append(platinum_card)


class GoldCreditCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str):
        return Gold(owner)

    def register_credit_card(self, gold_card: CreditCard):
        credit_card_database.append(gold_card)


platinum_a = PlatinumCreditCardFactory()
print(platinum_a.create('Tanaka'))

gold_a = GoldCreditCardFactory()
print(gold_a.create('Suzuki'))


