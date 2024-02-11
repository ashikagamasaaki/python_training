import mysql.connector

# conn = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='mysql'
#     )

# cursor = conn.cursor()
# cursor.execute('CREATE DATABASE test_mysql_database')
# cursor.close()
# conn.close()


conn = mysql.connector.connect(
    host='127.0.0.1',
    database='test_mysql_database',
    user='root',
    password='mysql'
    )

cursor = conn.cursor()
# cursor.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))')
cursor.execute('INSERT INTO persons(name) values("MIKE")')
conn.commit()
cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)
    
cursor.close()
conn.close()