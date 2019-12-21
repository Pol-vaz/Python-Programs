

numeros=[17,24,7,39,8,51,92]                    #con lambda

print(list(filter(lambda par: par%2==0, numeros)))

#*******************************************************************************************************************************************************************

class empleado:

	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)


listaempleados = [

empleado("juan","Director",750000),
empleado("Ana","prostituta",90000),
empleado("Antonio","Administrativo",60000),
empleado("Sara","Secretaria",27000),
empleado("Mario","Botones",21000)
]

salarios_alto=filter(lambda empleado : empleado.salario > 50000,listaempleados )

for empleado_salario in salarios_alto:

	print(empleado_salario)