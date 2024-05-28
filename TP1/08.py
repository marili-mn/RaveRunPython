def calculate_triangle_area(base, height):
    area = (base * height) / 2
    return area

def main():
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    height = float(input("Ingrese la altura del triángulo: "))

    total_area = calculate_triangle_area(base, height)

    print(f"El área total del triángulo es: {total_area}")
    
main()