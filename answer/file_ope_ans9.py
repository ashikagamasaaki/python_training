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

with open('students.json', 'r') as json_file:
    data = json.load(json_file)

workbook = openpyxl.Workbook()
sheet = workbook.active

headers = list(data['students'][0].keys())
sheet.append(headers)

for student in data['students']:
    sheet.append([student[header] for header in headers])

workbook.save('students.xlsx')