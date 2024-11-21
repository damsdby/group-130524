class Client:
    def __init__(self, name: str, balance: int, checking_account: bool):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount: int) -> str:
        if amount < 0:
            raise ValueError("Amount to withdraw cannot be negative")
        if amount > self.balance:
            raise ValueError("Not enough funds to withdraw")

        self.balance -= amount
        return f"Account balance for {self.name} is {self.balance}"

    def transfer(self, other: 'Client', amount: int) -> str:
        if amount < 0:
            raise ValueError("Amount to transfer cannot be negative")
        if not other.checking_account:
            raise ValueError(f"User {other.name} is not valid")
        if amount > self.balance:
            raise ValueError("Not enough funds to transfer")

        self.balance -= amount
        other.balance += amount
        return f"Account balance for {self.name} is {self.balance} and account balance for {other.name} is {other.balance}"

    def deposit(self, amount: int) -> str:
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative")

        self.balance += amount
        return f"Account balance for {self.name} is {self.balance}"


Taras = Client('Taras', 120, True)
Pavlo = Client('Pavlo', 95, False)



try:
    print(Pavlo.transfer(Taras, 25))
except ValueError as e:
    print(e)

Pavlo.checking_account = True

try:
    Taras.withdraw(-5)
except ValueError as e:
    print(e)

try:
    Pavlo.deposit(-10)
except ValueError as e:
    print(e)

print(Taras.withdraw(2))
print(Pavlo.deposit(20))
print(Taras.transfer(Pavlo, 25))
