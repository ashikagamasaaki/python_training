from abc import ABC, abstractmethod

# Product
class Player(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def next(self):
        pass
    
class MP3Player(Player):
    def play(self):
        print('MP3で再生')
    
    def stop(self):
        print('MP3で停止')
    
    def next(self):
        print('MP3で次の曲を再生')
    
class WAVPlayer(Player):
    def play(self):
        print('WAVで再生')
    
    def stop(self):
        print('WAVで停止')
    
    def next(self):
        print('WAVで次の曲を再生')
    
class OGGPlayer(Player):
    def play(self):
        print('OGGで再生')
    
    def stop(self):
        print('OGGで停止')
    
    def next(self):
        print('OGGで次の曲を再生')
        
class PlayerFactory(ABC):
    def create(self):
        player_factory = self.createPlayer()
        return player_factory
        
    @abstractmethod
    def createPlayer(self):
        pass
        
class MP3PlayerFactory(PlayerFactory):
    def createPlayer(self):
        return MP3Player()
        
class WAVPlayerFactory(PlayerFactory):
    def createPlayer(self):
        return WAVPlayer()
        
class OGGPlayerFactory(PlayerFactory):
    def createPlayer(self):
        return OGGPlayer()


mp3_factory = MP3PlayerFactory()
mp3 = mp3_factory.create()
mp3.play()
mp3.next()
mp3.stop()