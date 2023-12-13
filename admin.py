from user import User
from query import Query

database = Query()
database.connection('localhost', 'root', '', 'bank_ini')

class Admin(User):
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
        print(f'ID Customer         : {data[0]}')
        print(f'Nama Customer       : {data[1]}')
        print(f'Saldo Customer      : {data[5]}')

        print(f'\nPin Customer      : {data[2]}')
        print(f'Password Customer   : {data[3]}')
        print('=====================================\n')

    def akunTeller(self):
        id = self.generateId()
        nama = str(input('Masukkan Nama : '))
        pin = int(input('Masukkan 6 digit Pin : '))
        password = str(input('Masukkan Password : '))

        return id, nama, pin, password
        
    def konfirmasiRegistrasi(self, data):
        print('=====================================\n')
        for i in data:
            print(f'Customer : {i[1]} ({i[0]})')
            confirm = str(input('Konfirmasi ? '))
            if confirm.lower() == 'yes':
                database.konfirmasiRegistrasi([i[0], i[1], i[2], i[3]])