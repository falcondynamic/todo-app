from utils import write_users_file

def crud_user(user_inputs, loggedin_user, users): # ["signup", "username", "password"]
    # signup login signout
    if user_inputs[0] == "signup":
        _user = {"id": len(users) + 1, "username": user_inputs[1], "password": user_inputs[2]}
        users.append(_user)
        write_users_file(users)
        loggedin_user.update(_user)
    elif user_inputs[0] == "login" and len(loggedin_user.keys()) == 0:
        for user in users:
            if user["username"] == user_inputs[1] and user["password"] == user_inputs[2]:
                loggedin_user.update(user)
                break
    elif user_inputs[0] == "signout" and len(loggedin_user.keys()) != 0:
        loggedin_user.clear()
        print(loggedin_user)
