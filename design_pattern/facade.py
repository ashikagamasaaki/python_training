"""
Facade(構造)

・ClientにシンプルなIFを提供
・システム内部のクラス同士の関係を知っている
・クラス内部の複雑な処理を隠ぺいできる

〇その他クラスの構成要素を隠ぺいできる
〇クライアントとその他クラスの結びつきを弱める
×神クラスとなる可能性あり
"""

class Product:
    def get_product(self, name: str):
        print(f'{name}を取得しました。')

class Payment:
    def make_payment(self, name: str):
        print(f'{name}の支払いが完了しました。')

class Invoice:
    def send_invoice(self, name: str):
        print(f'{name}の請求書を送付しました。')


class Order:
    def place_order(self, name:str):
        product = Product()
        payment = Payment()
        invoice = Invoice()
        
        print('注文開始')
        product.get_product(name)
        payment.make_payment(name)
        invoice.send_invoice(name)
        print('注文が正常に完了しました。')


if __name__ == '__main__':
    order = Order()
    order.place_order('デザインパターン書籍')