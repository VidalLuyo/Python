import os

#Nombre del archivo

db = "student.db"

if os.path.exists(db):
    os.remove(db)
    print(f"La bd {db} ha sido eliminada")
else:
    print("No existe la bd")