import sqlite3

miconexion=sqlite3.connect("GestionProductos")

micursor=miconexion.cursor()


#micursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")
micursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")



miconexion.commit()

miconexion.close()