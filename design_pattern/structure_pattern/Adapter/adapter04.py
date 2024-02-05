from abc import ABC, abstractmethod

# Adaptee
class OldLibrary:
    def perform_action(self):
        print('OldLibraryでの処理')
        
# Target
class Target(ABC):
    @abstractmethod
    def perform_new_action(self):
        pass

# Adapter
class NewLibraryAdapter(Target):
    def __init__(self, old_lib: OldLibrary):
        self.__old_lib = old_lib
        
    def perform_new_action(self):
        self.__old_lib.perform_action()
        print('を利用して新しい処理を実行する')
        

# 以下は使用例です
old_library_instance = OldLibrary()
old_library_instance.perform_action()

new_library_instance = NewLibraryAdapter(old_library_instance)
new_library_instance.perform_new_action()