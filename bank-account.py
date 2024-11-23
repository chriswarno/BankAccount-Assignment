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
        pass


def main():
    j_smith = BankAccount(1, 'John', 'Smith')
    h_rollins = BankAccount(2, 'Harry', 'Rollins')
    l_sampson = BankAccount(3, 'Lucy', 'Sampson')
