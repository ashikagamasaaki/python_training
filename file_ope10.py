"""
問題10:
CSVファイル sales.csv には以下のようなデータが格納されています。

Product,January,February,March
Apple,100,120,150
Orange,80,90,110
Banana,50,60,70

このデータを読み取り、Excel形式に変換して、新しいExcelファイル sales_data.xlsx に保存してください。
"""
import csv
import openpyxl

with open('resources/sales.csv', 'r', encoding='utf-8') as csv_file:
    csv_data = csv.DictReader(csv_file)
    fieldnames = csv_data.fieldnames
    
    workbook = openpyxl.Workbook()
    sheet = workbook['Sheet']
    sheet.append(fieldnames)

    for row in csv_data:
        row_data = [row[key] for key in row.keys()]
        sheet.append(row_data)

workbook.save('resources/sales_data.xlsx')