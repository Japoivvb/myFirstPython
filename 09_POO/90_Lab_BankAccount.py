"""
STATEMENT:
----------
Create a bank account system using classes and inheritance.

REQUIREMENTS:
-------------
1. Base class BankAccount with:
   - Private attributes: holder, balance
   - Constructor that accepts holder and initial balance (default 0)
   - Methods: deposit, withdraw, show_balance

2. SavingsAccount subclass inheriting from BankAccount:
   - Additional private attribute: annual_interest (%)
   - Constructor that accepts holder, initial balance, and interest
   - Method: apply_interest

3. CheckingAccount subclass inheriting from BankAccount:
   - Additional private attribute: overdraft_limit
   - Constructor that accepts holder, initial balance, and overdraft limit
   - Override the withdraw method to allow overdrafts up to the limit

CONCEPTS TO APPLY:
------------------
- self: reference to the class instance
- Private attributes: __attribute_name (double underscore)
- Inheritance: class SubClass(BaseClass)
- super(): call the base class constructor
- Method overriding: redefine methods in subclasses

EXPECTED USAGE EXAMPLE:
-----------------------
account1 = BankAccount("Anna", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.show_balance()

savings = SavingsAccount("Peter", 2000, 3.5)
savings.apply_interest()
savings.show_balance()

checking = CheckingAccount("Maria", 500, 1000)
checking.withdraw(1200)  # Overdraft allowed
checking.show_balance()
"""
class BankAccount:
    currency = "$"
    def __init__(self, holder, balance=0): # constructor
        self.__holder = holder 
        self.__balance = balance 
    
    def deposit(self, amount): 
        self.__balance += amount 

    def withdraw(self, amount): 
        self.__balance -= amount 

    def show_balance(self): 
        print(self.__balance)

    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance

class SavingsAccount(BankAccount):
    def __init__(self, holder, balance, annual_interest): # constructor
        super().__init__(holder, balance)
        self.__annual_interest = annual_interest 
    
    def apply_interest(self): 
        current_balance = self._get_balance()
        # other way to access private super attribute with self._Class_attribute
        # current_balance = self._BankAccount__balance
        new_balance = current_balance + (current_balance * self.__annual_interest / 100)
        self._set_balance(new_balance)

class CheckingAccount(BankAccount):
    def __init__(self, holder, balance, overdraft_limit):
        super().__init__(holder, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        current_balance = self._get_balance()
        if current_balance - amount >= -self.__overdraft_limit:
            self._set_balance(current_balance - amount)
        else:
            print("Insufficient funds: overdraft limit exceeded")

account1 = BankAccount("Anna", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.show_balance()

savings = SavingsAccount("Peter", 2000, 3.5)
savings.apply_interest()
savings.show_balance()

checking = CheckingAccount("Maria", 500, 1000)
checking.withdraw(1200)  # Overdraft allowed
checking.show_balance()

# print all properties (instance and class)
print(account1.__dict__, account1.currency)
print(savings.__dict__, savings.currency)
print(checking.__dict__, checking.currency)

    