# coding=utf-8

class Ejemplo:

	def __init__(self):
		self.__oculto = "soy atributo privado" # definir atributo privado

	def Publico(self):
		return "Soy un metodo publico"

	def __Privado(self):# definimos el metodo privado " __ "
		print "estoy cambiando el valor del atributo"
		#return "soy un metodo privado"

	def get_oculto(self):
		return self.__oculto

	def set_oculto(self):
		self.__oculto = self.__Privado()
		
#Instaciamos un objeto de la clase ejemplo
Objeto = Ejemplo()
#intentamos acceder al metodo publico
print (Objeto.Publico())
print " "
#intentamos acceder al metodo privado INCORRECTA
#print (Objeto.__Privado())
# intentamos acceder al metodo privado CORRECTA con NAME MANGLING
#print (Objeto._Ejemplo__Privado())

#obtener acceso al atributo privado
#print (Objeto.get_oculto())

# cambiar el valor del atributo privado
Objeto.set_oculto()