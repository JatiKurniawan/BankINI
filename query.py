import mysql.connector

class Query():
    def __init__(self):
        pass
    
    def connection(self, host, user, password, database):
        self.connect = mysql.connector.connect(host = host, user = user, password = password, database = database)
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.cursor = self.connect.cursor()

    def tipeAkun(self):
        self.cursor.execute('SELECT * FROM tipe_akun')
        return self.cursor.fetchall()
    
    def konfirmasiPenarikan(self):
        self.cursor.execute(f'SELECT * FROM list_withdraw WHERE status="False" ')
        return self.cursor.fetchall()