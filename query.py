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