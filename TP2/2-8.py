def is_adult():
    # Solicitar la edad al usuario
    edad = int(input("Por favor, ingresa tu edad: "))

    # Verificar si es mayor de edad
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

# Llamamos a la función para ejecutar el programa
is_adult()
