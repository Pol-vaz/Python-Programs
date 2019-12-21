import sqlite3


lon=int(input("Introduce cuantos artículos quieres subir: "))

for i in range(lon):

	nombre=input("Introduce el nombre del producto: ")
	precio=int(input("Introduce el nombre del producto: "))
	seccion=input("Introduce el nombre del producto: ")


miconexion=sqlite3.connect("GestionProductos")

micursor=miconexion.cursor()


productos= [nombre,precio,seccion]

micursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER, 
	SECCION VARCHAR(20))
''')

	
productos=[nombre, precio ,seccion]

micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)


miconexion.commit()

miconexion.close()