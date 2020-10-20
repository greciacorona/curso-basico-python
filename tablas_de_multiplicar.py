def run():
    tabla = input("¿Qué tabla de multiplicar quieres ver?")
    for i in range(11):
        print("2 X " + str(i) + " = " + str(int(tabla) * i))


if __name__ == '__main__':
    run()