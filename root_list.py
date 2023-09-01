from utils import find_index

def crud_liste(girdiler, login, liste):
    try:
        if girdiler[0] == "add":
            print(login)
            liste.append({"urun": girdiler[1], "adet": int(girdiler[2]), "user_id": login["id"]})
        elif girdiler[0] == "delete":
            index = find_index(liste, girdiler[1])
            if index != -1:
                liste.pop(index)
        elif girdiler[0] == "update":
            index = find_index(liste, girdiler[1])
            if index != -1:
                liste[index]["adet"] = girdiler[2]
    except:
        print("hatali komut formati")
    return liste

