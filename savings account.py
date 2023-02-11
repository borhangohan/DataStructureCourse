class SavingsAccount:
    def __init__(self, balance=0):
        self.balance=balance
    def deposit(self, amount):
        if amount<500:
            return 'Minimum deposit amount is 500!!'
        else:
            self.balance += amount
            return f'{amount} hase been deposited to your account. Your current balance is {self.balance}'
    def withdraw(self, amount):
        if amount<10000:
            return 'Minimum withdrawal amount is 10000.'
        elif amount>self.balance:
            return 'Insufficient balance!'
        else:
            self.balance-=amount
            return f'{amount} has been deposited from your account. Your current balance is {self.balance}.'
    def CheckAmount(self):
        return f'Your current balance is {self.balance}'
account=SavingsAccount()
print(account.deposit(int(input('Enter the amount you want to deposit:'))))
print(account.withdraw(int(input('Enter the amount you want to withdraw:'))))
print(account.CheckAmount())