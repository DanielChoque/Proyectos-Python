
Lista = []

print len(Lista)

Lista = [0,False,"Hola Mundo",[5,4,3,2,145]]

print Lista #Mostrar todos los datos de la lista

print Lista[0],type(Lista[0]) # Mostrar la primera posicion de la lista

print Lista[2],type(Lista[2]) #Mostrar la tercea posicion de la lista

print Lista[3],type(Lista[3])#Mostrar la cuarta posicion de la lista

print Lista[3][1],type(Lista[3][1])# Mostrar la cuarta posicion de la lista y dentro de la lista la posicion dos

Lista[0]=17 #reemplazar el valor de una lista

print Lista
print "\n Ultimo elemento de la lista \n"
print Lista[-1] # Ultimo elemento o posicion de la lista
print "\n Ultimo elemento de la lista dentro otra lista \n"
print Lista[-1][-1] # Ultimo elemento o posicion de la lista dentro otra lista

Listado = ['A','B','C','D','E']
print "\n Imprimir un rango de posiciones de la lista \n"
print Listado[1:4]

Listados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print "\n Imprimir un rango de posiciones de la lista de numeros \n"
print Listados[0:4] #entre
print Listados[9:] # con inicio
print Listados[:10] # sin inicio pero con limite
print Listados[1::2]# con salto de 2
print Listados[::3]# con salto de 3
print "\n voltear una lista \n"
print Listados[::-1] # voltear la lista