"""
Adapter（構造）

IFを利用する側が求めるほかのIFに変換する

Client
↓
Target ← Adapter → Adaptee

継承する方法：Adaptee(親)をAdapter(子)が継承
委譲する方法：Adapteeを属性としてAdapterにもつ

〇既存クラス(Adaptee)の修正をしない、再テストは不要
〇単一責任、オープンクローズドが実現
×クラス数が増える
"""

# Adapterを継承で実現
from abc import ABCMeta, abstractmethod

class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass
    
class NewLibrary:
    def get_json_data(self) -> list[dict[str, str]]:
        json_data = [
            {"apple": "red", "banana": "yellow"}, 
            {"apple": "great", "banana": "beatiful"}
        ]
        return json_data
    
class JsonToCsvAdapter(NewLibrary, Target):
    def get_csv_data(self) -> str:
        json_data = self.get_json_data()
        header = ",".join(list(json_data[0].keys())) + '\n'
        body = "\n".join([",".join(list(d.values())) for d in json_data])
        csv_data = header + body
        return csv_data

if __name__ == '__main__':
    adaptee = NewLibrary()
    print("=== Adapteeが提供するデータ ===")
    print(adaptee.get_json_data())
    
    print()
    
    adapter = JsonToCsvAdapter()
    print("=== Adapterが提供するデータ ===")
    print(adapter.get_csv_data())
    