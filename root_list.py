from utils import find_index
import database as db

print("db", db.all_shopping_list(1))
def crud_liste(girdiler, login):
    # liste = db.all_shopping_list(login["id"])
    try:
        if girdiler[0] == "add":
            insert_query = 'INSERT INTO "shopping" (product, quantity, user_id) VALUES ' + "('{}', '{}', '{}');".format(girdiler[1],
                                                                            girdiler[2], login["id"])
            db.cursor.execute(insert_query)
            db.connection.commit()

            # liste.append({"urun": girdiler[1], "adet": int(girdiler[2]), "user_id": login["id"]})
        elif girdiler[0] == "delete":
            delete_query = 'DELETE FROM "shopping" WHERE '+"product='{}' AND user_id='{}';".format(girdiler[1], login["id"])
            db.cursor.execute(delete_query)
            db.connection.commit()
            # index = find_index(liste, girdiler[1])
            # if index != -1:
            #     liste.pop(index)
        elif girdiler[0] == "update":
            update_query = 'UPDATE "shopping" SET '+"quantity='{}' WHERE user_id='{}' AND product='{}';".format(girdiler[2], login["id"], girdiler[1])
            db.cursor.execute(update_query)
            db.connection.commit()
            # index = find_index(liste, girdiler[1])
            # if index != -1:
            #     liste[index]["adet"] = girdiler[2]
    except:
        print("hatali komut formati")
    return db.all_shopping_list(login["id"])

