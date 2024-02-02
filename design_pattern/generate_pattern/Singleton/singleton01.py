"""
Singleton

クラスが１つのインスタンスのみを持つことを保証
staticなget_instanceで、１つのインスタンスへアクセス

〇クラスが１つのインスタンしか持たないことを保証
〇メモリ効率がよい、インスタンス生成コストがかからない
×依存関係わかりにくく、密結合
×単体テストが難しい
×マルチスレッドで扱い難しい

■使いどころ
・ロギング
・キャッシュ管理
・コンフィグ
・DB接続ドライバ
"""
import datetime

class Logger:
    _instance = None
    
    # インスタンスが作成済みかどうかで挙動を変える
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def output(self, content: str):
        now = datetime.datetime.now()
        print(f'{now}: {content}')
        
class Test:
    pass


if __name__ == '__main__':
    test1 = Test()
    test2 = Test()
    print('Test: ', test1 == test2)
    
    
    logger1 = Logger()
    logger2 = Logger()
    print('Singleton: ', logger1 == logger2)
    
    logger1.output('logger1のログ')
    logger2.output('logger2のログ')
    