"""
④以下の音楽ストリーミングサービスのコードは、

ISPに違反しているでしょうか

違反している場合は、その理由を述べた上で、
ISPを満たすようにコードを改善してください
この音楽ストリーミングサービスでは、

無料ユーザーと有料ユーザーで使用できる機能が異なり、

次のようになっているとします
・無料ユーザーは、広告有りの再生のみが可能
・有料ユーザーは、広告なしの再生・一時停止・スキップが可能

"""

from abc import ABC, abstractmethod

class IFreeMusicPlayer(ABC):
    @abstractmethod
    def play(self) -> None:
        pass
    

class IPaidMusicPlayer(ABC):
    @abstractmethod
    def play(self) -> None:
        pass
    
    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def skip(self) -> None:
        pass

class FreeUserMusicPlayer(IFreeMusicPlayer):
    def play(self) -> None:
        print('広告表示')
        print('再生します')
        # 再生処理

class PaidUserMusicPlayer(IPaidMusicPlayer):
    def play(self) -> None:
        print('再生します')
        # 再生処理

    def pause(self) -> None:
        print('一時停止します')
        # 一時停止処理

    def skip(self) -> None:
        print('スキップします')
        # スキップ処理




class AbstractMusicPlayer(ABC):
    def __init__(self, playlist: list):
        self.playlist = playlist

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def skip(self) -> None:
        pass

class FreeUserMusicPlayer(AbstractMusicPlayer):
    def play(self) -> None:
        print('広告表示')
        print('再生します')
        # 再生処理

    def pause(self) -> None:
        pass

    def skip(self) -> None:
        pass

class PaidUserMusicPlayer(AbstractMusicPlayer):
    def play(self) -> None:
        print('再生します')
        # 再生処理

    def pause(self) -> None:
        print('一時停止します')
        # 一時停止処理

    def skip(self) -> None:
        print('スキップします')
        # スキップ処理