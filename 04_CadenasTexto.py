# coding=utf-8
cadena = "texto"

print cadena,type(cadena)

cadena = u" á ñ é" #Caracteres especiales 

print cadena,type(cadena)

cadena = "\n Linea 1 \n\tLinea 2 \n\n\t\t Linea 3"

print cadena

cadena = r"\n Linea 1 \n\tLinea 2 \n\n\t\t Linea 3" # tipo raw 

print cadena

cadena = """  esta cadena interpreta 

saltos de 
 				linea 

 					y Caracteres especila como 

 					la ñ o é á 

 					prueba 


""" # cadena que interpreta saltos de linea y algunos caracteres especiales

print cadena
print " \n"
cadena1 = "Hola"
cadena2 = "Mundo"

print cadena1 + cadena2

print " \n"
cadena1 = "Hola"
cadena2 = " Mundo"

cadena3 = cadena1 + cadena2

print cadena3 #concatenacion de strings

cad_esp = "**"

print cad_esp * 3 + cadena1 # operaciones con string