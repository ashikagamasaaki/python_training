"""
オープンクローズドの原則(OCP)
機能追加にはOPENで変更にはCLOSEである。
"""

class Notification:
    def send(self, notification_type: str, user_id: int) -> None:
        if notification_type == 'email':
            print('メール通知')
        elif notification_type == 'SMS':
            print('SMS通知')
        if notification_type == 'push':
            print('プッシュ通知')
        # 電話通知など新たな通知方法を追加するときに既存ソースを変更する必要あり。　　