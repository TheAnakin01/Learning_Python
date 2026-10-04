import pytest
from bank import BankAccount

def test_withdrawal_too_much():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.withdraw(50)

def test_negative_deposit():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.deposit(-200)

def test_negative_withdrawal():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.withdraw(-200)

def test_normal_answer():
    acc = BankAccount()
    acc.deposit(200)
    assert acc.balance == 200
    acc.withdraw(20)
    assert acc.balance == 180
    
    