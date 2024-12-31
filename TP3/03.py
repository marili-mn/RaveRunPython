# Lista predefinida de frutas
fruits = ["banana", "manzana", "pera"]

# Pedir al usuario que ingrese 3 frutas adicionales
user_fruits = []
print("Ingrese 3 frutas adicionales:")

# Repetir 3 veces para recoger las frutas del usuario
for _ in range(3):  # Itera 3 veces, no necesitamos el valor del índice
    fruit = input("Ingrese una fruta: ")
    user_fruits.append(fruit)
    fruits.append(fruit)  # Agregar la fruta ingresada a la lista principal

# Mostrar la lista completa de frutas
print("Lista completa de frutas:")
print(fruits)

# Mostrar solo las frutas añadidas por el usuario
print("Frutas añadidas por el usuario:")
print(user_fruits)