from user import User

class Customer(User):
    def __init__(self):
        super().__init__()
        self.saldo = None
        self.saving = None

    def deposito(self):
        print('deposito')

    def saving(self):
        print('saving')

    def withdraw(self):
        print('withdraw')

    def register(self):
        print('register')