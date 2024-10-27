class contacto:
    def __init__(self, nombre, telefono):

        self.nombre = nombre
        self.telefono = telefono


def mostrar_menu():
    print("Gestion de contactos")
    print("1. Agregar contacto")
    print("2. mostar contactos")
    print("3. buscar contacto")
    print("4. eliminar contacto")
    print("5. salir")

contactos = []


while True:
    mostrar_menu()
    opcion = input("elige una opcion")

    if opcion == "5":
        print("saliendo del programa")
        break

    if opcion == "1":
        nombre = input("ingresa el nombre: ")
        telefono = input("ingresa el telefono: ")
        contacto = contacto(nombre, telefono)
        contactos.append(contacto)
        print("contacto agregado")
    elif opcion == "2":
        for c in contactos:
            print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
    elif opcion =="3":
        nombre = input("ingresa el nombre a buscar")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
                encontrado = True
                break
        if not encontrado:
            print("contacto no encontrado")
    elif opcion == "4":
         nombre = input("ingresa el nombre a eliminar")
         for c in contactos:
             if c.nombre == nombre:
                 contactos.remove(c)
                 print("contacto eliminado")
                 break
    else:
        print("opcion no valida")         
