def imprimir_mensaje_segun_dia():
    # Pedir al usuario que ingrese un día de la semana
    dia = input("Por favor, ingresa un día de la semana: ")

    # Convertir el día ingresado a minúsculas para comparación
    dia = dia.lower()

    # Imprimir un mensaje diferente según el día ingresado
    if dia == "lunes":
        print("Es lunes. ¡Ánimo, comienza la semana!")
    elif dia == "viernes":
        print("Es viernes. ¡Al fin, llegó el fin de semana!")
    elif dia == "sabado" or dia == "domingo":
        print("Es sábado o domingo. ¡Disfruta del fin de semana!")
    else:
        print("Es un día de la semana diferente. ¡Sigue adelante!")

# Llamamos a la función para ejecutar el programa
imprimir_mensaje_segun_dia()
