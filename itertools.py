from itertools import *

for i in count(3):
	print(i)            #count cuenta infinitamente desde un numer

	if i>= 100:
		break

lista=[1,4,5,9,34,2,5,3,453,6,832,5344,1,7,5]

for i in cycle(lista):
	print(i)

	if i>= 100:
		break


palabra= "pollas"                 
for i in repeat(4):
	print(i)            

	if i>= 6:
		break

	