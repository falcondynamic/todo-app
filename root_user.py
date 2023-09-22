import dbsqlite3 as db

def crud_user(user_inputs, loggedin_user): # ["signup", "username", "password"]
    if user_inputs[0] == "signup":
        insert_query = 'INSERT INTO user (username, password)  VALUES (?, ?)'
        db.cursor.execute(insert_query, (user_inputs[1], user_inputs[2]))
        db.connection.commit()

        query_select = "SELECT * FROM user WHERE username=? AND password=?"
        db_user = db.cursor.execute(query_select, (user_inputs[1], user_inputs[2])).fetchone()
        _user = {"id": db_user[0], "username": db_user[1], "password": db_user[2]}
        loggedin_user.update(_user)

    elif user_inputs[0] == "login" and len(loggedin_user.keys()) == 0:
        query_select = "SELECT id, username FROM user WHERE username=? AND password=?"
        user = db.cursor.execute(query_select, (user_inputs[1], user_inputs[2])).fetchone()

        if user == None:
            print('Lutfen username/password kontrol ediniz')
        else:
            loggedin_user.update({"id": user[0], "username": user[1]})

    elif user_inputs[0] == "signout" and len(loggedin_user.keys()) != 0:
        loggedin_user.clear()

