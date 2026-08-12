from pathlib import Path

class Transaction:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

    def display(self):
        if self.category == 'income':
            return f"{self.title}: +{self.amount}(income)"
        elif self.category == 'expenditure':
            return f"{self.title}: -{self.amount}(expenditure)"
        else:
            return "Unknown category"

class AccountBook:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        total = 0 

        for transaction in self.transactions:
            if transaction.category == 'income':
                total += transaction.amount

            elif transaction.category == 'expenditure':
                total -= transaction.amount

        return total

    def show_transaction(self):
        for transaction in self.transactions:
            print(transaction.display())

    def save_to_file(self, filename):
        path = Path(filename)

        lines = []

        for transaction in self.transactions:
            line = f"{transaction.title},{transaction.amount},{transaction.category}"
            lines.append(line)

        path.write_text("\n".join(lines),encoding="utf-8")

    def load_from_file(self, filename):
        path = Path(filename)

        try:
            contents  = path.read_text(encoding="utf-8")

        except FileNotFoundError:
            print("File not found.")

        else:
            lines = contents.splitlines()

            for line in lines:
                title, amount, category = line.split(",")

                transaction = Transaction(title, int(amount), category)

                self.add_transaction(transaction)

book = AccountBook()

print("Enter 'q' at any time to quit.")

while True:
    title = input("Enter the title: ")
    if title == 'q':
        break

    amount = input("Enter the amount: ")
    if amount == 'q':
            break
    
    category = input("Enter the category(income/expenditure): ")
    if category == 'q':
            break
    
    amount = int(amount)

    transaction = Transaction(title, amount, category)
    book.add_transaction(transaction)

book.show_transaction()

print(f"Balance: {book.get_balance()}")

book.save_to_file("transaction.txt")