"""
問題4:
CSVファイル sales.csv には以下のようなデータが格納されています。

Product,January,February,March
Apple,100,120,150
Orange,80,90,110
Banana,50,60,70

各製品の月ごとの売上合計を計算し、新しいCSVファイル monthly_sales.csv に出力してください。
"""

import csv

with open('resources/sales.csv', 'r', encoding='utf-8') as r, open('resources/monthly_sales.csv', 'w', encoding='utf-8', newline='') as w:
    sales_data = csv.DictReader(r)
    fieldnames = sales_data.fieldnames + ['Total']
    
    sales_writer = csv.DictWriter(w, fieldnames=fieldnames)
    sales_writer.writeheader()
    
    for data in sales_data:
        total = sum(int(data[key]) for key in sales_data.fieldnames[1:])
        data['Total'] = total
        sales_writer.writerow(data)
        
