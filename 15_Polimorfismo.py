# coding=utf-8

class A:
	def Mensaje(self):
		print "Hola soy de la clase A"


class B:
	def Mensaje(self):
		print "Hola soy de la clase B"



def Saludar(Objeto):
	Objeto.Mensaje()


a = A()
b = B()

Saludar(a)
Saludar(b)