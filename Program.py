import pyhdb
connection = pyhdb.connect(
    host="10.200",
    port=30015,
    user="user",
    password="secret"
)
cursor = connection.cursor()
cursor.execute("SELECT 'Hello Python World' FROM DUMMY")
cursor.fetchone()
connection.close()

