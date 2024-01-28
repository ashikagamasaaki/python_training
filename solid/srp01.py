"""
■単一責任の原則(SRP)
・1つのオブジェクトには1つの責務しか持たせない
・責務はコードを変更する理由を考えるとよい
・SRPを実践することで、コードを修正するときに変更箇所を少なくすることが可能
・クラスやメソッドの数が増える
・クラスやメソッドの呼び出し処理が複雑化するが、Facadeパターンを使い解決できる
・値オブジェクトを使用することでガード句を作り、不正なデータ作成を防ぐことができる

■凝集度、結合度
・凝集度：
 モジュール内の関連性の強さ
 機能間での依存度が低いことを凝集度が高いという（機能Aに変更を加えても機能Bには影響しないこと）
 
・結合度：
 モジュール間の関連性の強さ
 凝集度が高ければ、結合度は下がる
"""


"""
Customerクラスに「顧客情報の管理」「割引計算」「メール送信」「ポイント計算」の4つの責務を含んでいる
それぞれの責務ごとにクラスを作成する必要がある
"""
class Customer:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'名前：{self.name}、年齢：{self.age}'
    
    def calculate_discount(self, total_amount: int) -> None:
        if self.age >= 60:
            discount = total_amount * 0.1
        else:
            discount = total_amount * 0.05
    
    def send_email(self) -> None:
        email_conten = f'お客様のご購入ありがとうございます、{self.name}さん。'
        print('メールを送信しました。')
        
    def calculate_points(self, total_amount: int) -> None:
        points = total_amount
        print(f'獲得ポイント：{points}')
        



"""
上記をSREに当てはめる
"""
class Customer:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'名前：{self.name}、年齢：{self.age}'

class Discount:
    def calculate_discount(self, customer: Customer, total_amount: int) -> None:
        if customer.age >= 60:
            discount = total_amount * 0.1
        else:
            discount = total_amount * 0.05
        print(f'割引額：{discount}')

class Mail:
    def send_mail(self, customer: Customer):
        self.mail_conten = f'ご購入ありがとうございます、{customer.name}さん。'
        print('メールを送信しました。')

class Point:
    def __init__(self, total_amount: int):
        self.points = total_amount

    def __str__(self) -> str:
        return f'獲得ポイント：{self.points}'