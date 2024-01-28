class Payment:
    def pay(self, amount: int, method: str) -> None:
        if method == 'cash':
            # 現金決済の処理
            print(f'{amount}円を現金で支払いました。')
        elif method == 'credit_card':
            # クレジットカード決済の処理
            print(f'{amount}円をクレジットカードで支払いました。')
        elif method == 'QRPay':
            # QRコード決済の処理
            print(f'{amount}円をQRコードで支払いました。')
        else:
            raise ValueError('利用できない決済方法です。')



from abc import ABC, abstractmethod

class AbstractPayment(ABC):
    def __init__(self, amount: int):
        self.amount = amount
    
    @abstractmethod
    def payment(self):
        pass

class CashPayment(AbstractPayment): 
    def payment(self):
        print(f'{self.amount}円を現金で支払いました。')

class CreditPayment(AbstractPayment):
    def payment(self):
        print(f'{self.amount}円をクレジットカードで支払いました。')

class QrPayment(AbstractPayment):
    def payment(self):
        print(f'{self.amount}円をQRコードで支払いました。')

cash_pay = CashPayment(2000)
cash_pay.payment()
print('#############################################')

credit_pay = CreditPayment(500)
credit_pay.payment()
print('#############################################')

qr_pay = QrPayment(1500)
qr_pay.payment()