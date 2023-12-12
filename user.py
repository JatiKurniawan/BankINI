import random

class User:
    def __init__(self):
        self.id = None
        self.nama = None
        self.pin = None
        self.password = None

    def generateId(self):
        listId = []
        listchoice = [0, 1, 2, 3, 4, 5, 6,7 ,8 ,9]
        for i in range(4):
            choice = random.choice(listchoice)
            listId.append(str(choice))
        return int(''.join(listId))

    def inputData(self):
        self.id = self.generateId()
        self.nama = str(input('Masukkan Nama Anda : '))
        self.pin = int(input('Masukkan Pin yang anda inginkan : '))
        self.password = str(input('Masukkan Password Anda : '))

    def login(self):
        id = int(input('Masukkan ID Anda : '))
        password = str(input('Masukkan Password Anda : '))

        return id, password
    
    def logout(self):
        return False