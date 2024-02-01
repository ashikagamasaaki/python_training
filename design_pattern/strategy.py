"""
Strategy(ふるまい)

Context  →    Strategy
              ↑      ↑
ConcreteStrategy1    ConcreteStrategy2

"""

from abc import ABCMeta, abstractmethod

class PaymentStrategy(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, amount: int):
        pass

class CreditCarPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int):
        print(f'クレジットカードで{amount}円お支払い')

class CashCarPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int):
        print(f'現金で{amount}円お支払い')
        

class ShoppingCart:
    def __init__(self) -> None:
        self.__total = 0
        self.__items:dict[str:int] = {}
    
    def add_item(self, item: str, price: int):
        self.__items[item] = price
        self.__total = sum(value for value in self.__items.values())
    
    def pay(self, payment_strategy: PaymentStrategy):
        payment_strategy.pay(self.__total)

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.add_item('本', 2000)
    shopping_cart.add_item('鞄', 5400)
    shopping_cart.add_item('服', 1200)
    shopping_cart.pay(CreditCarPaymentStrategy())
    shopping_cart.pay(CashCarPaymentStrategy())