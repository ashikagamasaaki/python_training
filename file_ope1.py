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

# Listを使った場合
# with open('resources/data.csv', 'r', encoding='utf-8') as csv_file:
#     f = csv.reader(csv_file, delimiter=',')
    
#     with open('resources/result.csv', 'w', encoding='utf-8', newline='') as result_file:
#         w = csv.writer(result_file)
        
#         for index, row in enumerate(f):
#             if index == 0:
#                 row.append('total')
#             else:
#                 total = sum(int(r) for r in row[1:])
#                 row.append(str(total))
#             w.writerow(row)


# 辞書型を使った場合
with open('resources/data.csv', 'r', encoding='utf-8') as csv_file, open('resources/result.csv', 'w', encoding='utf-8', newline='') as result_file:
    csv_data = csv.DictReader(csv_file)
    field_names = csv_data.fieldnames
    
    w = csv.DictWriter(result_file, fieldnames=field_names + ['Total'])
    w.writeheader()
    print(field_names)
    
    for data in csv_data:
        total = sum(int(data[key]) for key in field_names[1:])
        data['Total'] = total
        w.writerow(data)