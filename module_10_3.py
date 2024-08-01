import threading
from threading import Thread

lock = threading.Lock
lock1 = threading.Lock

class BankAccount():

    def __init__(self, account):
        self.account = account
        self.account = 1000

    def deposit_task(self, amount):
        for i in range(5):
            with lock():
                self.account += amount
                print(f'Deposited {amount}, new balance is {self.account}')


    def withdraw_task(self, amount):
        for i in range(5):
            with lock1():
                self.account -= amount1
                print(f'Withdrew {amount1}, new balance is {self.account}')


account = BankAccount(1000)
amount = 100
amount1 =150

deposit_thread = threading.Thread(target=account.deposit_task(amount=amount), args=(1000, ))
withdraw_thread = threading.Thread(target=account.withdraw_task(amount=amount1), args=(1000, ))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()