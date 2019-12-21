import sqlite3

miconexion=sqlite3.connect("GestionProductos")

micursor=miconexion.cursor()

micursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER, 
	SECCION VARCHAR(20))
''')

productos=[

	("pelota", 20,"juguetería"),
	("pantalón", 15,"confección"),
	("destornillador", 25,"ferretería"),
	("jarrón", 45,"cerámica"),
	("pantalones", 35,"confección"),

]

micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)


miconexion.commit()

miconexion.close()