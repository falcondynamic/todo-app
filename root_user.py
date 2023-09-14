from utils import write_users_file
import database as db

# "[{id:1, username:"codingbook", password:"123"}]"

def crud_user(user_inputs, loggedin_user): # ["signup", "username", "password"]
    # signup login signout
    if user_inputs[0] == "signup":
        # users.append(_user)
        # write_users_file(users)
        insert_query = 'INSERT INTO "user" (username, password) VALUES '+"('{}', '{}');".format(user_inputs[1], user_inputs[2])
        db.cursor.execute(insert_query)
        db.connection.commit()

        select_query = 'SELECT "id", "username", "password" FROM "user" WHERE ' + "username='{}' AND password='{}';".format(user_inputs[1], user_inputs[2])
        db.cursor.execute(select_query)
        db_user = db.cursor.fetchone()
        _user = {"id":db_user[0], "username": db_user[1], "password": db_user[2]}

        loggedin_user.update(_user)
    elif user_inputs[0] == "login" and len(loggedin_user.keys()) == 0:
        select_query = 'SELECT "id", "username" FROM "user" WHERE ' + "username='{}' AND password='{}';".format(user_inputs[1], user_inputs[2])
        db.cursor.execute(select_query)
        user = db.cursor.fetchone()
        print(user)
        if user == None:
            print('Lutfen username password bilgisini kontrol ediniz')
        else:
            loggedin_user.update({"id": user[0], "username": user[1]})

        # for user in users:
        #     if user["username"] == user_inputs[1] and user["password"] == user_inputs[2]:
        #         loggedin_user.update(user)
        #         break
    elif user_inputs[0] == "signout" and len(loggedin_user.keys()) != 0:
        loggedin_user.clear()
        print(loggedin_user)
