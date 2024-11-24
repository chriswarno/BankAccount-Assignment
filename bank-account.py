class BankAccount:
    #variables for BankAccount class
    id = int
    balance = float
    first_name = str
    last_name = str

    #__init__ module to construct BankAccount class
    def __init__(self, id, balance, first_name, last_name):
        self.id = id
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name


    #module to withdraw money from one bank account
    def withdraw(self, amount):
        #if statement to determine if there is enough money for the withdrawal
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than is in the account") #ValueError if there isn't enough money in the account
        else:
            self.balance -= amount


    #module to deposit money into an account
    def deposit(self, amount):
        self.balance += amount

    #module to transfer money to an account
    def transfer_from(self, amount, to_account):
        pass


    #__str__ module to print the object
    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}, Balance: {self.balance}"


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
    j_smith.deposit(int(input("How much do you want to deposit? ")))
    h_rollins.deposit(int(input("How much do you want to deposit? ")))
    l_sampson.deposit(int(input("How much do you want to deposit? ")))
    print("\n")

    print(j_smith)
    print(h_rollins)
    print(l_sampson)
    print("\n")

    #withdrawing money from the accounts
    j_smith.withdraw(int(input("How much do you want to withdraw? ")))
    h_rollins.withdraw(int(input("How much do you want to withdraw? ")))
    l_sampson.withdraw(int(input("How much do you want to withdraw? ")))

    print(j_smith)
    print(h_rollins)
    print(l_sampson)
    print("\n")

main()