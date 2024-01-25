"""
問題81-90: 様々な形式のファイル操作

Excelファイルの読み込み: 与えられたExcelファイルを読み込み、その内容を表示するプログラムを作成してください。
Excelファイルの書き込み: 与えられたデータを新しいExcelファイルに書き込むプログラムを作成してください。
JSONファイルの読み込み: 与えられたJSONファイルを読み込み、その内容を表示するプログラムを作成してください。
JSONファイルの書き込み: 与えられたデータを新しいJSONファイルに書き込むプログラムを作成してください。
CSVファイルからExcelファイルへの変換: 与えられたCSVファイルをExcelファイルに変換するプログラムを作成してください。
ExcelファイルからCSVファイルへの変換: 与えられたExcelファイルをCSVファイルに変換するプログラムを作成してください。
JSONファイルからCSVファイルへの変換: 与えられたJSONファイルをCSVファイルに変換するプログラムを作成してください。
CSVファイルからJSONファイルへの変換: 与えられたCSVファイルをJSONファイルに変換するプログラムを作成してください。
Excelファイルの特定の行列の抽出: 与えられたExcelファイルから特定の行列のデータを抽出するプログラムを作成してください。
JSONファイルの特定の要素の抽出: 与えられたJSONファイルから特定の要素のデータを抽出するプログラムを作成してください。
"""
import pandas as pd
sample_excel = 'resources/sample.xlsx'

# 81    Excelファイルの読み込み: 与えられたExcelファイルを読み込み、その内容を表示するプログラムを作成してください。
excel_data = pd.read_excel(sample_excel, sheet_name='sheet1')
print(excel_data)


# 82    Excelファイルの書き込み: 与えられたデータを新しいExcelファイルに書き込むプログラムを作成してください。
data_to_write = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df_to_write = pd.DataFrame(data_to_write)
df_to_write.to_excel('resources/new_excel_file.xlsx', index=False)


# 83    JSONファイルの読み込み: 与えられたJSONファイルを読み込み、その内容を表示するプログラムを作成してください。
path83 = 'resources/sample83.json'
with open(path83, 'r', encoding='utf-8') as f:
    print(f.read())

import json
with open(path83, 'r') as f:
    print(json.load(f))
# json_open = open(path83, 'r')
# print(json.load(json_open))


# 84    JSONファイルの書き込み: 与えられたデータを新しいJSONファイルに書き込むプログラムを作成してください。
data_to_write = {'Name': 'John', 'Age': 28, 'City': 'New York'}
path84 = 'resources/sample84.json'
with open(path84, 'w', encoding='utf-8') as f:
    json.dump(data_to_write, f)


# 85    CSVファイルからExcelファイルへの変換: 与えられたCSVファイルをExcelファイルに変換するプログラムを作成してください。
csv_file = 'resources/sample75.csv'





# 86    ExcelファイルからCSVファイルへの変換: 与えられたExcelファイルをCSVファイルに変換するプログラムを作成してください。
# 87    JSONファイルからCSVファイルへの変換: 与えられたJSONファイルをCSVファイルに変換するプログラムを作成してください。
# 88    CSVファイルからJSONファイルへの変換: 与えられたCSVファイルをJSONファイルに変換するプログラムを作成してください。
# 89    Excelファイルの特定の行列の抽出: 与えられたExcelファイルから特定の行列のデータを抽出するプログラムを作成してください。
# 90    JSONファイルの特定の要素の抽出: 与えられたJSONファイルから特定の要素のデータを抽出するプログラムを作成してください。