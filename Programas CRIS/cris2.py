'''
productos=["polo","camisa","cocaina","chancleta"]
precios=[50,30,130,80]


def tienda(productos,precios):    #creas la funcion tienda

	respuesta="s"
	print("Cuanto dinero tienes?: ")
	dinero=int(input())

	while respuesta=="s":
		print("\nElija un producto de nuestra tienda:\n 1- polo     - 50$\n 2- camisa   - 30$\n 3- cocaina  - 120$ \n 4- chancleta - 80$\n")
		eleccion=int(input())
		if dinero>precios[eleccion-1]:
			print(f"\nEsta bien, has comprado: {productos[eleccion-1]}, que cuesta {precios[eleccion-1]}$\n")
			dinero=dinero-precios[eleccion-1]
			print(f"\nTe queda {dinero}$ en la cartera\n")
			respuesta=input("\n¿Quiere comprar algo más (s/n)?: ")
			if respuesta=="n":
				respuesta="n"

		else:
			print("\nNo te llega el dinero\n")
			respuesta=input("\n¿Quiere comprar algo más (s/n)?: ")
			if respuesta=="n":
				respuesta="n"

# Se invoca la función

tienda(productos,precios)'''





'''
#SOLUCION EJERCICIO 3:

lista=[1,2,3,4,5,6,7,8,9,10,2,3,'r']

def longitud(lista1):
	cont=0

	for x in lista:
	
		cont=cont+1

	return cont

resultado=longitud(lista)

print(resultado)'''



'''li1=[1,2,3,4]
li2=[5,6,7,8]
li3= []
i=0

for x in li1:
	li3.append(li1[i]*li2[i])
	i+=1

print(li3)'''
	
#Funciones

'''def max_de_tres(num1,num2,num3):
	
	mayor=max(a,b,c)
	return mayor


cond=False

while cond==False:

	a=int(input("Dime un número: "))
	b=int(input("Dime otro número: "))
	c=int(input("Dime otro número: "))


	if a != type(int) or b != type(int) or c != type(int):

		print("\nSolo puedes introducir enteros!!\n")
		cond=False
	else:
		cond=True
	

maximo=max_de_tres(a,b,c)
print(maximo)'''





# EJERCICIO 3: Crea una función llamada longitud que reciba una lista previamente creada y te devuelva su longitud
#			     tal como haria la función "len".

#             [Solución arriba de todo.No mirar al menos que seas una caguica y te rindas]


'''li=[13,2,31,40,7,14]


def longitud(argumento):
	x=0
	for i in argumento:
		x+=1
	return x


a=longitud(li)
print(a)'''






	
'''4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.'''


'''def madagascar(caracter):
	
	if caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u":
		valido=True

	else:
		valido=False

	return valido 


x=input("Dime una letra: ")
y=madagascar(x)
print (y)'''











'''5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.



def sum(lista):
	x=0
	suma=0
	for i in lista:
		suma=lista[x]+suma
		x+=1
	return suma

def multip(lista):
	y=0
	m=1
	for j in lista:
		m=lista[y]*m
		y+=1
	return m 

li=[2,2,1,3]
a=sum(li)
b=multip(li)

print(li)
print(a)
print(b)

webbrowser.open_new("https://www.youtube.com/watch?v=4JVaRloezno&pbjreload=10")'''

'''Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el nombre y el año de nacimiento de una persona.
- Si la persona es mayor de 18 años se le pide una contraseña que solo conocerá el programador.
  Si la persona sabe la contraseña se le muestra el siguiente texto: "Bella ciao,bambini"
   y a continuación ejecuta esta instrucción:

  webbrowser.open_new("https://www.youtube.com/watch?v=4JVaRloezno&pbjreload=10")

-Si la persona es menor de edad se le muestra el siguiente mensaje: "No se puede acceder si se es menor de edad" 
y se acabe el programa(no ejecute nada más vamos)'''

'''import webbrowser

def rest(año):
	Resta=2019-año

	return Resta



Nombre=input("Dime tu nombre: ")
Añodenacimiento=int(input("Dime tu año de nacimiento: "))
a=rest(Añodenacimiento)


Condicion=False

if a>18:
	print("Contraseña: ")
	Contraseña=input()

	while Condicion==False:

		print("Contraseña: ")
		Contraseña=input()

		if Contraseña =="cristi":
			print("Bella ciao, bambini")
			webbrowser.open_new("https://www.youtube.com/watch?v=4JVaRloezno&pbjreload=10")
			Condicion=True

		else:
			print("Contraseña incorrecta")
			

else:
	print("No se puede acceder si se es menor de edad")

Haga un programa que pida al usuario que elija que producto quiere comprar de una lista de productos con sus precios en una tienda 
-Primero le pide al usuario cuanto dinero tiene
-Después le muestra al número de productos que tiene la tienda con sus precios
-El usuario elije el numero de el producto y si le llega el dinero lo compra 

ejemplo:

		-cuanto dinero tiene?
		- 150
		-Elija un producto de nuestra tienda:
		 1- polo     - 50$
		 2- camisa   - 30$
		 3- cocaina  - 120$
		 4- chancleta - 80$

		 - 2

		 -Esta bien, has comprado una camisa 
		 -¿Quiere comprar algo más (s/n)?
		 - s

		 -Elija un producto de nuestra tienda:
		 1- polo     - 50$
		 2- camisa   - 30$
		 3- cocaina  - 130$
		 4- chancleta - 80$

		 - 3
		 -No te llega el dinero.
		 -¿Quiere comprar algo más (s/n)?
		 - n
		 -Hasta luego, gracias por venir a nuestra tienda


		LA SOLUCIÓN ESTA ARRIBA'''

		



print('\nBienvenido a nuestra tienda online. Le mostramos nuestra selección de articulos.')
dinero=int(input('\n¿Cuánto dinero tiene?:'))
valido=False
while valido==False:

	stock={'cazadora':50,
 		'camiseta':15,
 		'camisa':20,
 		'jersey':25,
 		'sudadera':25,
 		'pantalón':30,
 		'zapato':60}


	print("\nCazadora - 50$\nCamisa -15$\nJersey - 25$\nSudadera - 25$\nPantalón - 30$\nZapato - 60\n")

	producto=input('\nElija un producto de nuestra tienda: ')

	

	if dinero<stock[producto]:
			print('\nNo te llega el dinero. \nGracias por comprar en nuestra tienda online.')
			valido=True
			break

	dinero=dinero-stock[producto]

	print(f'\nEsta bien, has comprado {producto}')
	print(f'\nTienes actualmente {dinero}$ ')



	

	

	Respuesta=input('\n¿Quieres comprar algo más? (s/n): ')

	

	if Respuesta=='s':

		valido=False

		
	else:
		valido=True
		print('\nHasta luego. \nGracias por comprar en nuestra tienda online.')


	
		















