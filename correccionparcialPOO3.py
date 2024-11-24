class Animal:
    def __init__(self, especie, edad, tamano, peso, altura, fecha_entrada, genero, tipo_comida, horarios_alimentacion, vacunas, enfermedades):
        self.especie = especie
        self.edad = edad
        self.tamano = tamano
        self.peso = peso
        self.altura = altura
        self.fecha_entrada = fecha_entrada
        self.genero = genero
        self.tipo_comida = tipo_comida
        self.horarios_alimentacion = horarios_alimentacion
        self.vacunas = vacunas
        self.enfermedades = enfermedades
    def mostrar_info(self):
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        print(f"Tamaño: {self.tamano}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"Fecha de entrada: {self.fecha_entrada}")
        print(f"Género: {self.genero}")
        print(f"Tipo de comida: {self.tipo_comida}")
        print(f"Horarios de alimentación: {self.horarios_alimentacion}")
        print(f"Vacunas: {self.vacunas}")
        print(f"Enfermedades: {self.enfermedades}")
        print("-" * 20)

class Zoologico:
    def __init__(self, nombre_zoologico):
        self.nombre_zoologico = nombre_zoologico
        self.animales = []

    def agregar_animal(self):
        if len(self.animales) < 15:
            especie = input("Ingrese la especie del animal: ")
            edad = int(input("Ingrese la edad del animal (en años): "))
            tamano = input("Ingrese el tamaño del animal: ")
            peso = float(input("Ingrese el peso del animal (en kg): "))
            altura = float(input("Ingrese la altura del animal (en metros): "))
            fecha_entrada = input("Ingrese la fecha de entrada al zoológico (YYYY-MM-DD): ")
            genero = input("Ingrese el género del animal: ")
            tipo_comida = input("Ingrese el tipo de comida que consume el animal: ")
            horarios_alimentacion = input("Ingrese los horarios de alimentación (separados por comas): ")
            vacunas = input("Ingrese las vacunas aplicadas (separadas por comas): ")
            enfermedades = input("Ingrese las enfermedades que ha tenido o tiene (separadas por comas): ")


            nuevo_animal = Animal(especie, edad, tamano, peso, altura, fecha_entrada, genero, tipo_comida, horarios_alimentacion, vacunas, enfermedades)
            self.animales.append(nuevo_animal)
            print(f"Animal {especie} agregado exitosamente.")
        else:
            print("No se pueden agregar más animales, se alcanzó el límite máximo.")

    def mostrar_animales(self):
        if len(self.animales) >= 5:
            print(f"Lista de animales en {self.nombre_zoologico}:")
            for animal in self.animales:
                animal.mostrar_info()
        else:
            print("No hay suficientes animales registrados para mostrar.")


def menu():
    print("Bienvenido al sistema de administración del Zoológico")
    nombre_zoologico = input("Ingrese el nombre del zoológico: ")
    zoologico = Zoologico(nombre_zoologico)

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar un animal")
        print("2. Mostrar todos los animales")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            zoologico.agregar_animal()
        elif opcion == "2":
            zoologico.mostrar_animales()
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


menu()
