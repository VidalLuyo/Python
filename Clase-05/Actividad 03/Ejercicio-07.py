#Menú interactivo

def menu():
    while True:
        print("1. Hay sopa 1")
        print("2. Hay sopa 2")
        print("3. Hay sopa 3")

        option = input( "Elija una opcion: ")

        if option == "1":
            print("Elegiste la sopa 1")
        elif option == "2":
            print("Elegiste la sopa 2")
        elif option == "3":
            print("Saliendo del menú... ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
    
menu()