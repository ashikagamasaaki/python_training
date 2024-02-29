class Account:
    def __init__(self, account_code, account_name, user_code, address, company_code):
        self.__account_code = account_code
        self.__account_name = account_name
        self.__user_code = user_code
        self.__address = address
        self.__company_code = company_code
    
    @property
    def account_code(self):
        return self.__account_code
    
    @account_code.setter
    def account_code(self, account_code):
        self.__account_code = account_code
    
    
    @property
    def account_name(self):
        return self.__account_name
    
    @account_name.setter
    def account_name(self, account_name):
        self.__account_name = account_name
    
    
    @property
    def user_code(self):
        return self.__user_code
    
    @user_code.setter
    def user_code(self, user_code):
        self.__user_code = user_code
    
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
    
    
    @property
    def company_code(self):
        return self.__company_code
    
    @company_code.setter
    def company_code(self, company_code):
        self.__company_code = company_code