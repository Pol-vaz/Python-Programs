import math


"""
1- Definir una función max() que tome como argumento dos números
y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio."""

def max(a,b):
	if a>b:
		return a
	elif a is b:
		return "los numeros son iguales"

	else :
		return b

print(max(7,4))


""" 2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos."""

def max_3(a,b,c):
	if a>b and a>c:
		return a
	elif a<b and b>c:
		return b

	else :
		return c

print(max_3(9,10,8))


"""3- Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio. """

def longitud(lista):
	c=0
	for i in lista:
		c+=1
	
	return c

print(longitud([5,2,5,3,8]))


""" 4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False. """
def vocales(letra):
	if letra is 'a' or letra is 'e' or letra is 'i' or letra is 'o' or letra is 'u':
		return True
	else:
		return False

print(vocales("f"))


""" 5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24. """

def sum_lista(lista):
	suma=0
	for i in lista:
		suma+=i
	return suma

def mult_lista(lista):
	multi=1
	for i in lista:
		multi=multi*i
	return multi
	
print(sum_lista([1,2,3,4]))
print(mult_lista([1,2,3,4]))


""" 6- Definir una función inversa() que calcule la inversión de una cadena.
 Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"""

def inversa(cadena):
	print(cadena[::-1])

inversa("polladura")


""" 7 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True."""

def es_palindromo(cadena):
	for i in cadena:
		if cadena[0] is cadena[len(cadena)-1]:
			return True
		else:
			return False

print(es_palindromo("radar"))


""" 8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos
 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.  """

def superposicion(lista1,lista2):
	opcion=0
	for i in range(len(lista1)):
		for j in range(len(lista2)):
			if lista1 [i] is lista2[j]:
				opcion=1
				return True
	if opcion is not 1:
		return False

print(superposicion([1,2,7,9],[4,5,6,7]))


""" 9- Definir una función generar_n_caracteres() que tome un entero n
 y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"."""


def generar_n_caracteres(n,letra):
	return 5*letra

print(generar_n_caracteres(5,"p"))



""" 10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
 Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******                                                                                                                           """

def histograma_procedimiento(lista):
	for i in range(len(lista)):
		a=lista[i]
		print(a*"*")

histograma_procedimiento([4,9,7])



