# # TODO App
from root_list import crud_liste
from root_user import crud_user
import dbsqlite3 as db

liste_komutlari = ["add", "delete", "update", "print"]
user_komutlari = ["signup", "login", "signout"]

login = {}

def kapat():
    # Close the db cursor and connection
    db.close()


while True:
    if "id" in login.keys():
        girdi = input(f"{login['username']}: ")  # "add ekmek 5" "delete ekmek"
    else:
        girdi = input("q for quit!\nsignup/login for start: ")  # "add ekmek 5" "delete ekmek"
    if girdi == "q":
        kapat()
        break
    girdiler = girdi.split()

    if girdiler[0] in user_komutlari:
        crud_user(girdiler, login)
    elif girdiler[0] in liste_komutlari:
        crud_liste(girdiler, login)

