import time

class agenda_telefonica:

	def __init__(self):
		self.dicc= {}

	def agrega(self,nombre,numero,email):
		self.dicc[nombre] = (numero,email)

	def borrar(self,nombre):
		del self.dicc[ nombre]

	def actualizar(self,nombre,valores):
		self.dicc[nombre]= valores

	def imprime(self):
		for i in self.dicc:

			print("\n",i,self.dicc[i])

	def exportar(self):
	
		fichero=open('/Users/molam/Desktop/Agenda_telefono.txt','w')
		for j in self.dicc:
			lista= str(j) , str(self.dicc[j])
			fichero.write(str(lista))

		fichero.close

	@property
	def cantidad(self):
		return len(self.dicc)


miagenda=agenda_telefonica()

miagenda.agrega("Amigos de Fran",677076532,'pollascalientes@hotmail.com')

#entrada de datos agenda

def opcion_agregar():
	numero_telefono= '0'
	nombre=input("\nIntroduce el nombre de el contacto: ")
	#while numero_telefono == 'a' or numero_telefono != '2' or numero_telefono != '3' or numero_telefono != '4'or numero_telefono != '5' or numero_telefono != '6' or numero_telefono != '7' or numero_telefono != '8' or numero_telefono != '9':
	numero_telefono=input("\nIntroduce el número de teléfono de el contacto: ")
	correo=input("\nIntroduce el correo electrónico de el contacto: ")
	miagenda.agrega(nombre,numero_telefono,correo)
	time.sleep(1)

def opcion_borrar():

	nombre_borrar=input("\nIntroduce el nombre de el contacto: ")
	miagenda.borrar(nombre_borrar)
	time.sleep(1)
	print("\nEl contacto {} ha sido borrado exitosamente\n".format(nombre_borrar))
	time.sleep(1)

def opcion_actualizar():

	nombre_modificar=input("\nIntroduce el nombre de el contacto que quieras modificar: ")
	numero_telefono_modificar=input("\nIntroduce el nuevo número de teléfono de el contacto a modificar: ")
	correo_modificar=input("\nIntroduce el nuevo correo electrónico de el contacto a modificar: ")
	miagenda.actualizar(nombre_modificar,(numero_telefono_modificar,correo_modificar))
	time.sleep(1)

def opcion_mostrar():
	print("\n")
	miagenda.imprime()
	time.sleep(1)

def opcion_num_contactos():

	print("\nLa cantidad de contactos en la agenda es: ",miagenda.cantidad) 
	time.sleep(1)

def opcion_exportar():

	miagenda.exportar()
	print("\nLa agenda ha sido exportada en formato 'txt' en tu escritorio\n") 
	time.sleep(1)


	
#Comienzo programa

a=True
opcion=0
while a == True:

	print("\n******************************************AGENDA TELEFÓNICA PYTHON******************************************\n")
	

	while opcion != '1' or opcion != '2' or opcion != '3' or opcion != '4' or opcion != '5'  or opcion != '6':
		print("\n*****************************************************************************************************************\n")
		print("¿Que quieres hacer?\n")	
		opcion=input("\n1. Agregar contacto\n2. Borrar contacto\n3. Modificar contacto\n4. Mostrar información de contacto\n5. Indicar el número de contactos presentes en la agenda\n6. Exportar agenda en formato de texto\n7.Salir\n\nElige la opción: ")
		
		
		if opcion is '1':
			opcion_agregar()
		elif opcion is '2':
			opcion_borrar()
		elif opcion is '3':
			opcion_actualizar()
		elif opcion is '4':
			opcion_mostrar()
		elif opcion is '5':
			opcion_num_contactos()
		elif opcion is '6':
			opcion_exportar()
		elif opcion is '7':
			print("\n")
			a=False
			break


print("\nHasta luego\n")


