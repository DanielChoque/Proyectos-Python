# coding=utf-8

class Persona:

	"""docstring for ClassName"""
	#Inicializadora
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad
		print "Usuario creado: ",nombre,edad
	#Metodos de clase
	def ValidarEdad(self):
		if self.edad >= 18:
			print "Es mayor de edad"
			return True
		else:
			print "NO es mayor de edad"
			return False
	def Aniversario(self):
		print "\n",self.nombre,u"\nCSSumple años"
		self.edad += 1
	#Metodo destructor	
	def __del__(self):
		print "borrando objeto de clase persona",self.nombre


Usuarios = Persona("Esteban",21)
print " "
print Usuarios.nombre
print " "
print Usuarios.edad

Usuarios.nombre = "Camila"
Usuarios.edad = 18

print " "
print Usuarios.nombre
print " "
print Usuarios.edad
print " "
Usuarios.ValidarEdad()

EsMayor = Usuarios.ValidarEdad()

print EsMayor
del(Usuarios)

User = Persona("Maria Camila Rios Villabona",17)
User.ValidarEdad()
User.Aniversario()
User.ValidarEdad()

print type(User)
#Metodo para saber el nombre de la clase en el objeto
print "Nombre de la clase: ",User.__class__.__name__