"""
④スマートホームのシステムについて考えてみましょう

家を出る時には、電灯とエアコンを消して、カーテンを閉める
家に帰ってきた時には、電灯とエアコンを点けて、カーテンを開ける
上記2つの手順を、それぞれ1つのメソッドだけで完了できるようにするには、

次のコードにどのような変更を加えれば良いでしょうか    
"""

class Light:
    def turn_on(self):
        print('電灯がオンになりました')

    def turn_off(self):
        print('電灯がオフになりました')

class AirConditioner:
    def turn_on(self):
        print('エアコンがオンになりました')

    def turn_off(self):
        print('エアコンがオフになりました')

class Curtain:
    def open(self):
        print('カーテンを開きました')

    def close(self):
        print('カーテンを閉じました')

""" 家電の操作に関するクラス """
class Operation():
    def __init__(self):
        self.light = Light()
        self.aircon = AirConditioner()
        self.curtain = Curtain()
    
    # 家を出るときの操作
    def leaveHomeOpe(self):
        self.light.turn_off()
        self.aircon.turn_off()
        self.curtain.close()
    
    # 家に帰るときの操作
    def backHomeOpe(self):
        self.light.turn_on()
        self.aircon.turn_on()
        self.curtain.open()    


ope = Operation()
# ope.leaveHomeOpe()
ope.backHomeOpe()