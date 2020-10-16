menu = """
Bienvenido al conversor de monedas 💱

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes? ")
    pesos = float(pesos)
    valor_dolar = 3845
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes? ")
    pesos = float(pesos)
    valor_dolar = 77.49
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes? ")
    pesos = float(pesos)
    valor_dolar = 21.13
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Ingresa una opción correcta")

