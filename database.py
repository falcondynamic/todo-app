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
tum_todo_list = "SELECT * FROM books WHERE author_id={};"
def tum_liste(user_id):
    cursor.execute(tum_todo_list.format(user_id))
    rows = cursor.fetchall()
    return rows

def close_db():
    cursor.close()
    connection.close()