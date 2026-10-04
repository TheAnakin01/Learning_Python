class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        if n < 0:
            raise ValueError("Negative Input")
        self._balance += n

    def withdraw(self, n):
        if n < 0 or n > self._balance:
            raise ValueError("Invalid Input")
        self._balance -= n

acc = BankAccount()
acc.deposit(200)
acc.withdraw(100)
print(acc.balance)

try:
    acc.withdraw(1000)
except ValueError as e:
    print(f"Transaction Failed: {e}")

print(f"Final Balance: {acc.balance}") 