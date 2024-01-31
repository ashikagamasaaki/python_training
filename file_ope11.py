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

with open('resources/grades.json', 'r', encoding='utf-8') as f, open('resources/new_agerage_grades.json', 'w', encoding='utf-8') as nf:
  json_data = json.load(f)
  school_class = json_data.get('class')
  grades_list = json_data.get('students')
  subjects = grades_list[0].get('grades').keys()

  new_json = {"class": school_class, "averages": {}}
  averages = new_json.get('averages')
  
  for s in subjects:
    averages[s] = {"total": 0, "count": 0, "average": 0}

  for l in grades_list:
    grades_data = l.get('grades')    
    for sub, val in grades_data.items():
      averages[sub]["total"] = averages[sub]["total"] + val
      averages[sub]["count"] = averages[sub]["count"] + 1
    
    
  for key in averages.keys():
    averages[key]["average"] = averages[key]["total"] / averages[key]["count"]



  json.dump(new_json, nf, indent=2)




# with open('resources/grades.json', 'r', encoding='utf-8') as f, open('resources/agerage_grades.json', 'w', encoding='utf-8') as nf:
#   data = json.load(f)
  
#   class_name = data.get('class', '')
#   students = data.get('students', [])

#   averages = {'class': class_name, 'averages': {}}

#   for student in students:
#       student_name = student.get('name', '')
#       grades = student.get('grades', {})
      
#       for subject, score in grades.items():
#           if subject not in averages['averages']:
#               averages['averages'][subject] = {'total': 0, 'count': 0}
          
#           averages['averages'][subject]['total'] += score
#           averages['averages'][subject]['count'] += 1

#   for subject, info in averages['averages'].items():
#       averages['averages'][subject]['average'] = info['total'] / info['count']

#   json.dump(averages, nf, indent=2)
  
  
  
  
  
  
  
  
  
