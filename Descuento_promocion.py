import random

def sorteo():
	compra=float(input("\nINTRODUZCA LA CANTIDAD TOTAL DE LA COMPRA: "))

	if compra >= 100.00:
		print("\nSU GASTO IGUALA O SUPERA LOS $100.00 Y POR TANTO PARTICIPARA EN LA PROMOCION.\n")

		bola=random.randint(0,4)

		if bola is 0:
			bola="BLANCA"
		
		elif bola is 1:
			bola="ROJA"
			descuento=10
		elif bola is 2:
			bola="AZUL"
			descuento=20
		elif bola is 3:
			bola="VERDE"
			descuento=25
		elif bola is 4:
			bola="AMARILLA"
			descuento=50

		print("COLOR                   DESCUENTO\n")
		print("BOLA BLANCA              NO TIENE\n")
		print("BOLA ROJA             10 POR CIENTO\n")
		print("BOLA AZUL             20 POR CIENTO\n")
		print("BOLA VERDE            25 POR CIENTO\n")
		print("BOLA AMARILLA         50 POR CIENTO\n")

	

		print("ALEATORIAMENTE USTED OBTUVO UNA BOLA {}\n ".format(bola))
		if bola is 'BLANCA':
			print("LO SENTIMOS, NO HA GANADO NINGÚN DESCUENTO\n")
		else:
			print("FELICIDADES, HA GANADO UN {} POR CIERTO DE DESCUENTO\n".format(descuento))
			print("SU NUEVO TOTAL A PAGAR ES: ${}\n".format((compra-(compra*(descuento/100)))))

	else: 
		print("\nSU GASTO NO SUPERA O IGUALA LOS $100.00 Y POR TANTO NO PARTICAPARA EN LA PROMOCION\n")	

	
while True:

		sorteo()
		numero=input("SI DESEA SALIR PRESIONE '1' O DE O CONTRARIO PRESIONE OTRA TECLA: ")
		if numero is '1':
			break
		else:
			print("VOLVERÁ A PARTICIPAR. MUCHA SUERTE!!\n")


print("\nHASTA LUEGO!!\n")