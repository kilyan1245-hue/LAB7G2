def calcular_area_cuadrado(lado):
    return lado * lado


def calcular_area_rectangulo(base, altura):
    return base * altura


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


print("CALCULO DE AREAS")

area_cuadrado = calcular_area_cuadrado(5)
print("Area del cuadrado:", area_cuadrado)

area_rectangulo = calcular_area_rectangulo(8, 4)
print("Area del rectangulo:", area_rectangulo)

area_triangulo = calcular_area_triangulo(10, 6)
print("Area del triangulo:", area_triangulo)