def determinar_grupo():
    # Solicitar al usuario que ingrese su nombre y sexo
    nombre = input("Por favor, ingresa tu nombre: ")
    sexo = input("Por favor, ingresa tu sexo (masculino/femenino): ")

    # Convertir el nombre a minúsculas para comparación
    nombre = nombre.lower()

    # Determinar el grupo al que pertenece el alumno
    if (sexo.lower() == "femenino" and nombre < "m") or (sexo.lower() == "masculino" and nombre >= "n"):
        grupo = "A"
    else:
        grupo = "B"

    # Mostrar por pantalla el grupo correspondiente
    print("Tu grupo es el grupo", grupo)

# Llamamos a la función para ejecutar el programa
determinar_grupo()
