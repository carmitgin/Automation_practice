class BankAccount:  
    def __init__(self, owner_name:str, balance:int):
        self.owner_name = owner_name
        self.balance = balance

#get the balance before actions
    def get_balance(self) ->int:
        return self.balance

# Dynamic function 1
    def deposit(self, amount:int) -> None:
         self.balance += amount

# Dynamic function 2
    def withdraw(self, amount:int) -> None:
        self.balance -= amount


    def show_account_info(self) ->str:
       return f"Account owner: {self.owner_name}, Balance: {self.balance}"

    # Static function
    @staticmethod
    def is_valid_amount(amount: int):
        if amount > 0:
            return True
        else:
            return False

if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    print(account.show_account_info())
    account.deposit(500)
    print(account.show_account_info())
    account.withdraw(20)
    print(account.show_account_info())