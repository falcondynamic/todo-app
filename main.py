# # TODO App
import json
import psycopg2

from root_list import crud_liste

# # Database connection
db_params = {
    'host': 'db.lfdyjztnhwlpmzalhkso.supabase.co',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'Ei0AbJfvrkiIoNrP'
}
connection = psycopg2.connect(**db_params)
# Create a cursor
cursor = connection.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM books WHERE publication_year='1998';")
rows = cursor.fetchall()
print(rows)

liste = []  # [{"urun":"ekmek", adet:5, user_id:1},{"urun":"su", adet:5, user_id:1}, {"urun":"seker", adet:5, user_id:1}]

try:
    fr = open("user.txt", "r")
    users = json.loads(fr.read())  # [{id:1, username:"codingbook", password:"123"}]
    print(users)
    fr.close()
except:
    users = []

liste_komutlari = ["add", "delete", "update"]
user_komutlari = ["signup", "login", "signout"]
login = {}


def crud_user(girdiler):
    # signup login signout
    if girdiler[0] == "signup":
        _user = {"id": len(users) + 1, "username": girdiler[1], "password": girdiler[2]}
        users.append(_user)
        login.update(_user)


def kapat():
    fw = open("user.txt", "w+")
    fw.write(json.dumps(users))
    fw.close()
    # Close the cursor and connection
    cursor.close()
    connection.close()


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
        crud_user(girdiler)
    elif girdiler[0] in liste_komutlari:
        liste = crud_liste(girdiler, login, liste)

    print(liste)
