class NameDefineException(Exception):
    pass

""" 値オブジェクト """
class FullName:
    def __init__(self, firstName: str, lastName: str) -> None:
        # ブロック句の定義もできる
        if len(firstName) >= 100 or len(firstName) <= 0:
            raise NameDefineException('ファーストネームは100文字以内で定義してください。')
        if firstName is None:
            raise NameDefineException('ファーストネームは必須です。')
        
        self.__firstName = firstName
        self.__lastName = lastName
        pass
    
    @property
    def firstName(self):
        return self.__firstName
    
    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName
    
    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName
    
    # クラス内に名前比較結果を返すメソッドを定義
    def __eq__(self, other: 'FullName'):
        return self.__firstName == other.firstName and self.__lastName == other.lastName
        

# 名前の比較メソッド()
def compareName(name1: FullName, name2: FullName) -> bool:
    return name1.firstName == name2.firstName and name1.lastName == name2.lastName

fullName = FullName('Taro', 'Tanaka')
print(f'Full Name = {fullName.firstName} {fullName.lastName} です。')

# fullName2 = FullName('Taro', 'Tanaka')

# print('比較１(eqメソッド) = ',fullName == fullName2)
# print('比較１(compareメソッド) = ',compareName(fullName, fullName2))

# fullName.firstName = '太郎'
# fullName.lastName = '田中'
# print(f'Full Name = {fullName.firstName} {fullName.lastName} です。')

# print('比較２(eqメソッド) = ',fullName == fullName2)
# print('比較２(compareメソッド) = ',compareName(fullName, fullName2))

