from bank_account import BankAccount


def test_create_account():
    test_account = BankAccount("Yossi",1000)
    assert test_account.get_balance() == 1000
