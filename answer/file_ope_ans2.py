"""
問題2:
JSONファイル data.json には以下のようなデータが格納されています。
{
  "John": 30,
  "Alice": 22,
  "Bob": 35
}

このデータを読み取り、各要素の値を2倍にして、新しいJSONファイル result.json に出力してください。
"""
import json

with open('data.json', 'r') as json_file, open('result.json', 'w') as result_file:
    data = json.load(json_file)
    doubled_data = {key: value * 2 for key, value in data.items()}
    json.dump(doubled_data, result_file, indent=2)