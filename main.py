# # TODO App
import database as db
from root_list import crud_liste
from root_user import crud_user
from utils import read_users_file

# [{"urun":"ekmek", adet:5, user_id:1},{"urun":"su", adet:5, user_id:1}, {"urun":"seker", adet:5, user_id:1}]
liste = db.all_shopping_list(1)
print(liste)


liste_komutlari = ["add", "delete", "update"]
user_komutlari = ["signup", "login", "signout"]
login = {}


def kapat():
    # Close the cursor and connection
    db.close_db()


while True:
    if "id" in login.keys():
        girdi = input(f"{login['username']}: ")  # "add ekmek 5" "delete ekmek"
    else:
        girdi = input("Lutfen kayit veya giris yapiniz: ")  # "add ekmek 5" "delete ekmek"
    if girdi == "q":
        kapat()
        break
    girdiler = girdi.split()

    if girdiler[0] in user_komutlari:
        crud_user(girdiler, login )
    elif girdiler[0] in liste_komutlari:
        liste = crud_liste(girdiler, login)

    print(liste)
