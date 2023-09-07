# # TODO App
from root_list import crud_liste
from root_user import crud_user
from utils import read_users_file, write_users_file
from database import close_db

# [{"urun":"ekmek", adet:5, user_id:1},{"urun":"su", adet:5, user_id:1}, {"urun":"seker", adet:5, user_id:1}]
liste = []

users = read_users_file()  # "[{id:1, username:"codingbook", password:"123"}]"
print(users)

liste_komutlari = ["add", "delete", "update"]
user_komutlari = ["signup", "login", "signout"]
login = {}




def kapat():
    # Close the cursor and connection
    close_db()


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
        crud_user(girdiler, login, users )
    elif girdiler[0] in liste_komutlari:
        liste = crud_liste(girdiler, login, liste)

    print(liste)
