import random
from query import Query

database = Query()
database.connection('localhost', 'root', '', 'bank_ini')


class User:
    def __init__(self):
        self.id = None
        self.nama = None
        self._pin = None
        self.__password = None

    def generateId(self):
        listId = []
        listchoice = [0, 1, 2, 3, 4, 5, 6,7 ,8 ,9]
        for i in range(5):
            choice = random.choice(listchoice)
            listId.append(str(choice))
        return int(''.join(listId))

    def inputData(self):
        self.id = self.generateId()
        self.nama = str(input('Masukkan Nama Anda : '))
        self._pin = int(input('Masukkan Pin yang anda inginkan : '))
        self.__password = str(input('Masukkan Password Anda : '))

        return self.id, self.nama, self._pin, self.__password
    
    def printInfo(self, data):
        print('\nInformasi Akun')
        print('=====================================')
        print(f'Id : {data[0]}')
        print(f'Nama : {data[1]}')
        print(f'Password : {data[3]}')
        print('=====================================\n')

    def login(self):
        id = int(input('Masukkan ID Anda : '))
        password = str(input('Masukkan Password Anda : '))

        check = database.login(id, password)
        if check:
            self.id = check[0]
            self.nama = check[1]
            self._pin = check[2]
            self.__password = check[3]
            return check
        return False
    
    def passChanger(self, new):
        self.changePassword = new
        database.changePassword(new, self.id)
    
    @property
    def changePassword(self):
        return self.__password
    @changePassword.setter
    def changePassword(self, newPass):
        self.__password = newPass

    def logout(self):
        return False

