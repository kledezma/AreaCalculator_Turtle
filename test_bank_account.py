import unittest
from bank_account import BankAccount

class TestCalculator(unittest.TestCase):

  # Setup method: New Calculator instance before each test
  def setUp(self):
    self.account = BankAccount(100)

  # Teardown method: Clean up resources after each test
  def tearDown(self):
    self.account = None

  def test_initial_balance(self):
    self.assertEqual(self.account.balance, 100)

  def test_deposit_positive_amount(self):
    self.account.deposit(50)
    self.assertEqual(self.account.balance, 150)

if __name__ == '__main__':
  unittest.main()