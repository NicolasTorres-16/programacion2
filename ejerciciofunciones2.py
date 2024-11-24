import math
def area_perimetro_circulo(radio):
    perimetro = 2.0*math.pi*radio
    area = math.pi*radio*radio
    return perimetro, area
rad = float(input("ingrese el radio del circulo "))
radio = perimetro, area = area_perimetro_circulo(rad)
print("perimetro: ", perimetro, "area: ", area)
