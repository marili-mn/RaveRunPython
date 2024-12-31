def task_manager():
    pending_tasks = []
    completed_tasks = []

    def separator():
        print("*****************************************************")

    def display_tasks(task_type, tasks):
        separator()
        print(f"Tareas {task_type}:")
        for idx, task in enumerate(tasks):
            print(f"* {idx} *** {task} *")

    def show_task_status():
        display_tasks("pendientes", pending_tasks)
        display_tasks("realizadas", completed_tasks)

    def add_task():
        new_task = input("Ingrese una tarea nueva para agregar: ")
        pending_tasks.append(new_task)
        show_task_status()

    def mark_task_completed():
        task_number = input("Ingrese el número de tarea a marcar para finalizar: ")
        if not task_number.isdigit():
            print("Por favor, ingrese un número válido.")
        else:
            task_number = int(task_number)
            if 0 <= task_number < len(pending_tasks):
                completed_tasks.append(pending_tasks.pop(task_number))
            else:
                print("Número de tarea no válido.")
        show_task_status()

    def menu():
        while True:
            separator()
            choice = input("Presiona 1 para Agregar una tarea, 2 para pasar una tarea a Completada, o enter para salir: ")
            if choice == "1":
                add_task()
            elif choice == "2":
                mark_task_completed()
            elif choice == "":
                break
            else:
                print("Valor incorrecto")

    menu()

task_manager()
