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
        self.connect = mysql.connector.connect(host = host, user = user, passwd = password, database = database)
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        print('hallo')

        self.cursor = self.connect.cursor()

    def login(self, id, password):
        self.cursor.execute(f'SELECT * FROM user WHERE id="{id}" and password="{password}"')
        return self.cursor.fetchone()

    def tipeAkun(self):
        self.cursor.execute('SELECT * FROM tipe_akun')
        return self.cursor.fetchall()
    
    def konfirmasiPenarikan(self):
        self.cursor.execute(f'SELECT * FROM list_withdraw WHERE status="False" ')
        return self.cursor.fetchall()