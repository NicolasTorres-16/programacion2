class EnteroARomano:
    def __init__(self, numero):
        self.numero = numero
        self.valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convertir(self):
        resultado = ""
        num = self.numero
        for valor, simbolo in self.valores:
            while num >= valor:
                resultado += simbolo
                num -= valor
        return resultado


class RomanoAEntero:
    def __init__(self, romano):
        self.romano = romano.upper()
        self.valores = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convertir(self):
        total = 0
        prev_value = 0
        for simbolo in reversed(self.romano):
            valor = self.valores.get(simbolo, 0)
            if valor < prev_value:
                total -= valor
            else:
                total += valor
            prev_value = valor
        return total


def main():
    print("Conversión de números: ")
    print("1. Convertir entero a número romano")
    print("2. Convertir número romano a entero")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        numero = int(input("Ingrese un número entero: "))
        if numero < 1 or numero > 3999:
            print("Por favor, ingrese un número entre 1 y 3999.")
        else:
            conversion = EnteroARomano(numero)
            print(f"El número {numero} en romano es: {conversion.convertir()}")
    elif opcion == '2':
        romano = input("Ingrese un número romano: ")
        conversion = RomanoAEntero(romano)
        try:
            resultado = conversion.convertir()
            print(f"El número romano {romano} equivale a: {resultado}")
        except Exception:
            print("Entrada inválida. Por favor, ingrese un número romano válido.")
    else:
        print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()


