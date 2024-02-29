class User:
    def __init__(self, user_code, user_name, family_code, address, account_code):
        self.__user_code = user_code
        self.__user_name = user_name
        self.__family_code = family_code
        self.__address = address
        self.__account_code = account_code
    
    @property
    def user_code(self):
        return self.__user_code
    
    @user_code.setter
    def user_code(self, user_code):
        self.__user_code = user_code
    
    
    @property
    def user_name(self):
        return self.__user_name
    
    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name
    
    
    @property
    def family_code(self):
        return self.__family_code
    
    @family_code.setter
    def family_code(self, family_code):
        self.__family_code = family_code
    
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
    
    
    @property
    def account_code(self):
        return self.__account_code
    
    @account_code.setter
    def account_code(self, account_code):
        self.__account_code = account_code