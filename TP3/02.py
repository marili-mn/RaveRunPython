# Pedir al usuario que ingrese 5 números
numbers = []
print("Ingrese 5 números:")

# Repetir 5 veces para recoger los números del usuario
for _ in range(5):
    number = int(input("Ingrese un número: "))
    numbers.append(number)

# Ordenar los números
numbers.sort()

# Imprimir los números ordenados
print("Números ordenados de manera ascendente:")
print(numbers)