import random

def mezclador_nombre_random():
	nombre=input("Cual es tu nombre: ")
	apellido=input("cual es tu primer apelido: ")
	mezcla=list(apellido)
	random.shuffle(mezcla)


	#inversor = nombre[::-1]
	cadena="".join(mezcla)
	print("\nSaludar todos a lord",nombre,apellido,"de la Casa ",cadena)



mezclador_nombre_random()




	

