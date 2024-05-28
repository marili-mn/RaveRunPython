def calculate_power(base, exponent):
    """
    Calcula la potencia de un entero positivo base elevado a un exponente.

    Parámetros:
    base (int): La base de la potencia.
    exponente (int): El exponente al que se elevará la base.

    Retorna:
    int: El resultado de elevar la base al exponente.
    """
    # Verifica si la base es negativa
    if base < 0:
        return "Error: La base debe ser un entero positivo."

    # Calcula la potencia
    resultado = base ** exponent
    return resultado

# Ejemplo de uso
base = int(input("Ingresa un entero positivo como base: "))
exponente = int(input("Ingresa el exponente al que quieres elevar la base: "))

resultado = calculate_power(base, exponente)
print(f"El resultado de {base} elevado a la potencia de {exponente} es: {resultado}")
