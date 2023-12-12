from user import User
from query import Query

db = Query()

class Teller(User):
    def __init__(self):
        super().__init__()
    
    def checkSaldoCustomer(self):
        id = input("Id = ")
        cek = db.cekSaldo(id)

    def konfirmasiPenarikan(self):
        penarikan = db.konfirmasiPenarikan()
        for i in penarikan:
            print (f"ID : {penarikan[0]}, amount:{penarikan[2]}")
            konfirm= input("Konfirmasi penarikan ini? [Y/T]: ")
            if konfirm.lower == "Y":
                self.cursor.execute("DELETE from list_whitdraw where id={penarikan[0]} ")