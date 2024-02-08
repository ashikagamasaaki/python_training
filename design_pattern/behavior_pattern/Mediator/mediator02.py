"""
Mediator
オブジェクト間のデータの受け渡しを行う。
オブジェクト同士が直接やり取りすると、オブジェクト間の関係が強くなるため。
オブジェクトの独立性を高める。

・Mediator: Colleagueと通信を行い、処理の調整を行うIF
・ConcreteMediator: Mediatorを具体化したクラス。特定のColleagueに対しての調整を行う
・Colleague: Mediatorと通信して、処理を調整する処理のIF
・ConcreteColleague: Colleagueを具体化したクラス
"""

from abc import ABC, abstractmethod

# Colleague
class WindowsBase(ABC):
    def __init__(self, mediator=None):
        self._mediator = mediator
        self._is_open = False
    
    @property
    def mediator(self):
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator
    
    @property
    def is_open(self):
        return self._is_open
    
    @is_open.setter
    def is_open(self, is_open):
        self._is_open = is_open
        
    @abstractmethod
    def open(self):
        pass
        
    @abstractmethod
    def close(self):
        pass
    
# ConcreteColleague(この中にほかのウィンドウの操作を記述すると独立性が悪くなる→Mediatorを使う)
class MainWindow(WindowsBase):
    def open(self):
        print('open MainWindow')
        self.is_open = True
    
    def close(self):
        self.mediator.notify('main', 'close')
        print('Close MainWindow')
        self.is_open = False
    
# ConcreteColleague
class SettingsWindow(WindowsBase):
    def open(self):
        self.mediator.notify('settings', 'open')
        print('open SettingsWindow')
        self.is_open = True
    
    def close(self):
        print('Close SettingsWindow')
        self.is_open = False
    
# ConcreteColleague
class HelpWindow(WindowsBase):
    def open(self):
        self.mediator.notify('help', 'open')
        print('open HelpWindow')
        self.is_open = True
    
    def close(self):
        print('Close HelpWindow')
        self.is_open = False
        
# Mediator
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, action):
        pass
    

# ConcreteMediator
class WindowMediator(Mediator):
    def __init__(self, main_window: MainWindow, settings_window: SettingsWindow, help_window: HelpWindow):
        self.__main_window = main_window
        self.__settings_window = settings_window
        self.__help_window = help_window
        main_window.mediator = self
        settings_window.mediator = self
        help_window.mediator = self
    
    def notify(self, sender, action):
        # SettingsWindowを開く場合は、HelpWindowを閉じる
        if (sender == 'settings') and (action == 'open'):
            if self.__help_window.is_open:
                self.__help_window.close()
        # HelpWindowを開く場合は、SettingsWindowを閉じる
        if (sender == 'help') and (action == 'open'):
            if self.__settings_window.is_open:
                self.__settings_window.close()
        # MainWindowを閉じる場合は、SettingsWindowとHelpWindowは閉じる
        if (sender == 'main') and (action == 'close'):
            if self.__settings_window.is_open:
                self.__settings_window.close()
                
            if self.__help_window.is_open:
                self.__help_window.close()
                

main_window = MainWindow()
settings_window = SettingsWindow()
help_window = HelpWindow()

mediator = WindowMediator(main_window, settings_window, help_window)

main_window.open()
settings_window.open()
help_window.open()
print(help_window.is_open)
settings_window.open()
print(help_window.is_open)
main_window.close()