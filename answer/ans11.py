import sqlite3
import json
from datetime import datetime

# データベース初期化
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
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
conn.commit()

# 商品クラス
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# 取引クラス
class Transaction:
    def __init__(self, customer_id, product_ids):
        self.customer_id = customer_id
        self.product_ids = product_ids
        self.purchase_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 商品情報をデータベースに追加
def add_product(product):
    cursor.execute('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', (product.name, product.price, product.stock))
    conn.commit()

# 取引データをデータベースに追加
def add_transaction(transaction):
    cursor.execute('INSERT INTO transactions (customer_id, product_ids, purchase_datetime) VALUES (?, ?, ?)', 
                   (transaction.customer_id, json.dumps(transaction.product_ids), transaction.purchase_datetime))
    conn.commit()

# 商品情報をファイルに保存
def save_products_to_file(products, filename='products.txt'):
    with open(filename, 'w') as file:
        for product in products:
            file.write(f"{product.name},{product.price},{product.stock}\n")

# 商品情報をファイルから読み込み
def load_products_from_file(filename='products.txt'):
    products = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            products.append(Product(data[0], float(data[1]), int(data[2])))
    return products

# サンプル商品と取引データの追加
sample_product = Product('Laptop', 1200.0, 50)
add_product(sample_product)

sample_transaction = Transaction(1, [1, 2])
add_transaction(sample_transaction)

# ファイルへの書き込みと読み込みの例
products_list = [sample_product, Product('Smartphone', 800.0, 100), Product('Headphones', 50.0, 200)]
save_products_to_file(products_list)
loaded_products = load_products_from_file()

# ファイルとデータベースの整合性確認
for db_product, file_product in zip(cursor.execute('SELECT * FROM products').fetchall(), loaded_products):
    assert db_product[1:] == (file_product.name, file_product.price, file_product.stock)

print("システム開発の仕様に基づいたプログラムが正常に動作しました。")