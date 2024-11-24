import pandas as pd

class Agenda:
    def __init__(self):
        self.contactos = pd.DataFrame(columns=['nombre', 'telf', 'email'])

    def menu(self):
        print()
        menu = [
            ['Agenda Personal'],
            ['1. Añadir Contacto'],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Guardar contactos'],
            ['6. Cargar contactos'],
            ['7. Cerrar agenda']
        ]

        for item in menu:
            print(item[0])

        opcion = int(input("Introduzca la opción deseada: "))
        if opcion == 1:
            self.anadir()
        elif opcion == 2:
            self.lista()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            self.editar()
        elif opcion == 5:
            self.guardar_contactos()
        elif opcion == 6:
            self.cargar_contactos()
        elif opcion == 7:
            print("Saliendo de la agenda ...")
            exit()

        self.menu()

    def anadir(self):
        print("---------------------")
        print("Añadir nuevo contacto")
        print("---------------------")
        nom = input("Introduzca el nombre: ")
        telf = int(input("Introduzca el teléfono: "))
        email = input("Introduzca el email: ")
        nuevo_contacto = {'nombre': nom, 'telf': telf, 'email': email}
        self.contactos = self.contactos.append(nuevo_contacto, ignore_index=True)

    def lista(self):
        print("------------------")
        print("Lista de contactos")
        print("------------------")
        if self.contactos.empty:
            print("No hay ningún contacto en la agenda")
        else:
            print(self.contactos)

    def buscar(self):
        print("---------------------")
        print("Buscador de contactos")
        print("---------------------")
        nom = input("Introduzca el nombre del contacto: ")
        resultado = self.contactos[self.contactos['nombre'] == nom]
        if not resultado.empty:
            print("Datos del contacto:")
            print(resultado)
            return resultado.index[0]
        else:
            print("No se encontró ningún contacto con ese nombre.")
            return None

    def editar(self):
        print("---------------")
        print("Editar contacto")
        print("---------------")
        data = self.buscar()
        if data is not None:
            while True:
                print("Selecciona qué quieres editar:")
                print("1. Nombre")
                print("2. Teléfono")
                print("3. E-mail")
                print("4. Volver")
                option = int(input("Introduzca la opción deseada: "))
                if option == 1:
                    nom = input("Introduzca el nuevo nombre: ")
                    self.contactos.at[data, 'nombre'] = nom
                elif option == 2:
                    telf = input("Introduzca el nuevo teléfono: ")
                    self.contactos.at[data, 'telf'] = telf
                elif option == 3:
                    email = input("Introduzca el nuevo email: ")
                    self.contactos.at[data, 'email'] = email
                elif option == 4:
                    break

    def guardar_contactos(self):
        print("---------------")
        print("Guardar contactos")
        print("---------------")
        archivo = input("Introduzca el nombre del archivo (ejemplo: agenda.csv): ")
        self.contactos.to_csv(archivo, index=False)
        print("Contactos guardados en", archivo)

    def cargar_contactos(self):
        print("---------------")
        print("Cargar contactos")
        print("---------------")
        archivo = input("Introduzca el nombre del archivo (ejemplo: agenda.csv): ")
        try:
            self.contactos = pd.read_csv(archivo)
            print("Contactos cargados desde", archivo)
        except FileNotFoundError:
            print("El archivo no existe.")

agenda = Agenda()
agenda.menu()
