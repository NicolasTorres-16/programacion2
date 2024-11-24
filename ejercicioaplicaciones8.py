def obtener_agenda():
    """Función para agregar contactos a la agenda."""
    agenda = {}
    while True:
        print("\n=== AGENDA TELEFÓNICA ===")
        print("1. Agregar contacto")
        print("2. Editar contacto")
        print("3. Eliminar contacto")
        print("4. Ver todos los contactos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre y apellidos: ").strip()
            if nombre in agenda:
                print("Este contacto ya existe.")
            else:
                telefono = input("Ingrese número de teléfono: ").strip()
                correo = input("Ingrese correo electrónico: ").strip()
                direccion = input("Ingrese dirección de residencia: ").strip()
                cumpleaños = input("Ingrese fecha de cumpleaños (DD/MM/AAAA): ").strip()
                agenda[nombre] = {
                    "Teléfono": telefono,
                    "Correo": correo,
                    "Dirección": direccion,
                    "Cumpleaños": cumpleaños,
                }
                print(f"Contacto {nombre} agregado exitosamente.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a editar: ").strip()
            if nombre in agenda:
                print(f"Editando contacto: {nombre}")
                telefono = input(f"Nuevo número de teléfono ({agenda[nombre]['Teléfono']}): ").strip()
                correo = input(f"Nuevo correo electrónico ({agenda[nombre]['Correo']}): ").strip()
                direccion = input(f"Nueva dirección ({agenda[nombre]['Dirección']}): ").strip()
                cumpleaños = input(f"Nuevo cumpleaños ({agenda[nombre]['Cumpleaños']}): ").strip()
                agenda[nombre] = {
                    "Teléfono": telefono or agenda[nombre]['Teléfono'],
                    "Correo": correo or agenda[nombre]['Correo'],
                    "Dirección": direccion or agenda[nombre]['Dirección'],
                    "Cumpleaños": cumpleaños or agenda[nombre]['Cumpleaños'],
                }
                print(f"Contacto {nombre} actualizado.")
            else:
                print("El contacto no existe.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print("El contacto no existe.")

        elif opcion == "4":
            if agenda:
                print("\n=== CONTACTOS ===")
                for nombre, datos in agenda.items():
                    print(f"\nNombre: {nombre}")
                    for key, value in datos.items():
                        print(f"{key}: {value}")
                print(f"\nTotal de contactos: {len(agenda)}")
            else:
                print("La agenda está vacía.")

        elif opcion == "5":
            print("Saliendo de la agenda.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


def main():
    obtener_agenda()

if __name__ == "__main__":
    main()
