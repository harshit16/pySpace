"""
https://leetcode.com/problems/simple-bank-system/description/

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:

The given account number(s) are between 1 and n, and
The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
Implement the Bank class:

Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.


Example 1:

Input
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
Output
[null, true, true, true, false, false]
"""


class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= len(self.balance) and 1 <= account2 <= len(self.balance):
            if self.balance[account1 - 1] >= money:
                self.balance[account1 - 1] = self.balance[account1 - 1] - money
                self.balance[account2 - 1] = self.balance[account2 - 1] + money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.balance):
            self.balance[account - 1] = self.balance[account - 1] + money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.balance):
            if self.balance[account - 1] >= money:
                self.balance[account - 1] = self.balance[account - 1] - money
                return True
            else:
                return False


# Your Bank object will be instantiated and called as such:
if __name__ == "__main__":
    obj = Bank([10, 100, 20, 50, 30])
    param_1 = obj.transfer(5, 1, 20)
    param_2 = obj.deposit(5, 20)
    param_3 = obj.withdraw(3, 10)
    print(f"Transfer result: {param_1}")
    print(f"Deposit result: {param_2}")
    print(f"Withdraw result: {param_3}")
    print(f"Balances: {obj.balance}")