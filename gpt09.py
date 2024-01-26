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

with open(csv_file, 'r', encoding='utf-8') as f:
    header_str = f.readline().replace('"', '').rstrip('\n')
    header_body = {key: [] for key in header_str.split(",")}
    read_line = f.readline()
    
    while read_line:
        read_line_list = read_line.replace('"', '').split(",")
        for index, key in enumerate(header_body.keys()):
            # print(f'index={index}, key={key}, value={read_line_list[index]}')
            header_body.get(key).append(read_line_list[index])
        read_line = f.readline()
    
df_to_write = pd.DataFrame(header_body)
df_to_write.to_excel('resources/sample85.xlsx', index=False)


# 85-2(CVSライブラリ使用)
import csv
with open(csv_file, 'r', encoding='utf-8') as f:
    f_list = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
    f_dict = csv.DictReader(f, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
    
    df_to_write = pd.DataFrame(f_dict)
    df_to_write.to_excel('resources/sample85_2.xlsx', index=False)


# 86    ExcelファイルからCSVファイルへの変換: 与えられたExcelファイルをCSVファイルに変換するプログラムを作成してください。
excel_data = pd.read_excel('resources/sample85.xlsx')
excel_data.to_csv('resources/converted_csv_file.csv', index=False)

print("#######################")
# 87    JSONファイルからCSVファイルへの変換: 与えられたJSONファイルをCSVファイルに変換するプログラムを作成してください。
with open('resources/sample87.json', 'r') as f:
    json_load = json.load(f)
    csv_data = pd.json_normalize(json_load)
    csv_data.to_csv('resources/sample87.csv', index=False)
    print(csv_data)


# 88    CSVファイルからJSONファイルへの変換: 与えられたCSVファイルをJSONファイルに変換するプログラムを作成してください。
csv_file = 'resources/sample75.csv' 
# csv_data = pd.read_csv(csv_file, sep=",")
# csv_data.to_json('resources/sample88.json', orient="records")

csv_data = pd.read_csv(csv_file, keep_default_na=False)
json_data = csv_data.to_dict(orient='records')
print(json_data)
with open('resources/sample88.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=2, ensure_ascii=False)


# 89    Excelファイルの特定の行列の抽出: 与えられたExcelファイルから特定の行列のデータを抽出するプログラムを作成してください。
df = pd.read_excel('resources/sample89.xlsx', sheet_name="Sheet1", usecols=['都道府県名', '人口（総数）']) # 都道府県名、人口総数を取得
print("#######################")
print(df)


# 90    JSONファイルの特定の要素の抽出: 与えられたJSONファイルから特定の要素のデータを抽出するプログラムを作成してください。
print("#######################")
with open('resources/sample90.json', 'r', encoding='utf-8') as f:
    jd = json.load(f)
    print(jd['001']['name'])
    print(f'{json.dumps(jd, indent=4)}')