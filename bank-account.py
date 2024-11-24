class BankAccount:
    id = int
    balance = float
    first_name = str
    last_name = str

    def __init__(self, id, balance, first_name, last_name):
        self.id = id
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name


    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than is in the account")
        else:
            self.balance -= amount


    def deposit(self, amount):
        self.balance += amount


    def transfer_from(self, amount, to_account):
        pass


    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}, Balance: {self.balance}"


def main():
    j_smith = BankAccount(1, 0, 'John', 'Smith')
    h_rollins = BankAccount(2, 0, 'Harry', 'Rollins')
    l_sampson = BankAccount(3, 0, 'Lucy', 'Sampson')

    print(j_smith)
    print(h_rollins)
    print(l_sampson)
    print("\n")

    j_smith.deposit(int(input("How much do you want to deposit? ")))
    h_rollins.deposit(int(input("How much do you want to deposit? ")))
    l_sampson.deposit(int(input("How much do you want to deposit? ")))
    print("\n")

    print(j_smith)
    print(h_rollins)
    print(l_sampson)
    print("\n")

    j_smith.withdraw(int(input("How much do you want to withdraw? ")))
    h_rollins.withdraw(int(input("How much do you want to withdraw? ")))
    l_sampson.withdraw(int(input("How much do you want to withdraw? ")))

    print(j_smith)
    print(h_rollins)
    print(l_sampson)
    print("\n")

main()