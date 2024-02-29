class Family:
    def __init__(self, family_code, family_name, address, user_code):
        self.__family_code = family_code
        self.__family_name = family_name
        self.__address = address
        self.__user_code = user_code
    
    @property
    def family_code(self):
        return self.__family_code
    
    @family_code.setter
    def family_code(self, family_code):
        self.__family_code = family_code

    
    @property
    def family_name(self):
        return self.__family_name
    
    @family_name.setter
    def family_name(self, family_name):
        self.__family_name = family_name
    
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
    
    @property
    def user_code(self):
        return self.__user_code
    
    @user_code.setter
    def user_code(self, user_code):
        self.__user_code = user_code