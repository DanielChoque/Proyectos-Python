# coding=utf-8

# Clase libro
class Libro:
	"""docstring for Libro"""
	def __init__(self,isbn,titulo,autor):
		self.isbn = isbn
		self.titulo = titulo
		self.autor = autor

	def Info(self):
		print "\n\n#####"
		print "ISBN: ",self.isbn
		print u"Título: ",self.titulo
		print "Autor: ",self.autor
		print "#####"

	def Disponibilidad(self):
			print self.titulo,u" está disponible"


book = Libro("998-3-100-300","La iliada","Zeus")
book.Info()
book.Disponibilidad()

#Clase ebook hereda de libro
class Ebook(Libro):
	def Otorgar_Enlace(self,enlace):
		self.enlace = enlace

	def Otorgar_tamano(self,tamano):
		self.tamano = tamano

	def Info(self):
		print "\n\n#####"
		print "ISBN: ",self.isbn
		print u"Título: ",self.titulo
		print "Autor: ",self.autor
		print "Enlace: ",self.enlace
		print u"Tamaño: ",self.tamano,"KB"
		print "#####"

Newbook = Ebook("998-3-100-300","La iliada","Zeus")

Newbook.Otorgar_Enlace("http://LibrosWeb.com/01")
Newbook.Otorgar_tamano(1899)
Newbook.Info()
Newbook.Disponibilidad();

#Clase LibroPapel que hereda libro

class LibroPapel(Libro):

	peso = 0
	stock = 0

	def Otorgar_peso(self,peso):
		self.peso = peso

	def Otorgar_stock(self,stock):
		self.stock = stock

	def Disponibilidad(self):
		if self.stock >0:
			print self.titulo,u" sí esta disponible"
		else:
			print self.titulo,u"NO está disponible"


	def Info(self):
		print "\n\n#####"
		print "ISBN: ",self.isbn
		print u"Título: ",self.titulo
		print "Autor: ",self.autor
		print "Peso: ",self.peso,"Gramos"
		print u"Stock: ",self.stock,"Unidades"
		print "#####"
				

Paperbook = LibroPapel("998-3-100-300","La iliada","Zeus")
Paperbook.Info()
Paperbook.Disponibilidad();
Paperbook.Otorgar_peso(2000)
Paperbook.Otorgar_stock(10)
Paperbook.Info()
Paperbook.Disponibilidad();
