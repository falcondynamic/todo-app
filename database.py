import psycopg2

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
list_by_user = "SELECT product, quantity FROM shopping WHERE user_id={};"
add_list = "INSERT INTO shopping (product, quantity, user_id) VALUES ({}, {}, {});"
#cur.execute('INSERT INTO %s (day, elapsed_time, net_time, length, average_speed, geometry) VALUES (%s, %s, %s, %s, %s, %s)', (escaped_name, day, time_length, time_length_net, length_km, avg_speed, myLine_ppy))


def all_shopping_list(user_id):
    cursor.execute(list_by_user.format(user_id))
    rows = cursor.fetchall()
    return rows

def add_shopping_list(p, q, user_id):
    cursor.execute((add_list.format(p, q, user_id)))
    rows = cursor.fetchall()
    return rows
def close_db():
    cursor.close()
    connection.close()