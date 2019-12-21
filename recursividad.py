def factorial(n):
	if n is 1:                        #Factorial modo recursivo
		return 1
	else:
		return n*factorial(n-1)

#Llamada función
num=int(input("\nIntroduce un número: "))
print("El factorial de {} es : {} ".format(num,factorial(num)))