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

with open('resources/data.csv', 'r', encoding='utf-8') as csv_file, open('resources/data2.json', 'w', encoding='utf-8') as json_file:
    csv_data = csv.DictReader(csv_file)
    json_data = [row for row in csv_data]
    json.dump(json_data, json_file, indent=4)
    