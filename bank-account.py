class BankAccount:
    #variables for BankAccount class
    account_id = int
    balance = float
    first_name = str
    last_name = str

    #__init__ module to construct BankAccount class
    def __init__(self, account_id, balance, first_name, last_name):
        self.account_id = account_id
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name


    #module to withdraw money from one bank account
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("There are not enough funds in the account to withdraw $" + str(amount))
        self.balance -= amount


    #module to deposit money into an account
    def deposit(self, amount):
        self.balance += amount

    #module to transfer money to an account
    def transfer_from(self, amount, to_account):
        if self.balance < amount:
            raise ValueError("There are not enough funds in the account to transfer $" + str(amount))
        self.withdraw(amount)
        to_account.deposit(amount)


    #__str__ module to print the object
    def __str__(self):
        return f"{self.account_id}: {self.first_name} {self.last_name}, Balance: {self.balance}"


def main():
    #object for the bank accounts
    j_smith = BankAccount(1, 0, 'John', 'Smith')
    h_rollins = BankAccount(2, 0, 'Harry', 'Rollins')
    l_sampson = BankAccount(3, 0, 'Lucy', 'Sampson')

    print(j_smith)
    print(h_rollins)
    print(l_sampson)
    print("\n")

    #depositing money into the accounts
    j_smith.deposit(100)
    h_rollins.deposit(100)
    l_sampson.deposit(100)

    print(j_smith)
    print(h_rollins)
    print(l_sampson)
    print("\n")

    #withdrawing money from an account which has enough money
    try:
        j_smith.withdraw(50)
    except ValueError as e:
        print(e)
        print("\n")

    #withdrawing money from an account which doesn't have enough money
    try:
        h_rollins.withdraw(200)
    except ValueError as e:
        print(e)
        print("\n")

    #transfering money and the from account has enough money
    try:
        l_sampson.transfer_from(20, j_smith)
    except ValueError as e:
        print(e)
        print("\n")

    #transfering money and the from account doesn't have enough money
    try:
        l_sampson.transfer_from(200, h_rollins)
    except ValueError as e:
        print(e)
        print("\n")

    #final print
    print(j_smith)
    print(h_rollins)
    print(l_sampson)

main()