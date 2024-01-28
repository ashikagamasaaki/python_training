"""
誤った例
トッピングが増えれば増えるほどクラスが増える。
↓
Decoratorパターンで解決する
"""
# class Coffee:
#     @property
#     def cost(self) -> int:
#         return
    
#     @property
#     def description(self) -> str:
#         return 'コーヒー'
    
# class CreamCoffee(Coffee):
#     @property
#     def cost(self) -> int:
#         return super().cost + 50
    
#     @property
#     def description(self) -> str:
#         return f'{super().description()}、生クリーム'

# class VanillaCoffee(Coffee):
#     @property
#     def cost(self) -> int:
#         return super().cost + 70
    
#     @property
#     def description(self) -> str:
#         return f'{super().description()}、バニラアイス'


""" Decorator使い方 """
from abc import ABC, abstractmethod
# コーヒーインターフェース
class AbstractCoffee(ABC):
    @property
    @abstractmethod
    def cost(self) -> int:
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        pass

# ベースのコーヒークラス
class Coffee(AbstractCoffee):
    @property
    def cost(self) -> int:
        return 200
    
    @property
    def description(self) -> str:
        return 'コーヒー'

# コーヒーのトッピングデコレーター
class CoffeeDecorator(AbstractCoffee, ABC):
    def __init__(self, decorated_coffee: AbstractCoffee):
        self.decorated_coffee = decorated_coffee
        
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost
    
    @property
    def description(self) -> str:
        return self.decorated_coffee.description


class CreamDecorator(CoffeeDecorator):
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost + 50
    
    @property
    def description(self) -> str:
        return f'{self.decorated_coffee.description}、生クリーム'


class VanillaDecorator(CoffeeDecorator):
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost + 70
    
    @property
    def description(self) -> str:
        return f'{self.decorated_coffee.description}、バニラアイス'
    

coffee = Coffee()
print(coffee.cost)
print(coffee.description)
print('#############################################')
coffee_creem_decorator = CreamDecorator(coffee)
print(coffee_creem_decorator.cost)
print(coffee_creem_decorator.description)
print('#############################################')
coffee_creem_vanilla_decorator = VanillaDecorator(coffee_creem_decorator)
print(coffee_creem_vanilla_decorator.cost)
print(coffee_creem_vanilla_decorator.description)


