def area_tringulo(base,altura):
	return (base*altura)/2                                 #funcion convencional

triangulo1=(area_tringulo(10,7))

triangulo2=(area_tringulo(9,6))

print(triangulo1 ,"y ",triangulo2)

#*******************************************************************************

area_tringulo=lambda base, altura : (base*altura)/2        #funcion Lambda

print(area_tringulo(15,8))

#**********************************************************************************

al_cubo=lambda numero: numero**3

print(al_cubo(13))                                             #otro ejemplo

#************************************************************************************

destacar_valor=lambda comision: "¡{}! $".format(comision)

comision_Ana= 15585                                             #otro ejemplo

print(destacar_valor(comision_Ana))