# 81.
import pandas as pd

excel_data = pd.read_excel('example.xlsx')
print(excel_data)

# 82.
data_to_write = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df_to_write = pd.DataFrame(data_to_write)
df_to_write.to_excel('new_excel_file.xlsx', index=False)

# 83.
import json

with open('example.json', 'r') as file:
    json_data = json.load(file)
    print(json_data)

# 84.
data_to_write = {'Name': 'John', 'Age': 28, 'City': 'New York'}
with open('new_json_file.json', 'w') as file:
    json.dump(data_to_write, file, indent=2)

# 85.
csv_data = pd.read_csv('example.csv')
csv_data.to_excel('converted_excel_file.xlsx', index=False)

# 86.
excel_data = pd.read_excel('example.xlsx')
excel_data.to_csv('converted_csv_file.csv', index=False)

# 87.
with open('example.json', 'r') as json_file:
    json_data = json.load(json_file)
    csv_data = pd.json_normalize(json_data)
    csv_data.to_csv('converted_csv_file.csv', index=False)

# 88.
csv_data = pd.read_csv('example.csv')
json_data = csv_data.to_dict(orient='records')
with open('converted_json_file.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

# 89.
excel_data = pd.read_excel('example.xlsx', sheet_name='Sheet1', usecols=['Name', 'Age'])
print(excel_data)

# 90.
with open('example.json', 'r') as json_file:
    json_data = json.load(json_file)
    selected_data = {'Name': json_data['Name'], 'Age': json_data['Age']}
    print(selected_data)