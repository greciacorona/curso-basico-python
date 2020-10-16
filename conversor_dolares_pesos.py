dolares = input("¿Cuántos dólares tienes? ")
dolares = float(dolares)
valor_pesos = 0.047
pesos = dolares / valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos mexicanos")