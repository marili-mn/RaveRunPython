def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    """
    Calcula el total de una factura tras aplicarle el IVA.

    Parámetros:
    cantidad_sin_iva (float): La cantidad sin IVA.
    porcentaje_iva (float, opcional): El porcentaje de IVA a aplicar. Por defecto es 21%.

    Retorna:
    float: El total de la factura después de aplicar el IVA.
    """
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total

# Ejemplo de uso
cantidad_sin_iva = float(input("Introduce la cantidad sin IVA: "))
porcentaje_iva = float(input("Introduce el porcentaje de IVA (opcional, presiona Enter para aplicar el 21% por defecto): ") or 21)

total_factura = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)
print(f"El total de la factura es: {total_factura}")
