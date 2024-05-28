def display_numeric_info():
    # Solicitar al usuario que ingrese un número entero positivo
    numero = int(input("Por favor, ingresa un número entero positivo: "))

    # a. Imprimir todos los números impares desde 1 hasta ese número separados por comas
    print("a. Todos los números impares desde 1 hasta {}:".format(numero))
    impares = [str(x) for x in range(1, numero + 1, 2)]
    print(", ".join(impares))

    # b. Imprimir la cuenta atrás desde ese número hasta cero separados por comas
    print("b. La cuenta atrás desde {} hasta 0:".format(numero))
    cuenta_atras = [str(x) for x in range(numero, -1, -1)]
    print(", ".join(cuenta_atras))

    # c. Verificar si el número es primo
    es_primo = True
    if numero <= 1:
        es_primo = False
    else:
        for i in range(2, numero):
            if (numero % i) == 0:
                es_primo = False
                break
    if es_primo:
        print("c. {} es un número primo.".format(numero))
    else:
        print("c. {} no es un número primo.".format(numero))

    # d. Calcular el factorial del número
    factorial = 1
    if numero < 0:
        print("No se puede calcular el factorial de un número negativo.")
    elif numero == 0:
        print("d. El factorial de 0 es 1.")
    else:
        for i in range(1, numero + 1):
            factorial *= i
        print("d. El factorial de {} es {}.".format(numero, factorial))

# Llamamos a la función para ejecutar el programa
display_numeric_info()
