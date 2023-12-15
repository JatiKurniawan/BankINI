from user import User

class Customer(User):
    def __init__(self):
        super().__init__()
        self.saldo = None
        self.__saving = None

    def inputData(self, data):
        self.saldo = data[4]
        self.saving = data[5]

    def checkSaldo(self, data):
        print('\n=====================================')
        print(f'Nama Customer : {data[1]} ({data[0]})')
        print(f'Saldo Customer : {data[2][0]}')
        print('=====================================\n')

    def checkAkun(self, data):
        print('\n=====================================')
        print(f'Nama Customer : {data[1]} ({data[0]})')
        print(f'Saldo Customer : {data[4]}')

        print(f'\nPin = {data[2]}')
        print(f'Password = {data[3]}')
        print('=====================================\n')

        change = str(input('Ubah Password ? <yes/no> : '))
        if change.lower() == 'yes' :
            newPass = str(input('Masukkan Password baru Anda : '))
            return newPass

    def deposito(self):
        print(f'Saldo Anda Sekarang : Rp {self.saldo}')
        deposito = int(input('Jumlah Deposito : Rp '))
        self.saldo = self.saldo + deposito
        return deposito

    def withdraw(self):
        print(f'Saldo Anda Sekarang : Rp {self.saldo}')
        withdraw = int(input('Jumlah Penarikan : Rp '))
        pin = int(input('Masukkan Pin anda : '))
        return withdraw, pin
    
    def savingMoney(self):
        print(f'Saldo Anda Sekarang : Rp {self.saldo}')
        print(f'Saldo Tabungan Anda Sekarang : Rp {self.saving}')
        print('Note : Jumlah maksimal Tabungan adalah 75% dari total saldo')
        saving = int(input('Jumlah Tabungan : Rp '))
        if saving < (self.saldo*75/100):
            pin = int(input('Masukkan Pin anda : '))
            return saving, pin
        print('Jumlah tabungan yang Anda masukkan terlalu besar')
    
    def register(self):
        print('register')