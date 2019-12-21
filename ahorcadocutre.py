import random
import winsound
frequencyV = 3000  # FRECUENCIA PARA VICTORIA.
durationV = 200  # DURACIÓN PARA VICTORIA.
frequencyF = 1000  # FRECUENCIA PARA DERROTA.
durationF = 2000  # DURACIÓN PARA DERROTA.



AHORCADO = ['''
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


def palabra_aleatoria(palabras): #ELIGE UNA PALABRA AL AZAR DE LA LISTA DE PALABRAS PARA EL JUEGO.

	aleatoria=random.randint(0,len(palabras)-1)

	return palabras[aleatoria]

def palabra_A_caracteres(palabra): #PASA LA PALABRA A LISTA DE CARACTERES.
	eleccion=[]
	for i in palabra:
		eleccion+=[i]
	return eleccion

def juego(vidas,elegida,longitud): # COMPRUEBA SI LETRA ESTÁ EN PALABRA Y SI ES ASÍ SUSTITUYE EL '_' POR LA LETRA.

	print("\n\n {}\n\n".format(vidas))
	print("\nLa palabra contiene {} letras\n".format(longitud))
	cont=0
	yes=False
	otra=''
	
	while cont<7:
		letra=input("\nIntroduce una letra:")
		e=letra in elegida
		if e:
			print("\nHas dado una\n")
			posicion=elegida.index(letra)
			vidas.pop(posicion)
			vidas.insert(posicion,letra)
			print(vidas)
			o= '_' in vidas
			if o is False:
				yes=True
				break 
		else:
			print("\nNo has acertado\n")
			print(AHORCADO[cont])
			cont+=1

	if cont == 7:
		print("**********************************************************************")
		print("\n\n\n\nLa palabra era: \n\n\n{}\n".format(elegida))
		print("\n\n\n\n                   GAME OVER\n")
		winsound.Beep(frequencyF, durationF)
		while otra != 'y' and otra != 'n':
			otra=input("\n¿Quieres jugar otra partida? (y/n): ")	
		return otra

	if yes is True:
		print("**********************************************************************")
		print("\n\n\n\n                   HAS GANADO EL JUEGO\n")
		winsound.Beep(frequencyV, durationV)
		while otra != 'y' and otra != 'n':
			otra=input("\n¿Quieres jugar otra partida? (y/n): ")
		return otra	

#COMIENZO EJECUCIÓN PROGRAMA.

print("\n\n*****************************************EL AHORCADO*******************************************\n\n")
palabras=['monte','culo','hijo','persona','arbol','cantero','entropia','gato','tsunami','truhan','coruña','castigo','oregon','raton','hueco','hielo','rapunsel','celosia','medusa','fusion']
otra=''
while otra is not 'n':
	eleccion=palabra_aleatoria(palabras)
	longitud=len(eleccion)
	vidas=[]
	for i in range(longitud):
		vidas+=['_']

	elegida=palabra_A_caracteres(eleccion)
	otra=juego(vidas,elegida,longitud)

print("	\n\nHASTA LUEGO!!!")