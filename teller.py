from user import User
from query import Query

database = Query()
database.connection('localhost', 'root', '', 'bank_ini')


class Teller(User):
    def __init__(self):
        super().__init__()

    def checkSaldoCustomer(self):
        id = input("Id = ")
        cek = database.cekSaldo(id)

    def konfirmasiPenarikan(self):
        penarikan = database.informasiPenarikan()
        for i in penarikan:
            print('=====================================')
            print(f'ID Customer         : {i[0]}')
            print(f'Withdraw Amount     : {i[2]}')
            print(f'Saldo Customer      : {i[1]}')
            confirm = str(input('Konfirmasi ? : '))
            if confirm.lower() == 'yes':
                database.konfirmasiPenarikan(i[0], i[2])
        
                