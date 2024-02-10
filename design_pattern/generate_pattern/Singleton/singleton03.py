
class DatabaseConnection:
    _instance = None
    host = 'localhost'
    port = '5432'
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __str__(self):
        return f'host: {self.host}, port: {self.port}'
    
    def output(self, contet: str):
        print(contet)
    
db = DatabaseConnection()
db2 = DatabaseConnection()

db.output('testtesttest')

print(db)
print(db == db2)