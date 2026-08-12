from pathlib import Path

class BankAccount:
    def __init__(self, owner, balance=0, transactions=None):
        self.owner = owner
        self.balance = balance
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit +{amount}")

        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw -{amount}")

        else:
            print("Insufficient balance.")

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def display(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, owner):
        for account in self.accounts:
            if account.owner == owner:
                return account

        return None

    def show_all_accounts(self):
        for account in self.accounts:
            print(f"{account.owner}: {account.balance}")

    def save_accounts(self, filename):
        path = Path(filename)

        contents = ''

        for account in self.accounts:
            contents += (
                f"{account.owner},"
                f"{account.balance},"
                f"{'|'.join(account.transactions)}\n"
                )

        path.write_text(contents, encoding="utf-8")

        print("Account saved.")

    def load_accounts(self, filename):
        path = Path(filename)

        self.accounts = []
        try:
            contents = path.read_text(encoding="utf-8")

        except FileNotFoundError:
            print("File not found.")
            return
        
        else:
            lines = contents.splitlines()

            for line in lines:
                owner, balance, transaction = line.split(",")
                account = BankAccount(owner, int(balance), transaction.split("|"))
                self.accounts.append(account)

bank = Bank()

a1 = BankAccount("Alice")
a2 = BankAccount("Bob")

a1.deposit(1000)
a1.withdraw(300)

a2.deposit(500)

bank.add_account(a1)
bank.add_account(a2)

bank.show_all_accounts()

bank.save_accounts("accounts.txt")