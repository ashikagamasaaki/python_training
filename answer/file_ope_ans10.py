"""
問題10:
CSVファイル sales_data.csv には以下のようなデータが格納されています。

Product,January,February,March
Apple,100,120,150
Orange,80,90,110
Banana,50,60,70

このデータを読み取り、Excel形式に変換して、新しいExcelファイル sales_data.xlsx に保存してください。
"""
import csv
import openpyxl

with open('sales_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(headers)

    for row in csv_reader:
        sheet.append(row)

    workbook.save('sales_data.xlsx')