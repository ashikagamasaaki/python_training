"""
問題1:
CSVファイル data.csv には以下のようなデータが格納されています。
Name,Math,English,Science
John,90,85,92
Alice,78,92,88
Bob,89,78,90

このデータを読み取り、各行の合計を計算して、新しいCSVファイル result.csv に出力してください。
"""

import csv

with open('data.csv', 'r') as csv_file, open('result.csv', 'w', newline='') as result_file:
    reader = csv.DictReader(csv_file)
    fieldnames = reader.fieldnames + ['Total']
    
    writer = csv.DictWriter(result_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        total = sum(int(row[key]) for key in reader.fieldnames[1:])
        row['Total'] = total
        writer.writerow(row)