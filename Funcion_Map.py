
class empleado:

	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)


listaempleados = [

empleado("juan","Director",6700),
empleado("Ana","prostituta",7500),
empleado("Antonio","Administrativo",2100),
empleado("Sara","Secretaria",2150),
empleado("Mario","Botones",1800)
]

def calculo_comision(empleado):

	empleado.salario= empleado.salario * 1.03
