#Hide data + control how it is accessed
#Bank account with encapsulation

class Bank():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"{amount} withdrawn"
        else:
            return "Insufficient amount"
        
    def get_balance(self):
        return self.__balance
    
acc = Bank(5000)
acc.deposit(1000)
print(acc.withdraw(4500))
print(acc.get_balance())

        
