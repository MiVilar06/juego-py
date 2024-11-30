

import random


numero_secreto = random.randint(0,100)
cant_int = 0
cant_maxint = 5
adivinado = False

print("Bienvendidx a Adivina Adivinados, suerte encontrando el número oculto")

while not adivinado:
    if not cant_int < cant_maxint:
        print("Buuuu!!! Te quedaste sin intentos")
        break

    entrada = input("Elige un número entre el 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicidades champ! Ganaste!")
        adivinado = True
    elif numero < numero_secreto:
        print("Caliente,caliente! No es el número, pero puede que sea mayor")
    else:
        print("Casi,casi! Proba con números más chicos")

    cant_int += 1
