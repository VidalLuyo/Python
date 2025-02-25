#Crear base de datos
import sqlite3

#Coneccion a la bd

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

#Crear una tabla

cursor.execute('''
               
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL
)     
               
''')


# Guardan los cambios
conn.commit()
conn.close()

print("La base de datos y la tabla a sido creada")