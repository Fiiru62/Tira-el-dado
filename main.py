# Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like). 
# Write one subroutine with one parameter that allows us to call a function (such as rollDice).

import random

# tiradas = int(input("Cuantas veces quieres tirar el dado? "))

# bucle que pide la cantidad de lados del dado y valida que la entrada sea correcta
while True:
    try:
        lados = int(input("Cuantos lados tiene el dado? "))
        # si se ingresa un numero negativo o 0
        if lados < 1:
            print("No se puede tirar un dado con menos de 1 lado")
            # el continue vuelve al inicio del bucle
            continue
        # el break corta el bucle si la entrada es correcta
        break
    # si se ingresa un valor que no es un numero
    except ValueError:
        print("Por favor ingresa un numero válido")
        # el continue vuelve al inicio del bucle
        continue
        
# funcion que dice el numero que salio y pregunta si se quiere tirar de nuevo
def rollDice():
    # bucle para repetir el programa tantas veces como el usuario quiera
    while True:
        # elige un numero aleatorio entre 1 y "lados" que seria el numero maximo que puede salir
        num = random.randint(1, lados)
        print("El numero que salio es: ", num)
        
        # pregunta si se quiere volver a jugar. En el caso de que si, la variable num vuelve a elegir un numero aleatorio
        repetir = input("\nQuieres tirar el dado de nuevo? ").lower()
        if repetir == "si":
            continue
        else:
            # si el usuario pone algo que no sea si, se cierra el programa
            break
    print("Gracias por jugar!")
        
# se llama a la funcion       
rollDice()
