import time

""" Ejercicio 1
 La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte),
 solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
 Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande. """

def max_in_list(lista):
 	return max(lista)


print(max_in_list([2,6,3,9,4,1,5,11,45,2,55,1,98,3,4,2]))



""" Ejercicio 2
 Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. """

def mas_larga(palabras):
 	lista=[]
	
 	for i in palabras:
 		 lista.append(len(i))
 	maxim= max(lista)
 	for a in palabras:
 		if maxim is len(a):
 			return a
	
	
print(mas_larga(["hola","mi","marios","cacacolapituperro","escalada","motocicleta","El rey en el Norte","candela"]))


""" Ejercicio 3
 Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 
  """
"""
def filtar_palabras(palabras,n):
	lista=[]
 	
 	for i in palabras:
 		if len(i) > n:
 			lista.append(i)
	
	return lista
		
num=int(input("Introduce un número: "))
print(filtar_palabras(["calamar","hola","mi","marios","cacacolapituperro"],num))
"""
"""Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena.
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.  """

def mayus_Cadena(cadena):
 	mayus=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','Y','Z']
 	count=0
 	for i in range(len(cadena)):
 		for j in range(len(mayus)):
 			if cadena[i] is mayus[j]:
 				count+=1

 	return count


cade= input("Introduzca una cadena de carateres: ")
print(mayus_Cadena(cade))

""" Ejercicio 5
Construir un pequeño programa que convierta números binarios en enteros. """

def bin_int(bina):
 	num=int(bina,2)
 	return num

binario=input("Introduzca un numero binario: ")
print(bin_int(binario))

"""Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla. """


def año_cumple():
	tiempo = time.gmtime()
	segundos_dia=tiempo.tm_hour*3600 +tiempo.tm_min*60 + tiempo.tm_sec

	for i in range(3):
		print("Persona {} \n".format(i+1))
		nombre=input("Cual es tu nombre?: ")
		data=int(input("En que año naciste, {}?: ".format(nombre)))
		mes= int(input("En que mes?(en número): "))
		if mes> tiempo.tm_mon:
			print("{}, tienes {} años ahora mismo".format(nombre,tiempo.tm_year-data-1))
			print("De hecho existes en este mundo desde hace {} segundos. ".format(((tiempo.tm_year-data-1)*8760*3600)+segundos_dia))
			
		else:
			print("{}, tienes {} años ahora mismo".format(nombre,tiempo.tm_year-data))
			print("De hecho existes en este mundo desde hace {} segundos. ".format(((tiempo.tm_year-data)*8760*3600)+segundos_dia))
		print("\n---------------------------------------------------------------------------------------------\n")	

año_cumple()



"""Ejercicio 7
Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades."""

def tupla_edad(tupla):
	count=0
	print("\n Las personas con una edad superior a 20 son: \n")
	for i in range(len(tupla)):
		if tupla[i] > 20:
			print(tupla[i])
			count+=1
	print("\n El numero de personas con una edad superior a 20 son: \n")
	return count
	
	

edades=(10,30,54,32,12,76,98,45,20,65)
print(tupla_edad(edades))

		
""" Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante) """



def comienzo_nombre(nombres):
	
	for i in range(len(nombres)):
		inicial(nombres[i])

	
def inicial(nom):


	for j in range(1):
		if nom[0] == "a":
			print(nom," empieza por a \n")
			
	
nombre=['macario','lorenzo','anacardo','ana','laurentino','samael','andres']
comienzo_nombre(nombre)


""" Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400"""

def bisiesto(año):
	if año %4  is 0:
		if año %100 is not 0:
			print("es bisiesto ")
		if año %100 is 0 and año %400 is 0:
			print("es bisiesto total, con el error gregoriano corregido ")
	else:
		print("no es bisiesto")

ano=int(input("Introduce un año: "))
bisiesto(ano)	



