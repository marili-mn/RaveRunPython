def mostrar_menor():
    # Solicitar al usuario que ingrese dos números
    number1 = float(input("Ingresa el primer número: "))
    number2 = float(input("Ingresa el segundo número: "))

    # Verificar cuál número es menor o si son iguales
    if number1 < number2:
        print("El primer número ({}) es menor que el segundo número ({}).".format(number1, number2))
    elif number1 > number2:
        print("El segundo número ({}) es menor que el primer número ({}).".format(number2, number1))
    else:
        print("Ambos números son iguales.")

# Llamamos a la función para ejecutar el programa
mostrar_menor()
