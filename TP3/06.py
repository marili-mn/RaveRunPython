def task_manager():
    task_list = []

    def separator():
        print("*******************************************")

    def get_number(prompt):
        return input("Ingrese un número " + prompt)

    def show_list():
        print("La lista se ha modificado: " + str(task_list))
        separator()

    def add_to_end():
        task_list.append(get_number("para agregarlo al final de la lista: "))
        show_list()

    def add_to_start():
        task_list.insert(0, get_number("para agregarlo al principio de la lista: "))
        show_list()

    def remove_from_end():
        if task_list:
            task_list.pop()
            show_list()
        else:
            print("La lista está vacía. No se puede quitar un elemento del final.")
            separator()

    def remove_from_start():
        if task_list:
            task_list.pop(0)
            show_list()
        else:
            print("La lista está vacía. No se puede quitar un elemento del principio.")
            separator()

    def continue_or_exit():
        print("¿Quiere seguir modificando la lista?")
        choice = input("Presione Enter para Seguir u otra tecla para Salir: ")
        separator()
        if choice != "":
            print("Saliendo del gestor de tareas...")
            exit()

    def choose_option():
        while True:
            separator()
            print(
                """Elija una opción:
                a - Para agregar un elemento al final
                b - Para agregar un elemento al principio
                c - Quitar un elemento del final
                d - Quitar un elemento del principio
                """
            )
            print("Lista actual: " + str(task_list))
            separator()
            option = input("Opción: ")
            separator()
            if option == "a":
                add_to_end()
            elif option == "b":
                add_to_start()
            elif option == "c":
                remove_from_end()
            elif option == "d":
                remove_from_start()
            else:
                print("No elegiste una opción correcta, elije nuevamente")
                continue

            continue_or_exit()

    choose_option()

task_manager()