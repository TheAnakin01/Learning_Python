class Vault:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Vault(self.amount + other.amount)

    def __str__(self):
        return f"{self.amount} Galleons"

v1 = Vault(100)
v2 = Vault(200)
v3 = v1 + v2
print(v3)