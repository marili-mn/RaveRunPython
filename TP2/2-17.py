def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_numeros_primos():
    contador_primos = 0
    print("Números primos entre 0 y 100:")
    for num in range(101):
        if es_primo(num):
            print(num, end=" ")
            contador_primos += 1
    print("\nTotal de números primos entre 0 y 100:", contador_primos)

# Llamamos a la función para ejecutar el programa
mostrar_numeros_primos()
