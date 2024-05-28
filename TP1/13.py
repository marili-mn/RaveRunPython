def generate_username(name, lastname):
    # Concatenar la primera letra del nombre y el apellido, y convertir a minúsculas
    username = (name[0] + lastname).lower()
    return username

def generate_password(initials, year):
    # Concatenar las iniciales y el año de nacimiento
    password = initials + "." + year
    return password

def main():
    # Pedir al usuario que ingrese su nombre, apellido y año de nacimiento
    name = input("Ingrese su nombre: ")
    lastname = input("Ingrese su apellido: ")
    year = input("Ingrese su año de nacimiento: ")

    # Generar el nombre de usuario
    username = generate_username(name, lastname)

    # Generar las iniciales para la contraseña
    initials = name[0].lower() + lastname[0].lower()

    # Generar la contraseña
    password = generate_password(initials, year)

    # Imprimir la sugerencia de usuario y contraseña
    print("Sugerencia de usuario:", username)
    print("Sugerencia de contraseña:", password)
main()
