class Zoologico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.zonas = []
        self.instalaciones = []
        self.animales = []
        self.trabajadores = []
        self.asignaciones = []

    def introducir_zona(self, zona):
        self.zonas.append(zona)

    def introducir_instalacion(self, instalacion):
        self.instalaciones.append(instalacion)

    def introducir_animal(self, animal):
        self.animales.append(animal)

    def introducir_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def introducir_asignacion(self, asignacion):
        self.asignaciones.append(asignacion)

    def listado_instalaciones(self):
        print("Listado de Instalaciones:")
        for instalacion in self.instalaciones:
            print(instalacion)

    def listado_animales(self):
        print("Listado de Animales:")
        for animal in self.animales:
            print(animal)

    def listado_zonas_trabajador(self, dni):
        print(f"Zonas asignadas al trabajador con DNI {dni}:")
        for asignacion in self.asignaciones:
            if asignacion.trabajador.dni == dni:
                print(asignacion)


class Zona:
    def __init__(self, codigo, nombre, capacidad):
        self.codigo = codigo
        self.nombre = nombre
        self.capacidad = capacidad

    def __str__(self):
        return f"Zona: {self.codigo}, {self.nombre}, Capacidad: {self.capacidad}"


class Instalacion:
    def __init__(self, codigo, descripcion, anio, zona):
        self.codigo = codigo
        self.descripcion = descripcion
        self.anio = anio
        self.zona = zona

    def __str__(self):
        return f"Instalación {self.codigo}: {self.descripcion}, Año: {self.anio}, Zona: {self.zona.nombre}"


class Animal:
    def __init__(self, codigo, nombre, anio, especie, instalacion):
        self.codigo = codigo
        self.nombre = nombre
        self.anio = anio
        self.especie = especie
        self.instalacion = instalacion

    def __str__(self):
        return f"Animal {self.codigo}: {self.nombre}, Especie: {self.especie}, Instalación: {self.instalacion.codigo}"


class Trabajador:
    def __init__(self, dni, nombre, apellido1, apellido2, puesto):
        self.dni = dni
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.puesto = puesto

    def __str__(self):
        return f"Trabajador {self.dni}: {self.nombre} {self.apellido1} {self.apellido2}, Puesto: {self.puesto}"


class Asignacion:
    def __init__(self, trabajador, zona, horario):
        self.trabajador = trabajador
        self.zona = zona
        self.horario = horario

    def __str__(self):
        return f"{self.trabajador.nombre} asignado a {self.zona.nombre}, Horario: {self.horario}"


def main():
    zoo = Zoologico("Mi Zoo")

    # Crear Zonas
    zona1 = Zona("01FEL", "Felinos", 400)
    zona2 = Zona("02PRI", "Primates", 300)
    zona3 = Zona("03PMA", "Pequeños mamíferos", 230)
    zona4 = Zona("04RES", "Restaurante", 400)

    zoo.introducir_zona(zona1)
    zoo.introducir_zona(zona2)
    zoo.introducir_zona(zona3)
    zoo.introducir_zona(zona4)

    # Crear Instalaciones
    insta1 = Instalacion(143, "Jaula amplia con dos árboles en el centro", 2012, zona1)
    insta2 = Instalacion(144, "Jaula alta con barrotes separados", 2014, zona1)
    insta3 = Instalacion(150, "Jaula con distintos niveles y zona de juegos", 2013, zona2)

    zoo.introducir_instalacion(insta1)
    zoo.introducir_instalacion(insta2)
    zoo.introducir_instalacion(insta3)

    # Crear Animales
    ani1 = Animal("SI-01", "Simba", 2010, "león", insta1)
    ani2 = Animal("NA-12", "Nala", 2011, "león", insta1)
    ani3 = Animal("SA-11", "Bruto", 2001, "gorila", insta3)

    zoo.introducir_animal(ani1)
    zoo.introducir_animal(ani2)
    zoo.introducir_animal(ani3)

    # Crear Trabajadores
    tra1 = Trabajador("11223344H", "Ana", "García", "Rojas", "Veterinario")
    zoo.introducir_trabajador(tra1)

    # Crear Asignaciones
    asig1 = Asignacion(tra1, zona1, "Lunes y Miércoles de 9 a 11")
    asig2 = Asignacion(tra1, zona2, "Jueves por la tarde")
    asig3 = Asignacion(tra1, zona3, "Sábado por la mañana")

    zoo.introducir_asignacion(asig1)
    zoo.introducir_asignacion(asig2)
    zoo.introducir_asignacion(asig3)

    # Listados
    zoo.listado_instalaciones()
    print("\n")
    zoo.listado_animales()
    print("\n")
    zoo.listado_zonas_trabajador("11223344H")


if __name__ == "__main__":
    main()
