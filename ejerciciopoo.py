class Vehiculo:
    def __init__(self, marca, modelo, año, tipo_pintura, precio):
        """
        Clase base para vehículos en el concesionario.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo_pintura = tipo_pintura
        self.precio = precio

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}) - Pintura: {self.tipo_pintura}, Precio: ${self.precio:,.2f}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_pintura, precio, puertas):
        super().__init__(marca, modelo, año, tipo_pintura, precio)
        self.puertas = puertas

    def __str__(self):
        return super().__str__() + f", Puertas: {self.puertas}"


class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_pintura, precio, capacidad_carga):
        super().__init__(marca, modelo, año, tipo_pintura, precio)
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return super().__str__() + f", Capacidad de carga: {self.capacidad_carga} kg"


class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_pintura, precio, capacidad_toneladas):
        super().__init__(marca, modelo, año, tipo_pintura, precio)
        self.capacidad_toneladas = capacidad_toneladas

    def __str__(self):
        return super().__str__() + f", Capacidad: {self.capacidad_toneladas} toneladas"


class Tractocamion(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_pintura, precio, potencia_hp):
        super().__init__(marca, modelo, año, tipo_pintura, precio)
        self.potencia_hp = potencia_hp

    def __str__(self):
        return super().__str__() + f", Potencia: {self.potencia_hp} HP"


class Concesionario:
    def __init__(self, nombre):
        """
        Clase para manejar un concesionario de vehículos.
        """
        self.nombre = nombre
        self.inventario = []

    def agregar_vehiculo(self, vehiculo, cantidad):
        """
        Agrega un vehículo al inventario.
        """
        self.inventario.append({"vehiculo": vehiculo, "cantidad": cantidad})

    def mostrar_inventario(self):
        """
        Muestra todos los vehículos en el inventario.
        """
        print(f"Inventario del concesionario '{self.nombre}':")
        for idx, item in enumerate(self.inventario, start=1):
            vehiculo = item["vehiculo"]
            cantidad = item["cantidad"]
            print(f"{idx}. {vehiculo} - Unidades: {cantidad}")

    def buscar_por_tipo(self, tipo):
        """
        Filtra vehículos por su tipo.
        """
        print(f"\nVehículos de tipo '{tipo}' en el inventario:")
        for item in self.inventario:
            if isinstance(item["vehiculo"], tipo):
                print(f"- {item['vehiculo']} - Unidades: {item['cantidad']}")


# Ejemplo de uso
def main():
    concesionario = Concesionario("Autos del Futuro")

    # Agregar vehículos al concesionario
    auto1 = Automovil("Toyota", "Corolla", 2023, "Metálica", 25000, 4)
    auto2 = Automovil("Honda", "Civic", 2023, "Mate", 27000, 4)
    camioneta1 = Camioneta("Ford", "Ranger", 2022, "Perlada", 35000, 1000)
    camion1 = Camion("Volvo", "FH16", 2021, "Sólida", 120000, 25)
    tractocamion1 = Tractocamion("Kenworth", "W900", 2023, "Metálica", 180000, 500)

    concesionario.agregar_vehiculo(auto1, 10)
    concesionario.agregar_vehiculo(auto2, 7)
    concesionario.agregar_vehiculo(camioneta1, 5)
    concesionario.agregar_vehiculo(camion1, 2)
    concesionario.agregar_vehiculo(tractocamion1, 3)

    # Mostrar inventario
    concesionario.mostrar_inventario()

    # Buscar vehículos por tipo
    concesionario.buscar_por_tipo(Automovil)
    concesionario.buscar_por_tipo(Camioneta)


if __name__ == "__main__":
    main()
