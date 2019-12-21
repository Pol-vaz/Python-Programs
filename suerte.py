import random
import time



def cara_cruz():

	cara=0
	cruz=0
	jugador1=input("\n Como se llama el primer jugador: ")
	jugador2=input("\n Como se llama el segundo jugador: ")

	print("\n {}, tu irás con cara. \n".format(jugador1))
	print("\n {}, tu irás con cruz. \n".format(jugador2))
	time.sleep(3)

	for i in range(5):
	
		opcion=random.randint(1,10)
		if opcion <=5:
			time.sleep(1)
			print("cara\n")
			cara+=1

		if opcion >5:
			time.sleep(1)
			print("cruz\n")
			cruz+=1

		i+=1

	time.sleep(2)

	if cara >=3:
		print("\n Gana {}!! ".format(jugador1))

	if cruz >= 3:
		print("\n Gana {}!! ".format(jugador2))



cara_cruz()