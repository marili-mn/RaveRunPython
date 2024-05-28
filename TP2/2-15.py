def validar_letra():
    # Solicitar al usuario que ingrese una letra
    letra = input("Por favor, ingresa una letra: ")

    # Validar si la entrada es un solo carácter
    if len(letra) != 1:
        print("Error: Debes ingresar solo una letra.")
    else:
        # Verificar si la letra ingresada es una vocal
        if letra.lower() in "aeiou":
            print("La letra '{}' es una vocal.".format(letra))
        else:
            print("La letra '{}' no es una vocal.".format(letra))

# Llamamos a la función para ejecutar el programa
validar_letra()
