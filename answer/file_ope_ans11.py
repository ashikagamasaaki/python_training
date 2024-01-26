"""
問題11:
以下は、複雑にネストしたJSONデータです。

{
  "class": "A",
  "students": [
    {
      "name": "John",
      "grades": {
        "Math": 90,
        "English": 85,
        "Science": 92
      }
    },
    {
      "name": "Alice",
      "grades": {
        "Math": 78,
        "English": 92,
        "Science": 88
      }
    },
    {
      "name": "Bob",
      "grades": {
        "Math": 89,
        "English": 78,
        "Science": 90
      }
    }
  ]
}

このデータを読み取り、各生徒の科目ごとの平均点を計算して、新しいJSONファイル average_grades.json に出力してください。
"""
import json

with open('grades_nested.json', 'r') as json_file, open('average_grades.json', 'w') as result_file:
    data = json.load(json_file)

class_name = data.get('class', '')
students = data.get('students', [])

averages = {'class': class_name, 'averages': {}}

for student in students:
    student_name = student.get('name', '')
    grades = student.get('grades', {})
    
    for subject, score in grades.items():
        if subject not in averages['averages']:
            averages['averages'][subject] = {'total': 0, 'count': 0}
        
        averages['averages'][subject]['total'] += score
        averages['averages'][subject]['count'] += 1

for subject, info in averages['averages'].items():
    averages['averages'][subject]['average'] = info['total'] / info['count']

json.dump(averages, result_file, indent=2)