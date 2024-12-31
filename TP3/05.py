def exercise_5():
    numbers_list = []

    def separator():
        print("********************************************************")

    def enter_numbers():
        while True:
            new_input = input("Ingrese un número para añadir a la lista, escriba 'fin' para terminar: ")
            if new_input.lower() == "fin":
                break
            else:
                try:
                    new_input = int(new_input)
                    numbers_list.append(new_input)
                except ValueError:
                    print("Por favor, ingrese solo números enteros válidos.")

    def point_a():
        separator()
        print("Punto A")
        max_num = max(numbers_list, default="La lista está vacía.")
        print("El número más alto es: " + str(max_num))

    def point_b():
        print("Punto B")
        sorted_list = sorted(set(numbers_list))
        if len(sorted_list) >= 2:
            print("El segundo número más alto es: " + str(sorted_list[-2]))
        else:
            print("No hay suficientes números para encontrar el segundo más alto.")

    def point_c():
        print("Punto C")
        min_num = min(numbers_list, default="La lista está vacía.")
        print("El número más bajo es: " + str(min_num))

    def point_d():
        print("Punto D")
        product = 1
        for num in numbers_list:
            product *= num
        print("El resultado de la multiplicación de todos los números es: " + str(product))

    def point_e():
        print("Punto E")
        even_count = sum(1 for num in numbers_list if num % 2 == 0)
        odd_count = len(numbers_list) - even_count
        print("La lista tiene " + str(even_count) + " números pares y " + str(odd_count) + " números impares.")

    def point_f():
        print("Punto F")
        unique_list = list(set(numbers_list))
        print("Lista sin valores repetidos:")
        print(unique_list)

    enter_numbers()
    point_a()
    separator()
    point_b()
    separator()
    point_c()
    separator()
    point_d()
    separator()
    point_e()
    separator()
    point_f()
    separator()

exercise_5()
