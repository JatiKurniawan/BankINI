from user import User

class Teller(User):
    def __init__(self):
        super().__init__()
    
    def checkSaldoCustomer(self):
        print('cek')

    def konfirmasiPenarikan(self):
        print('confirm')