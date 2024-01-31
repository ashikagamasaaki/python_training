""" Parameter Objectパターンを使用した修正 """


from abc import ABC, abstractmethod

class DiscountParameters:
    def __init__(self, items: list):
        self._items = items

    @property
    def total_price(self) -> int:
        return sum(price for _, price in self._items)

    @property
    def item_count(self) -> int:
        return len(self._items)



class CouponStrategy(ABC):
    @abstractmethod
    # def apply_discount(self, price: int, items_count: int) -> int:  # 引数に商品数を追加
    def apply_discount(self, discount_param: DiscountParameters) -> int:
        pass

class PercentageDiscountCoupon(CouponStrategy):
    def __init__(self, percentage: int):
        self.percentage = percentage

    # def apply_discount(self, price: int, items_count: int = 0) -> int:  # 引数に商品数を追加
    def apply_discount(self, discount_param: DiscountParameters) -> int:
        return int(discount_param.total_price * (1 - self.percentage / 100))

class QuantityDiscountCoupon(CouponStrategy):
    # def apply_discount(self, price: int, items_count: int) -> int:
    def apply_discount(self, discount_param: DiscountParameters) -> int:
        if discount_param.item_count >= 10:
            return int(discount_param.total_price * 0.9)
        return discount_param.total_price

class ShoppingCart:
    def __init__(self, discount_strategy: CouponStrategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, item_name: str, price: int):
        self.items.append((item_name, price))

    def calculate_total(self) -> int:
        total = sum(price for _, price in self.items)
        discount_param = DiscountParameters(self.items)     # パラメータを１つにまとめる
        print('Total===>', total)
        # return self.discount_strategy.apply_discount(total)
        # return self.discount_strategy.apply_discount(total, len(self.items))    # 引数に商品数を追加
        return self.discount_strategy.apply_discount(discount_param)


percent_discount = PercentageDiscountCoupon(20)
quantity_discount = QuantityDiscountCoupon()

shopping_cart1 = ShoppingCart(percent_discount)
shopping_cart1.add_item('本', 2000)
shopping_cart1.add_item('靴', 4000)
shopping_cart1.add_item('鞄', 8000)
print(shopping_cart1.calculate_total())

shopping_cart2 = ShoppingCart(quantity_discount)
shopping_cart2.add_item('本', 2000)
shopping_cart2.add_item('靴', 4000)
shopping_cart2.add_item('鞄', 8000)
shopping_cart2.add_item('本', 2000)
shopping_cart2.add_item('靴', 4000)
shopping_cart2.add_item('鞄', 8000)
shopping_cart2.add_item('本', 2000)
shopping_cart2.add_item('靴', 4000)
shopping_cart2.add_item('鞄', 8000)
shopping_cart2.add_item('鞄', 8000)
print(shopping_cart2.calculate_total())
