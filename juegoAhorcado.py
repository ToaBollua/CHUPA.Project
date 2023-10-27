#AHORCADO
import random

boi = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

palabras = 'hola caballo hombre roberto fica pene marihuana perro metamorfosis paralelepipedo poto creacion consistencia abril'.split()

def ahorcado(palabras):
    eleccion = random.randint(0, len(palabras) - 1)
    return palabras[eleccion]

def interface(boi, incorrecto, correcto, eleccion):
    print(boi[len(incorrecto)])
    print("")
    fin = " "
    print("Letras equivocadas: ", fin)
    for letra in incorrecto:
        print(letra, fin)
    print("")
    espacio = "_" * len(eleccion)
    for posicion in range (len(eleccion)):
        if eleccion[posicion] in correcto:
            espacio = espacio[:posicion] + eleccion[posicion] + espacio[posicion + 1:]
    for letra in espacio :
        print(letra, fin)
    print("")
    
def adivinar_letra(adivinacion):
    while True:
        print('Ingrese una letra: ')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print('Introduce una letra a la vez...')
        elif letra in adivinacion:
            print('Ya nombraste esta letra. Por favor elige otra...')
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz':
            print("Vo crei q soy weon? Elige una letra.")
        else:
            return letra

def juego():
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

print('Jogo do ahorcadinho')
incorrecto = ""
correcto = ""
eleccion = ahorcado(palabras)
juego_fin = False
while True:
    interface(boi, incorrecto, correcto, eleccion)
    letra = adivinar_letra(incorrecto + correcto)
    if letra in eleccion:
        correcto = correcto + letra
        encontrado = True
        for i in range(len(eleccion)):
            if eleccion[i] not in correcto:
                encontrado = False
                break
        if encontrado:
            print('Felicidades!, la palabra secreta es: ' + eleccion)
    else:
        incorrecto = incorrecto + letra
        if len(incorrecto) == len(boi) - 1:
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(incorrecto)) + ' letras erroneas y ' + str(len(correcto)) + ' letras correctas, la palabra era "' + eleccion + '"')
            juego_fin = True
    
    if juego_fin:
        if juego():
            incorrecto = ""
            correcto = ""
            juego_fin = False
            eleccion = ahorcado(palabras)
        else:
            break
            