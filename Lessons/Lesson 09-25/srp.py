class Account:

    # def __init__(self, account_number):
    #     self.account_number = account_number

    def __init__(self, account_number, db_helper):
        self.account_number = account_number
        self.db_helper = db_helper

    def get_account_number(self):
        return self.account_number

    #Violation:
    #def save(self, db_connection): 
        #saving an account data to db
        #pass
    
    def save(self):
        self.db_helper.save()

class DBHelper:

    def save(self):
        pass
