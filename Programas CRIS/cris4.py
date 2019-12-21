#ARCHIVOS

'''palabra='unos'

archivo=open('cristina.txt','w')

archivo.write("Hoy hemos desayunado unos croasants\n bien ricos en el hotel spa")

archivo.close()

archivo2=open('cristina.txt','r')


for i in archivo2:

	if palabra in i:
		print ("\nEncontrada")

	else:
		print('\nNo encontrada')


archivo2.close()'''



'''
- Haga un programa que abra un archivo llamado 'queja.txt'
  y escriba lo siguiente:

   'Mi nombre es cristina sanchez prado y necesito que me suban el sueldo a 3000 euros para cocido o me voy de la empresa'

- A continuacion que lo abra en modo lectura y lo lea entero mostrandolo por pantalla.
- A continuación que busque la palabra 'cocido' dentro de el texto y si la palabra aparece que se
  muestre por pantalla 'Encontrada' sino que se muestre 'No encontrada' 

'''
valido=False
while valido==False:
	palabra=input('\nDime una palabra: ')


	carpeta=open('queja.txt','r')

	for i in carpeta:
		if palabra in i:
			print('\nEncontrada')

		else:
			print('\nNo encontrada')

	juego=input("\n¿Quieres seguir juagando(s/n)?: ")

	if juego=='s':
		valido=False

	else:
		valido=True


	carpeta.close()


print('\nGracias por jugar.\nVuelve pronto.')






