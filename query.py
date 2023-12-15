import mysql.connector

class Query():
    def __init__(self):
        self.host = None
        self.user = None
        self.password = None
        self.database = None
        self.connect = None
        self.cursor = None
    
    def connection(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connect = mysql.connector.connect(host = host, user = user, passwd = password, database = database)
        self.cursor = self.connect.cursor()
        return True

    def login(self, id, password):
        self.cursor.execute(f'SELECT * FROM user WHERE id="{id}" and password="{password}"')
        return self.cursor.fetchone()

    def tambahAkun(self, data):
        self.cursor.execute(f'INSERT INTO list_registrasi (id, nama, pin, password, status) VALUES ("{data[0]}", "{data[1]}", "{data[2]}", "{data[3]}", "False")')
        self.connect.commit()

    def register(self, data):
        self.cursor.execute(f'SELECT * FROM user WHERE id="{data[0]}"')
        check = self.cursor.fetchone()
        if check:
            return 'Id Sudah Terdaftar, Silahkan Masuk ke Akun anda'
        self.cursor.execute(f'INSERT INTO user (id, nama, pin, password, saldo, saving, id_tipe) VALUES ("{data[0]}", "{data[1]}", "{data[2]}", "{data[3]}", "0", "0", "34521")')
        self.connect.commit()
        return True
    
    def changePassword(self, new, id):
        self.cursor.execute(f'UPDATE user SET password = "{new}" WHERE id = "{id}"')
        self.connect.commit()
    
    def informasiPenarikan(self):
        self.cursor.execute(f'SELECT * FROM list_withdraw WHERE status=0')
        return self.cursor.fetchall()
    
    def konfirmasiPenarikan(self, id, jumlah_penarikan):
        self.cursor.execute(f"DELETE FROM list_withdraw WHERE id='{id}' ")
        self.connect.commit()
        self.cursor.execute(f"UPDATE user SET saldo = saldo - %s WHERE id=%s", (jumlah_penarikan, id))
        self.connect.commit()
        return True
    
    def dataAkun(self):
        self.cursor.execute('SELECT * FROM user WHERE id_tipe=34521')
        return self.cursor.fetchall()

    def cekSaldo(self, id):
        self.cursor.execute(f"SELECT saldo FROM user WHERE id='{id}'")
        return self.cursor.fetchone()
    
    def cariAkunCustomer(self, id):
        self.cursor.execute(f"SELECT * FROM user WHERE id='{id}' ")
        return self.cursor.fetchone()

    def buatakunTeller(self, data):
        self.cursor.execute(f"INSERT INTO user (id, nama, pin, password, saldo, saving, id_tipe ) VALUES (%s, %s, %s, %s, 0, 0, 11150)", (data[0], data[1], data[2], data[3]))
        self.connect.commit()
    
    def deposito(self, id, jumlah):
        self.cursor.execute(f'UPDATE user SET saldo = saldo + %s WHERE id = %s', (jumlah, id))
        self.connect.commit()

    def withdraw(self, id, saldo, data, pin):
        if data[1] == pin:
            self.cursor.execute(f'INSERT INTO list_withdraw (id, saldo, amount, status ) VALUES(%s, %s, %s, %s)', (id, saldo, data[0], False))
            self.connect.commit()
            print('Penarikan saldo membutuhkan konfirmasi teller, Harap menunggu Konfirmasi')
        else:
            print('Pin yang anda masukkan Salah')

    def informasiRegistrasi(self):
        self.cursor.execute('SELECT * FROM list_registrasi WHERE status=0')
        return self.cursor.fetchall()
    
    def konfirmasiRegistrasi(self, data):
        self.cursor.execute(f'DELETE FROM list_registrasi WHERE id="{data[0]}"')
        self.connect.commit()
        self.cursor.execute(f'INSERT INTO user (id, nama, pin, password, saldo, saving, id_tipe) VALUES (%s, %s, %s, %s, 0, 0, 34521)', (data[0], data[1], data[2], data[3]))
        self.connect.commit()

    def savingMoney(self, data, saving):
        if data[1] == saving[1]:
            self.cursor.execute(f'UPDATE user SET saldo = saldo - "{saving[0]}", saving = saving + "{saving[0]}" WHERE id = "{data[0]}"')
            self.connect.commit()
        else:
            print('Pin yang anda masukkan Salah')