def main():
    date = input("Ingrese una fecha en formato dd/mm/aaaa: ")

    day, month, year = date.split("/")

    print(f"Día: {day}, Mes: {month} y Año: {year}")

main()