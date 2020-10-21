import random
import string

def generar_contrasena():
    letras = list(string.ascii_letters)
    simbolos = list(string.punctuation)
    numeros = list(string.digits)

    caracteres = letras + simbolos + numeros

    contrasena = []
    longitud = int(input("¿Longitud de la contraseña?: "))
    
    for i in range(longitud):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena) 


if __name__ == "__main__":
    run()