import unittest

from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(55)

    def test_deposit(self):
        self.account.deposit(43)
        self.assertEqual(self.account.balance, 98)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw(self):
        self.account.withdraw(20)
        self.assertEqual(self.account.balance, 35)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_withdraw_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_transfer(self):
        other_account = BankAccount(30)
        self.account.transfer(other_account, 25) # transfer from account to other_account
        self.assertEqual(self.account.balance, 30) # after transfer, account should have 30 (55 - 25)
        self.assertEqual(other_account.balance, 55) # after transfer, other_account should have 55 (30 + 25)

    def test_transfer_insufficient_funds(self):
        other_account = BankAccount(30)
        with self.assertRaises(Exception):
            self.account.transfer(other_account, 100) # attempt to transfer 100 from self.account to other_account, which should raise an exception due to insufficient funds

    def test_transfer_invalid_account(self):
        with self.assertRaises(TypeError):
            self.account.transfer("fraud account", 10) # Attempt to transfer to an invalid account, which should raise a TypeError

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 55)

    def test_get_balance_after_transactions(self):
        self.account.deposit(45) # 45 + 55 = 100
        self.account.withdraw(20) # 100 - 20 = 80
        self.assertEqual(self.account.get_balance(), 80)

    def test_get_balance_after_deposit(self):
        self.account.withdraw(10)
        self.assertEqual(self.account.get_balance(), 45)

    def test_get_balance_after_withdrawal(self):
        self.account.withdraw(10)
        self.assertEqual(self.account.get_balance(), 45)