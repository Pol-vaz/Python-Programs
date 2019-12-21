from math import factorial,exp
x= 10
resul=0


def error(resul,x):
	real= exp(x)
	porcentaje=abs(real-resul)/100
	print(f"\nERROR: {porcentaje}%\n")

for num in range(1,50):

	resul=resul+(1+(x**num/factorial(num)))
	print(f"*{num+1}*: {resul} \n")
	error(resul,x)





	
	
	