import os
from pyfiglet import Figlet

from query import Query

from user import User
from customer import Customer
from teller import Teller
from admin import Admin

database = Query()
database.connection('localhost', 'root', '', 'bank_ini')

dataUser = User()
dataCustomer = Customer()
dataTeller = Teller()
dataAdmin = Admin()


listMenuCustomer = ['Setor Tunai', 'Penarikan Tunai', 'Menabung',  'Informasi Saldo', 'Informasi Akun']
listMenuTeller = ['Konfirmasi Penarikan', 'Cari Akun Customer']
listMenuAdmin = ['Cari Akun Customer', 'Buat Akun Teller', 'Konfirmasi Registrasi']


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
                        saving = dataCustomer.savingMoney()
                        if saving:
                            database.savingMoney([login[0], login[2]], saving)
                        else:
                            pass
                    elif choiceCustomer == 4:
                        saldo = database.cekSaldo(login[0])
                        dataCustomer.checkSaldo([login[0], login[1], saldo])
                    elif choiceCustomer == 5:
                        data = database.cariAkunCustomer(login[0])
                        change = dataCustomer.checkAkun(data)
                        if change:
                            dataUser.passChanger(change)
                    elif choiceCustomer == 0:
                        return dataUser.logout()
                    
            elif login[6] == 98710:
                while True:
                    choiceTeller = menu(listMenuTeller)
                    if choiceTeller == 1:
                        dataTeller.konfirmasiPenarikan()
                    elif choiceTeller == 2:
                        id = dataTeller.printIdCustomer()
                        data = database.cariAkunCustomer(id)
                        dataTeller.checkCustomer(data)
                    elif choiceTeller == 0:
                        return dataUser.logout()

            elif login[6] == 11150:
                while True:
                    choiceAdmin = menu(listMenuAdmin)
                    if choiceAdmin == 1:
                        id = dataAdmin.printIdCustomer()
                        data = database.cariAkunCustomer(id)
                        dataAdmin.checkCustomer(data)
                    elif choiceAdmin == 2:
                        data = dataAdmin.akunTeller()
                        database.buatakunTeller(data)
                    elif choiceAdmin == 3:
                        data = database.informasiRegistrasi()
                        dataAdmin.konfirmasiRegistrasi(data)
                    elif choiceAdmin == 0:
                        return dataUser.logout()

        else:
            print('\nPassword atau Username Salah')
            signup = str(input('Buat Akun? <y/n>'))
            if signup.lower() == 'y':
                dataSign = dataUser.inputData()
                database.tambahAkun(dataSign)
                dataUser.printInfo(dataSign)
                print('\nPembuatan akun membutuhkan konfirmasi Admin Bank. Harap Menunggu Konfirmasi\n')
    
mainMenu()