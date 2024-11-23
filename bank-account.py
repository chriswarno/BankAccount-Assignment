class BankAccount:
    id = int
    balance = float
    first_name = str
    last_name = str

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


    def withdraw(self, amount):
        self.amount = amount


    def deposit(self, amount):
        self.amount = amount


    def transfer_from(self, amount, to_account):
        self.amount = amount
        self.to_account = to_account


    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}, Balance: {self.balance}"


def main():
    j_smith = BankAccount(1,'John', 'Smith')
    h_rollins = BankAccount(2, 'Harry', 'Rollins')
    l_sampson = BankAccount(3, 'Lucy', 'Sampson')

    j_smith.deposit(100)

    print(j_smith)
    print(h_rollins)
    print(l_sampson)

main()