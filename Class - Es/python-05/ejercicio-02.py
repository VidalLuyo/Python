#Insertar datos a la bd

import sqlite3

#Coneccion a la bd
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

#Insertar registros
cursor.executemany('INSERT INTO student (Nombre) VALUES(?)',
                   [("Vidal 3 ",), ("Melanie 4",),("José 5",)])

conn.commit()
conn.close()

print("Daros insertados correctamente.")