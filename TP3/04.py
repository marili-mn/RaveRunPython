# Lista de países predefinida
countries = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

# a. Imprimir la cantidad de elementos que tiene la lista
print("Cantidad de elementos en la lista:", len(countries))

# b. Imprimir el primer y último elemento
print("Primer elemento:", countries[0])
print("Último elemento:", countries[-1])

# c. Imprimir el resto
print("El resto de los elementos:", countries[1:-1])

# d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista
country_to_find = input("Ingrese un país para buscar en la lista: ").capitalize()
if country_to_find in countries:
    print(f"El país '{country_to_find}' se encuentra en el índice:", countries.index(country_to_find))
else:
    print(f"El país '{country_to_find}' no se encuentra en la lista.")

# e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista
position_to_remove = int(input(f"Ingrese un número entre 1 y {len(countries)} para quitar el elemento correspondiente: "))

if 1 <= position_to_remove <= len(countries):
    removed_country = countries.pop(position_to_remove - 1)  # Ajustar el número para obtener el índice correcto en la lista
    print(f"El país '{removed_country}' ha sido eliminado de la lista.")
else:
    print("Número fuera de rango. No se eliminó ningún elemento.")

# f. Imprimir la lista en orden inverso
print("Lista en orden inverso:", list(reversed(countries)))

# g. Vaciar la lista
countries.clear()
print("Lista vacía:", countries)
