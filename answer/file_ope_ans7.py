"""
問題7:
CSVファイル data.csv には以下のようなデータが格納されています。

Name,Math,English,Science
John,90,85,92
Alice,78,92,88
Bob,89,78,90

CSVファイル data.csv を読み取り、そのデータをJSON形式に変換して、新しいJSONファイル data.json に保存してください。
"""
import csv
import json

with open('data.csv', 'r') as csv_file, open('data.json', 'w') as json_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]
    json.dump(data, json_file, indent=2)