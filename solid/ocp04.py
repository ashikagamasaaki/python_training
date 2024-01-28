"""
④あるカラオケ店の料金計算システムについて考えてみよう

このカラオケ店では、次のような料金システムになっているとする
・利用時間は1時間単位
・基本料金は1時間あたり700円
・学生は料金が基本料金の80%になる
・会員は料金が基本料金の90%になる
・学生割引と会員割引は併用できる
"""

from abc import ABC, abstractmethod

# ベースとなる抽象クラス
class AbstractRoomFee(ABC):
    @abstractmethod
    def get_cost(self, hours: int) -> int:
        pass
    
# ベースの基本料金の計算クラス
class BaseRoomFee(AbstractRoomFee):
    def get_cost(self, hours: int) -> int:
        return 700 * hours

# 会員割引をつけるインターフェース
class RoomFeeDecorator(AbstractRoomFee, ABC):
    def __init__(self, room_fee: AbstractRoomFee):
        self.room_fee = room_fee

    @abstractmethod
    def get_cost(self, hours: int) -> int:
        return self.room_fee * hours


class StudentDiscountDecorator(RoomFeeDecorator):
    def get_cost(self, hours: int) -> int:
        base_cost = self.room_fee.get_cost(hours)
        return int(base_cost * 0.8)


class MemberDiscountDecorator(RoomFeeDecorator):
    def get_cost(self, hours: int) -> int:
        base_cost = self.room_fee.get_cost(hours)
        return int(base_cost * 0.9)


def calculate_fee(room_fee: AbstractRoomFee, hours: int):
    print(f'カラオケの料金は：{room_fee.get_cost(hours)}円')


calculate_fee(BaseRoomFee(), 2)
calculate_fee(StudentDiscountDecorator(BaseRoomFee()), 2)
calculate_fee(MemberDiscountDecorator(BaseRoomFee()), 2)
calculate_fee(StudentDiscountDecorator(MemberDiscountDecorator(BaseRoomFee())), 2)


# base_fee = BaseRoomFee()
# student_fee = StudentDiscountDecorator(base_fee)


# print(base_fee.get_cost(5))
# print(student_fee.get_cost(5))
