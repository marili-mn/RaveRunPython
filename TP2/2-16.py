def imprimir_patron():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()

# Llamamos a la función para ejecutar el programa
imprimir_patron()
