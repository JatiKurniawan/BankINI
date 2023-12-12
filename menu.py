import os
import pyfiglet

from user import User
from customer import Customer

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

