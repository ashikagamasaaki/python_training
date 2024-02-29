class Company:
    def __init__(self, company_code, company_name, account_code, address):
        self._company_code = company_code
        self._company_name = company_name
        self._account_code = account_code
        self._address = address
    
    @property
    def company_code(self):
        return self._company_code
    
    @company_code.setter
    def company_code(self, company_code):
        self._company_code = company_code
    
    
    @property
    def company_name(self):
        return self._company_name
    
    @company_name.setter
    def company_name(self, company_name):
        self._company_name = company_name
    
    
    @property
    def account_code(self):
        return self._account_code
    
    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code
    
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
    