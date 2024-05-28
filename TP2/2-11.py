def contar_vocales_en_frase():
    # Solicitar al usuario que ingrese una frase
    frase = input("Por favor, ingresa una frase: ")

    # Inicializar un contador para las vocales
    contador_vocales = 0

    # Recorrer cada carácter de la frase
    for caracter in frase:
        # Verificar si el carácter es una vocal (mayúscula o minúscula)
        if caracter.lower() in "aeiou":
            contador_vocales += 1

    # Imprimir la cantidad de vocales encontradas en la frase
    print("La cantidad de vocales en la frase es:", contador_vocales)

# Llamamos a la función para ejecutar el programa
contar_vocales_en_frase()
