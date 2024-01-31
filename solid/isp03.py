"""
⑤以下のATMを表現したコードは、

ISPに違反しているでしょうか
違反している場合は、その理由を述べた上で、
ISPを満たすようにコードを改善してください

ただし、ATMで行える操作は、
・引き出し
・預け入れ
・振り込み
の3つであり、これらの操作は1つのトランザクションで1つだけ行われます
また、BankAccountは銀行口座を表す値オブジェクトであるとします
"""
from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, account_code: int) -> None:
        self.account_code = account_code


# class ATMInterface(ABC):
#     @abstractmethod
#     def withdraw_transaction(self, amount: int) -> None:
#         pass

#     @abstractmethod
#     def deposit_transaction(self, amount: int) -> None:
#         pass

#     @abstractmethod
#     def transfer_transaction(self, to_bank_account: BankAccount, amount: int) -> None:
#         pass

# 出金用IF
class IWithdraw(ABC):
    @abstractmethod
    def withdraw_transaction(self, amount: int) -> None:
        pass

# 預金用IF
class IDeposit(ABC):
    @abstractmethod
    def deposit_transaction(self, amount: int) -> None:
        pass

# 振込用IF
class ITransfer(ABC):
    @abstractmethod
    def transfer_transaction(self, to_bank_account: BankAccount, amount: int) -> None:
        pass
    
class ATM(IWithdraw, IDeposit, ITransfer):
    def __init__(self, bank_account: BankAccount):
        self.bank_account = bank_account

    def withdraw_transaction(self, amount: int) -> None:
        # 引き出し処理
        print('出金成功')

    def deposit_transaction(self, amount: int) -> None:
        # 預け入れ処理
        print('入金成功')

    def transfer_transaction(self, to_bank_account: BankAccount, amount: int) -> None:
        # 振り込み処理
        print('振込成功')


# 出金用クライアント 
class WithdrowClient(IWithdraw):
    def __init__(self, atm_if: IWithdraw):
        self.atm_if = atm_if
    
    def execute(self, amount: int):
        self.atm_if.withdraw_transaction(amount)


# 預金用クライアント 
class DepositClient(IDeposit):
    def __init__(self, atm_if: IDeposit):
        self.atm_if = atm_if
    
    def execute(self, amount: int):
        self.atm_if.deposit_transaction(amount)


# 振込用クライアント 
class TransferClient(ITransfer):
    def __init__(self, atm_if: ITransfer, bank_account: BankAccount):
        self.atm_if = atm_if
        self.bank_account = bank_account
    
    def execute(self, amount: int):
        account = self.bank_account
        self.atm_if.transfer_transaction(amount, account)