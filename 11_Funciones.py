
def Operaciones(num1,num2): # definir funcion
	print "Serie de Operaciones entre ",num1," y ",num2
	print "Suma: ",num1," + ",num2," = ",num1+num2
	print "Resta: ",num1," - ",num2," = ",num1-num2
	print "Multiplicacion: ",num1," * ",num2," = ",num1*num2
	if num2 >0:
	   print "Division: ",num1," / ",num2," = ",num1/num2

print " "
Operaciones(0.4,67) # Llamar funcion
print " "
Operaciones(4,-27)
print " "
Operaciones(3,0)
print " "
Operaciones(4.4,14/7)
print " "
Operaciones(num2=0,num1=10)

print "\nLlamar la funcion\n"
for x in range(1,4):
	Operaciones(x,x+3) #Llamar funcion en un for y llenarlo


def NumeroColor(numero=10,color="Azul"): #funcion con parametros definidos
	print "Numero ",numero," y color ",color

print " "
NumeroColor(17,"Blanco") #llamar la funcion y reemplazar ambos valor
print " "
NumeroColor() # llamar funcion sin llamar valores
print " "
NumeroColor(12) #llamar funcion y reemplazar un valor
print " "
NumeroColor(color="Verde") # llamar funcion y especificar que valor reemplazar

def Indefinida(*args):
	print args # es una tupla o lista
	for x in args:
		print x

print "\n Funciones con parametros indefinidos \n"
Indefinida(1,2,354,566,False,"Texto",112.10)

def indefinidosFuntion(**kwargs):
	print kwargs
	for x in kwargs.items():
		print x


indefinidosFuntion(color="rojo",numeroP=120)

def functionIndefinidos(*args,**kwargs):
	# argumentos normales
	for x in args:
		print x
	
	# argumentos key-word (diccionario)
	for y in kwargs.items():
		print y

functionIndefinidos(1,23.4,23,"texto",False,colores="pan",numeropar=4578)


# funciones que retornan valores
print "\n funciones que retornan valores \n"	 		 	
def DobleMitad(numero1):
	return numero1*2,float(numero1)/2
		

print DobleMitad(5)

doble, mitad = DobleMitad(7)

print "\n doble \n ",doble
print "\n mitad  \n ",mitad