"""
問題9:
JSONファイル students.json には以下のようなデータが格納されています。

{
  "students": [
    {"id": 101, "name": "John", "grade": 85},
    {"id": 102, "name": "Alice", "grade": 92},
    {"id": 103, "name": "Bob", "grade": 78}
  ]
}

このデータを読み取り、Excel形式に変換して、新しいExcelファイル students.xlsx に保存してください。
"""

import json
import openpyxl

with open('resources/students.json', 'r', encoding='utf-8') as json_file:
  json_data = json.load(json_file)
  
  json_rows = json_data.get('students')
  json_key = json_rows[0].keys()


header = {i: key for i, key in enumerate(json_key, 1)}

workbook = openpyxl.Workbook()
sheet = workbook["Sheet"]
sheet.title = "Students"
sheet.append(header)

for json_row in json_rows:
  # print(type(json_row))
  sheet.append([json_row[key] for key in json_row.keys()])


workbook.save('resources/students.xlsx')