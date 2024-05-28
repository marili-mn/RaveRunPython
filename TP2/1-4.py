def calculate_triangle_area(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    area = (base * altura) / 2
    return area

# Ejemplo de uso
base = float(input("Ingrese la longitud de la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area_triangulo = calculate_triangle_area(base, altura)
print(f"El área del triángulo es: {area_triangulo}")
