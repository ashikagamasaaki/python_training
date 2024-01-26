import sqlite3
import json
from datetime import datetime

# データベース初期化
conn = sqlite3.connect('crm_system.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        contact TEXT NOT NULL,
        company_name TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        product_ids TEXT NOT NULL,
        purchase_datetime TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS activity_logs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        activity TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
''')
conn.commit()

# 顧客クラス
class Customer:
    def __init__(self, name, contact, company_name):
        self.name = name
        self.contact = contact
        self.company_name = company_name

# 取引クラス
class Transaction:
    def __init__(self, customer_id, product_ids):
        self.customer_id = customer_id
        self.product_ids = product_ids
        self.purchase_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# アクティビティログクラス
class ActivityLog:
    def __init__(self, user_id, activity):
        self.user_id = user_id
        self.activity = activity
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 顧客情報をデータベースに追加
def add_customer(customer):
    cursor.execute('INSERT INTO customers (name, contact, company_name) VALUES (?, ?, ?)', 
                   (customer.name, customer.contact, customer.company_name))
    conn.commit()

# 取引データをデータベースに追加
def add_transaction(transaction):
    cursor.execute('INSERT INTO transactions (customer_id, product_ids, purchase_datetime) VALUES (?, ?, ?)', 
                   (transaction.customer_id, json.dumps(transaction.product_ids), transaction.purchase_datetime))
    conn.commit()

# アクティビティログをデータベースに追加
def add_activity_log(activity_log):
    cursor.execute('INSERT INTO activity_logs (user_id, activity, timestamp) VALUES (?, ?, ?)', 
                   (activity_log.user_id, activity_log.activity, activity_log.timestamp))
    conn.commit()

# 顧客情報をファイルに保存
def save_customers_to_file(customers, filename='customers.txt'):
    with open(filename, 'w') as file:
        for customer in customers:
            file.write(f"{customer.name},{customer.contact},{customer.company_name}\n")

# 顧客情報をファイルから読み込み
def load_customers_from_file(filename='customers.txt'):
    customers = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            customers.append(Customer(data[0], data[1], data[2]))
    return customers

# サンプル顧客、取引データ、アクティビティログの追加
sample_customer = Customer('John Doe', '555-1234', 'ABC Inc.')
add_customer(sample_customer)

sample_transaction = Transaction(1, [1, 2])
add_transaction(sample_transaction)

sample_activity_log = ActivityLog(1, 'Login')
add_activity_log(sample_activity_log)

# ファイルへの書き込みと読み込みの例
customers_list = [sample_customer, Customer('Jane Smith', '555-5678', 'XYZ Corp.')]
save_customers_to_file(customers_list)
loaded_customers = load_customers_from_file()

# ファイルとデータベースの整合性確認
for db_customer, file_customer in zip(cursor.execute('SELECT * FROM customers').fetchall(), loaded_customers):
    assert db_customer[1:] == (file_customer.name, file_customer.contact, file_customer.company_name)

print("CRMシステムの開発に基づいたプログラムが正常に動作しました。")