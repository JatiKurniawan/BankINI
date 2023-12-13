import os
from pyfiglet import Figlet

from user import User
from customer import Customer
from teller import Teller
from query import Query

database = Query()
database.connection('localhost', 'root', '', 'bank_ini')

dataUser = User()
dataCustomer = Customer()
dataTeller = Teller()


listMenuCustomer = ['Setor Tunai', 'Penarikan Tunai', 'Informasi Saldo', 'Informasi Akun']
listMenuTeller = ['Konfirmasi Penarikan', 'Cari Akun Customer']
listMenuAdmin = ['History', 'Cari Akun Customer', 'Buat Akun Teller', 'Konfirmasi Registrasi']



def menu(list):
    for i in range(len(list)):
        print(f'{i+1}. {list[i]}')
    print('0. Keluar')

    choice = int(input('Masukkan pilihan anda : '))
    return choice

def mainMenu():
    while True:
        # os.system(('cls'))
        f = Figlet(font='slant')
        print(f.renderText('Bank INI'))
        login = dataUser.login()
        if login :
            if login[6] == 34521:
                dataCustomer.inputData(login)
                while True:
                    choiceCustomer = menu(listMenuCustomer)
                    if choiceCustomer == 1:
                        deposito = dataCustomer.deposito()
                        database.deposito(login[0], deposito)
                    elif choiceCustomer == 2:
                        withdraw = dataCustomer.withdraw()
                        database.withdraw(login[0], dataCustomer.saldo, withdraw, login[2])
                    elif choiceCustomer == 3:
                        saldo = database.cekSaldo(login[0])
                        dataCustomer.checkSaldo([login[0], login[1], saldo])
                    elif choiceCustomer == 4:
                        data = database.cariAkunCustomer(login[0])
                        dataCustomer.checkAkun(data)
                        

            elif login[6] == 98710:
                print(login[0])
                choiceTeller = menu(listMenuTeller)
                if choiceTeller == 1:
                    dataTeller.konfirmasiPenarikan()

            elif login[6] == 11150:
                menu(listMenuAdmin)
        else:
            print('\nPassword atau Username Salah')
            signup = str(input('Buat Akun? <y/n>'))
            if signup.lower() == 'y':
                dataSign = dataUser.inputData()
                print(dataSign)
                database.register(dataSign)
                dataUser.printInfo(dataSign)
    
mainMenu()