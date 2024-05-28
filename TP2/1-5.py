def calculate_average(number1, number2, number3):
    """
    Calcula el promedio de tres números.

    Parámetros:
    number1 (float): El primer número.
    number2 (float): El segundo número.
    number3 (float): El tercer número.

    Retorna:
    float: El promedio de los tres números.
    """
    average = (number1 + number2 + number3) / 3
    return average

# Ejemplo de uso
number1 = float(input("Ingresa el primer número: "))
number2 = float(input("Ingresa el segundo número: "))
number3 = float(input("Ingresa el tercer número: "))

average = calculate_average(number1, number2, number3)
print(f"El promedio de los tres números es: {average}")
