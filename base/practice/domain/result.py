class Result:
    def __init__(self, company_code, company_name, address):
        self.company_code = company_code
        self.company_name = company_name
        self.address = address
    
    @property
    def company_code(self):
        return self.company_code
    
    @company_code.setter
    def company_code(self, company_code):
        self.company_code = company_code
    
    
    @property
    def company_name(self):
        return self.company_name
    
    @company_name.setter
    def company_name(self, company_name):
        self.company_name = company_name
    
    
    @property
    def address(self):
        return self.address
    
    @address.setter
    def address(self, address):
        self.address = address