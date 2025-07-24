class BankAccount:
    def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self,money):
        self.balance += money
    
    def withdraw(self,money):
        self.balance -= money
    
    def display_balance(self):
        print(self.balance)


firstAccount = BankAccount('Byron','Ferreira',0,'Normal',4567,0.0)

firstAccount.display_balance()
firstAccount.deposit(96.0)
firstAccount.display_balance()
firstAccount.withdraw(25.0)
firstAccount.display_balance()
