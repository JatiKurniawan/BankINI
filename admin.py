from user import User
from query import Query

db = Query()

class Admin(User):
    def __init__(self):
        super().__init__()
      
    def cekHistory(self):
        
    def cariAkun(self):
        id = input("Cari akun")
        db = db.cariAkunCust(id)
        # print id, nama ,


    def akunTeller(self):
        print("Buat akun teller")
        
    def konirmasiRegistrasi(self):
        