def show_word_10_times(word):
    """
    Muestra una palabra por pantalla 10 veces.

    Parámetros:
    palabra (str): La palabra a mostrar.
    """
    for _ in range(10):
        print(word)

# Pedir al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Mostrar la palabra por pantalla 10 veces
show_word_10_times(palabra)
