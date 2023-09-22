import dbsqlite3 as db

def crud_liste(girdiler, login):
    try:
        if girdiler[0] == "add":
            insert_query = "INSERT INTO shopping (product, quantity, user_id) VALUES (?, ?, ?)"
            db.cursor.execute(insert_query, (girdiler[1], girdiler[2], login["id"]))
            db.connection.commit()

        elif girdiler[0] == "delete":
            delete_query = "DELETE FROM shopping WHERE product=? AND user_id=?"
            db.cursor.execute(delete_query,(girdiler[1], login["id"]))
            db.connection.commit()

        elif girdiler[0] == "update":
            update_query = "UPDATE shopping SET quantity=? WHERE user_id=? AND product=?"
            db.cursor.execute(update_query,(girdiler[2], login["id"], girdiler[1]))
            db.connection.commit()

        elif girdiler[0] == "print":
            update_query = "SELECT product, quantity FROM shopping WHERE user_id=?"
            rows = db.cursor.execute(update_query,(login["id"],)).fetchall()
            print(rows)

    except:
        print("hatali komut")


