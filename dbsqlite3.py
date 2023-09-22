import sqlite3

connection = sqlite3.connect("todo.db")
cursor = connection.cursor()

def create_tables():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS shopping (id INTEGER PRIMARY KEY,product VARCHAR(255) NOT NULL,quantity INT NOT NULL,user_id INT,FOREIGN KEY (user_id) REFERENCES user(id))")


create_tables()

def close():
    cursor.close()
    connection.close()


query_shopping_by_user = "SELECT product, quantity FROM shopping WHERE user_id=?"
