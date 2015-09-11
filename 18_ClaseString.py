
cadena = raw_input("Ingresa el texto: ")

#Longitud de la cadena
print "\nLongitud de la cadena",len(cadena)

# devuelve true si la cadena solo contiene letras
if cadena.isalpha():
	print "\nla cadena contiene solo letras"


# devuelve true si la cadena solo contiene numeros
if cadena.isdigit():
	print "\nla cadena contiene solo numeros"


# convierte la cadena a MAYUSCULAS
print "\nla cadena en MAYUSCULAS es: ",cadena.upper()

# convierte la cadena a minisculas
print "\nla cadena en minisculas es: ",cadena.lower()

# convierte mayuscuslas a minisculas o viceverza 
print "\nInvierte minisculas y MAYUSCULAS",cadena.swapcase()

# reemplaza
print "\nreemplaza a por x",cadena.replace("a","X")

#Devuelve la posicion del caracter solicitado (la primera incidencia)
print "\nla posicion del caracter solicitado es: ",cadena.find("a")

#Devuelve la posicion del caracter solicitado (la ultima incidencia)
print "ultima posicion"
print "\nla posicion del caracter solicitado es: ",cadena.rfind("a")

# crea una lista de sub-cadenas de la cadena
print "\nLista de sub-cadenas: ",cadena.split("a")
