def run():
    tabla = input("¿Qué tabla de multiplicar quieres ver?")
    for i in range(11):
        print(f"2 X {i} = {int(tabla) * i}")


if __name__ == '__main__':
    run()