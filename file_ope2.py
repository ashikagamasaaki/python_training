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

with open('resources/data.json', 'r', encoding='utf-8') as r_json, open('resources/result.json', 'w', encoding='utf-8') as w_json:
  r_data = json.load(r_json)
  w_data = {key: (value * 2) for key, value in r_data.items()}
  json.dump(w_data, w_json, indent=4, ensure_ascii=False)
    