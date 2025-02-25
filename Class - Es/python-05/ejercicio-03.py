#Leer datos de la bd

import sqlite3

#Coneccion a la bd
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

#Leer datos
cursor.execute("SELECT * FROM student")
registros = cursor.fetchall()

#Mostrar en consola
for i in registros:
    print(i)
    
conn.close()