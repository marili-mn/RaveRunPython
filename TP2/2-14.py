def es_bisiesto():
    # Solicitar al usuario que ingrese un año
    año = int(input("Por favor, ingresa un año: "))

    # Verificar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("{} es bisiesto.".format(año))
    else:
        print("{} no es bisiesto.".format(año))

# Llamamos a la función para ejecutar el programa
es_bisiesto()
