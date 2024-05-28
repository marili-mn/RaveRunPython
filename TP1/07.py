def days_to_hours_minutes_seconds():

    days = int(input("Ingrese el número de días: "))

    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(f"{days} días son:")
    print(f"{hours} horas")
    print(f"{minutes} minutos")
    print(f"{seconds} segundos")

days_to_hours_minutes_seconds()