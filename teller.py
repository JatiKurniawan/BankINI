from user import User
from query import Query

database = Query()
database.connection('localhost', 'root', '', 'bank_ini')


class Teller(User):
    def __init__(self):
        super().__init__()

    def printIdCustomer(self):
        akun = database.dataAkun()
        for i, j in enumerate(akun, start=1):
            print(f"{i}. {j[1]} ({j[0]})")
        id = int(input('Pilih ID Customer : '))
        return id

    def checkCustomer(self, data):
        print('\n=====================================')
        print(f'ID Customer     : {data[0]}')
        print(f'Nama Customer   : {data[1]}')
        print(f'Saldo Customer  : {data[5]}')
        print('=====================================\n')

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
        
                