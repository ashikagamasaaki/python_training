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