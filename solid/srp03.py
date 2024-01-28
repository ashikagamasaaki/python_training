"""
メールアドレスを表現する値オブジェクトを作成
ただし、メールアドレスの値は次の条件を満たす必要があるものとします※
・メールアドレスは必ず「@」を含む
・メールアドレスの「@」の前には少なくとも1文字以上、後ろには少なくとも2文字以上の文字列がある
"""

class MailAddress:
    def __init__(self, mail_address: str):
        if mail_address is None or len(mail_address) == 0:
            raise ValueError('メールアドレスは必須です。')
        elif '@' not in mail_address:
            raise ValueError('メールアドレスには「@」を含めてください。')
        elif 1 > mail_address.find('@'):
            raise ValueError('@の前は１文字以上')
        elif 2 > len(mail_address.split('@')[1]):
            raise ValueError('@の後ろは２文字以上')
        
        self.mail_address = mail_address
        
    def __str__(self):
        return self.mail_address
        
mail = MailAddress('sample@gmail.com')
print(mail)
    
# address = 'sample@gmail.com'

# # print(1 <= address.find('@'))
# print(len(address.split('@')[1]))