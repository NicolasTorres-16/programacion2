def obtener_agenda():
    contactos = {}
    while True:
        nombre = input(
            "Ingrese un nombre o déjelo vacío para terminar de agregar: ")
        if nombre == "":
            break
        if nombre in contactos:
            print("Nombre ya existente")
        else:
            telefono = input(f"Ingrese el teléfono de {nombre}: ")
            contactos[nombre] = telefono
    return contactos


def imprimir_agenda():
    contactos = obtener_agenda()
    for nombre in contactos:
        telefono = contactos[nombre]
        print(f"{nombre} tiene el teléfono {telefono}")


def main():
    imprimir_agenda()


main()
