"""
■リスコフの置換原則(LSP)
・継承のときに、親子のクラスは置換できる必要がある
・置換できるというのは、クライアント側から見て置換できる必要がある
・正方形 is a 長方形のように言葉として置換できても、クライアントから見て置換できなければNG

■基本型を派生型で置換できないのはどのような場合でしょうか
・派生形のほうが事前条件が厳しい
・派生形のほうが事後条件が緩い
・不変条件に違反（関数の開始時と正常終了時に共通して保証されるべき状態についての条件）
"""


"""
③商品を表現するProductクラスについて考えてみましょう

商品は以下のルールを持つとします
・名前は1文字以上20文字以内
・価格は1円以上
・割引率は5~50%
"""

class Product:
    def __init__(self, name: str, price: int) -> None:
        if len(name) < 1 or 20 < len(name):
            raise ValueError('名前は1文字以上20文字以内で入力してください。')
        if price < 1:
            raise ValueError('価格は1円以上で入力してください。')
        
        self._name = name
        self._price = price

    def discount(self, discount_percent: int) -> None:
        if discount_percent < 5 or 50 < discount_percent:
            raise ValueError('割引率は5~50%で入力してください。')
        self._price = self._price * (100 - discount_percent) // 100

    def change_name(self, new_name: str) -> None:
        if len(new_name) < 1 or 20 < len(new_name):
            raise ValueError('名前は1文字以上20文字以内で入力してください。')
        self._name = new_name