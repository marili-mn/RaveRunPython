total = float(input("Ingrese el precio total de la cuenta: "))
num_Clients = int(input("Ingrese el número de comensales: "))

# Verificar si el número de comensales es válido
while num_Clients <= 0:
    print("El número de comensales debe ser mayor que cero.")
    num_Clients = int(input("Ingrese el número de comensales nuevamente: "))


amount_per_client = total / num_Clients
print("Cada persona debe pagar:", amount_per_client)
