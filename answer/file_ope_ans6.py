"""
問題6:
Excelファイル inventory.xlsx には以下のようなデータが格納されています。

| Product | Stock |
|---------|-------|
| Apple   | 15    |
| Orange  | 8     |
| Banana  | 5     |
| Grape   | 12    |

各商品の在庫数が10以下の場合、その商品名と在庫数を表示するプログラムを作成してください。
"""
import openpyxl

workbook = openpyxl.load_workbook('inventory.xlsx')
sheet = workbook.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    product_name, stock = row
    if stock <= 10:
        print(f"Low Stock: {product_name}, Stock: {stock}")