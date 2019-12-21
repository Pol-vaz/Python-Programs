import sqlite3

miconexion=sqlite3.connect("PrimeraBase")

micursor=miconexion.cursor()

#
micursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

miconexion.commit()


 

miconexion.close()