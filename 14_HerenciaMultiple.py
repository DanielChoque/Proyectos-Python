# coding=utf-8
class A:
	
	def Hola(self):
		print " Hola soy A"

	def a(self):
		print "Soy de A"


class B:
	
	def Hola(self):
		print "Hola soy B"

	def b(self):
		print "Soy de B"


class C(B,A): # Tiene prioridad el parametro de la izquierda
	def Hola(self):
		print "Hola soy C"

	def c(self):
		print "Soy de C"


c = C();
c.Hola()

class D(B,C,A):

	def d(self):
		print "Soy de D"
	

d = D()
d.Hola()
d.a()
d.b()
d.c()
d.d()
	
		
