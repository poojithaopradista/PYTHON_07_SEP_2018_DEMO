class InsufficientBalanceError(Exception):
    def __init__(self,message="Insufficient Balance"):
        self.message = message

class Account:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def __eq__(self, other):
        return self.acno == other.acno

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientBalanceError("Insufficient Balance. Balance is " + str(self.balance))

    def get_balance(self):
        return self.balance

    def print_details(self):
        print("Account No              : ",self.acno)
        print("Account Holder's Name   : ",self.ahname)
        print("Current Balance         : ",self.balance)


a1 = Account(1, "Mr. Steve",10000)
try:
    a1.withdraw(20000)
    print("Use that amount")
except Exception as ex:
    print("Error : ", ex.message)


