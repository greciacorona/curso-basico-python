def es_primo(numero):
    if numero > 1:
        import math
        if (math.factorial(numero - 1) + 1) % numero == 0:
            return True
        else:
            return False
    else:
        return False


def run(): 
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} NO es primo")


if __name__ == "__main__":
    run()