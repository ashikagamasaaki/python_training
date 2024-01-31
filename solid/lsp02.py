"""
④次のコードはLSPに違反しているでしょうか
違反している場合は、その理由を述べた上で、
LSPを満たすようにコードを改善してください


基本形のCouponStrategy.apply_discountよりも
派生形のQuantityDiscountCoupon.apply_discountの事前条件が強い(引数が追加されている。)

基本形の関数パラメータにも数量をとるように変更する
"""

from abc import ABC, abstractmethod

class CouponStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: int, items_count: int) -> int:  # 引数に商品数を追加
        pass

class PercentageDiscountCoupon(CouponStrategy):
    def __init__(self, percentage: int):
        self.percentage = percentage

    def apply_discount(self, price: int, items_count: int = 0) -> int:  # 引数に商品数を追加
        return int(price * (1 - self.percentage / 100))

class QuantityDiscountCoupon(CouponStrategy):
    def apply_discount(self, price: int, items_count: int) -> int:
        if items_count >= 10:
            return int(price * 0.9)
        return price

class ShoppingCart:
    def __init__(self, discount_strategy: CouponStrategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, item_name: str, price: int):
        self.items.append((item_name, price))

    def calculate_total(self) -> int:
        total = sum(price for _, price in self.items)
        print('Total===>', total)
        # return self.discount_strategy.apply_discount(total)
        return self.discount_strategy.apply_discount(total, len(self.items))    # 引数に商品数を追加


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
