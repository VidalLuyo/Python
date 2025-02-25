#Eliminar datos de la bd

import sqlite3

#Coneccion a la bd
conn = sqlite3.connect("student.db")
cursor = conn.cursor()


# Eliminar tabla
cursor.execute("DELETE FROM student WHERE id = ?", (6,))

conn.commit()
conn.close()

print("Un registro se elimino")