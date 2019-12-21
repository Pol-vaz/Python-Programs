import random

def mezclador_nombre_random():
	nombre=input("cual es tu nombre: ")
	nombres=list(nombre)
	random.shuffle(nombres)


	#inversor = nombre[::-1]
	cadena="".join(nombres)
	print("\n",cadena)


mezclador_nombre_random()




	

