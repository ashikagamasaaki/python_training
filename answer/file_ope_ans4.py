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

with open('sales.csv', 'r') as csv_file, open('monthly_sales.csv', 'w', newline='') as result_file:
    reader = csv.DictReader(csv_file)
    fieldnames = reader.fieldnames + ['Total']
    
    writer = csv.DictWriter(result_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        total = sum(int(row[key]) for key in reader.fieldnames[1:])
        row['Total'] = total
        writer.writerow(row)