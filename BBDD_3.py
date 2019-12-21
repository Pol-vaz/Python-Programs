import sqlite3

miconexion=sqlite3.connect("GestionProductos")

micursor=miconexion.cursor()


micursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección' ")

productos=micursor.fetchall()

print(productos)


miconexion.commit()

miconexion.close()