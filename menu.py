import os
from pyfiglet import Figlet

from user import User
from customer import Customer
from query import Query

database = Query()
dataUser = User()


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
        if login[6] == 34521:
            menu(listMenuCustomer)
            
    
database.connection('localhost', 'root', '', 'bank_ini')
mainMenu()