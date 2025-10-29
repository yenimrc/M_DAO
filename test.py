import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="usuarios"
)

cursor = conn.cursor()
cursor.execute("SELECT VERSION();")
version = cursor.fetchone()
print("Versión de MySQL:", version[0])

cursor.close()
conn.close()

