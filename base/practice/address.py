from domain.company import Company
from domain.account import Account
from domain.user import User
from domain.family import Family


class CommonFormData:
    company_code: int
    company_name: str
    master_obj: Company | Account | User | Family


company1 = Company(10001, 'A社', 10001, '東京都港区')
company2 = Company(10002, 'B社', 10002, '東京都足立区')
company3 = Company(10003, 'C社', 10003, '東京都世田谷区')
company4 = Company(10004, 'D社', 10004, '東京都渋谷区')
company5 = Company(10005, 'E社', 10005, '東京都新宿区')
company6 = Company(10006, 'W社', 10006, '大阪府大阪市')

account1 = Account(10001, 'a_10001', 10001, '１丁目１番地', 10001)
account2 = Account(10002, 'a_10002', 10002, '１丁目２番地', 10001)
account3 = Account(10003, 'b_10003', 10003, '２丁目１番地', 10002)
account4 = Account(10004, 'b_10004', 10004, '２丁目２番地', 10002)
account5 = Account(10005, 'c_10005', 10005, '３丁目１番地', 10003)
account6 = Account(10006, 'c_10006', 10006, '３丁目２番地', 10003)
account7 = Account(10007, 'd_10007', 10007, '４丁目１番地', 10004)
account8 = Account(10008, 'd_10008', 10008, '４丁目２番地', 10004)
account9 = Account(10009, 'e_10009', 10009, '５丁目１番地', 10005)
account10 = Account(10010, 'e_10010', 10010, '５丁目２番地', 10005)
account11 = Account(10011, 'x_10010', 10011, '５丁目２番地', 11111)


user1 = User(10001, 'a_10001', 10001, '１-１', 10001)
user2 = User(10002, 'a_10002', 10002, '１-２', 10001)
user3 = User(10003, 'a_10003', 10003, '２-１', 10002)
user4 = User(10004, 'a_10004', 10004, '２-２', 10002)
user5 = User(10005, 'b_10005', 10005, '３-１', 10003)
user6 = User(10006, 'b_10006', 10006, '３-２', 10003)
user7 = User(10007, 'b_10007', 10007, '４-１', 10004)
user8 = User(10008, 'b_10008', 10008, '４-２', 10004)
user9 = User(10009, 'c_10009', 10009, '５-１', 10005)
user10 = User(10010, 'c_10010', 10010, '５-２', 10005)
user11 = User(10011, 'c_10011', 10011, '６-１', 10006)
user12 = User(10012, 'c_10012', 10012, '６-２', 10006)
user13 = User(10013, 'd_10013', 10013, '７-１', 10007)
user14 = User(10014, 'd_10014', 10014, '７-２', 10007)
user15 = User(10015, 'd_10015', 10015, '８-１', 10008)
user16 = User(10016, 'd_10016', 10016, '８-２', 10008)
user17 = User(10017, 'e_10017', 10017, '９-１', 10009)
user18 = User(10018, 'e_10018', 10018, '９-２', 10009)
user19 = User(10019, 'e_10019', 10019, '１０-１', 10010)
user20 = User(10020, 'e_10020', 10020, '１０-２', 10010)
user21 = User(10021, 'y_10020', 10020, '１０-２', 22222)


family1 = Family(10001, 'a_10001', '101', 10001)
family2 = Family(10002, 'a_10002', '102', 10002)
family3 = Family(10003, 'a_10003', '103', 10003)
family4 = Family(10004, 'a_10004', '104', 10004)
family5 = Family(10005, 'a_10005', '105', 10005)
family6 = Family(10006, 'a_10006', '106', 10006)
family7 = Family(10007, 'a_10007', '107', 10007)
family8 = Family(10008, 'a_10008', '108', 10008)
family9 = Family(10009, 'a_10009', '109', 10009)
family10 = Family(10010, 'a_10010', '110', 10010)
family11 = Family(10011, 'a_10011', '111', 10011)
family12 = Family(10012, 'a_10012', '112', 10012)
family13 = Family(10013, 'a_10013', '113', 10013)
family14 = Family(10014, 'a_10014', '114', 10014)
family15 = Family(10015, 'a_10015', '115', 10015)
family16 = Family(10016, 'a_10016', '116', 10016)
family17 = Family(10017, 'a_10017', '117', 10017)
family18 = Family(10018, 'a_10018', '118', 10018)
family19 = Family(10019, 'a_10019', '119', 10019)
family20 = Family(10020, 'a_10020', '120', 10020)
family21 = Family(10021, 'z_10020', '121', 33333)

companies = []
companies.append(company1)
companies.append(company2)
companies.append(company3)
companies.append(company4)
companies.append(company5)
companies.append(company6)


accounts = []
accounts.append(account1)
accounts.append(account2)
accounts.append(account3)
accounts.append(account4)
accounts.append(account5)
accounts.append(account6)
accounts.append(account7)
accounts.append(account8)
accounts.append(account9)
accounts.append(account10)
accounts.append(account11)


users = []
users.append(user1)
users.append(user2)
users.append(user3)
users.append(user4)
users.append(user5)
users.append(user6)
users.append(user7)
users.append(user8)
users.append(user9)
users.append(user10)
users.append(user11)
users.append(user12)
users.append(user13)
users.append(user14)
users.append(user15)
users.append(user16)
users.append(user17)
users.append(user18)
users.append(user19)
users.append(user20)
users.append(user21)

families = []
families.append(family1)
families.append(family2)
families.append(family3)
families.append(family4)
families.append(family5)
families.append(family6)
families.append(family7)
families.append(family8)
families.append(family9)
families.append(family10)
families.append(family11)
families.append(family12)
families.append(family13)
families.append(family14)
families.append(family15)
families.append(family16)
families.append(family17)
families.append(family18)
families.append(family19)
families.append(family20)
families.append(family21)

first_target_list = []


for company in companies:
    # print(f'company.company_code: {company.company_code}, company.account_code: {company.account_code}')
    
    for account in accounts:    
        # print(f'company.company_code: {company.company_code}, account.company_code: {account.company_code}')
        
        if company.company_code == account.company_code:
            account_dict = {}
            account_dict["company_code"] = company.company_code
            account_dict["company_name"] = company.company_name
            account_dict["obj"] = account
            first_target_list.append(account_dict)
            
            for user in users:
                
                if account.account_code == user.account_code:
                    user_dict = {}
                    user_dict["company_code"] = company.company_code
                    user_dict["company_name"] = company.company_name
                    user_dict["obj"] = user
                    first_target_list.append(user_dict)
                    
                    for family in families:
                        
                        if user.user_code == family.user_code:
                            family_dict = {}
                            family_dict["company_code"] = company.company_code
                            family_dict["company_name"] = company.company_name
                            family_dict["obj"] = family
                            first_target_list.append(family_dict)


print("--------------------------------------------------------------------")

for target in first_target_list:
    # if isinstance(target.get('obj'), Company):
    #     print(target, target.get('obj').company_name)
    # if isinstance(target.get('obj'), Account):
    #     print(target, target.get('obj').account_name)
    # if isinstance(target.get('obj'), User):
    #     print(target, target.get('obj').user_name)
    if isinstance(target.get('obj'), Family):
        print(target, target.get('obj').family_name)