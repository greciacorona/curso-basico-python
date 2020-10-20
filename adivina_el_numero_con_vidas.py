import random


def run():
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)
    numero_elegido = int(input("Elige un número del 1 al 100, tienes 3 oportunidades: "))
    vidas = 2
    while numero_elegido != numero_aleatorio and vidas > 0:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande")
        elif numero_elegido > numero_aleatorio:
            print("Busca un número más pequeño")
        numero_elegido = int(input("Elige otro número: "))
        vidas -= 1
    if vidas == 0:
        print("¡Perdiste!")
    else:
        print("¡Ganaste!")


if __name__ == '__main__':
    run()