'''compra=['pan','jamon','queso',23]
nombre='cristina'

#print(dir(compra))

compra.append(323)

print(compra)

compra.insert(1,'arroz')

print(compra)

print(compra.index('queso'))

com=tuple(compra)

print(type(nombre))

lista=list(nombre)

print(type(lista))

print(lista[3])

lista.remove('t')
lista.append('w')

print(lista)'''


stock = {'camiseta':20,
		 'polo':40,
		 'camisa': 30,
		 'cazadora': 70,
		 'pantalon': 20   }




stock['polo']= 50


print("Bienvenido a la boutique de cris y paol\n Elijan el producto de nuestra tienda que mas les guste: \n")

print("Tenemos:\n\n1- camiseta\n2- polo\n3- camisa\n4-cazadora\n5- pantolon\n")

eleccion=input()
print(stock[eleccion])























