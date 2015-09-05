
# condicionales if else

# if clasico
nota = 10
if nota == 10:
	print "Excelente"

# if-else
nota = 15
if nota >= 0 and nota <=10:
	print "\n\n\tExcelente ",nota
else:
	print "\n\n\n\t La nota no es valida",nota

print" "
#if-elif-else
nota = 2
if nota ==10:
	print "Excelente"
elif nota == 9:
	print "Sobresaliente"
elif nota <9 and nota >=6:
	print "Aceptable"
elif nota <=5 and nota >2:
	print "Insuficiente"
else:
	print "Deficiente"


print " "
nota = 54
if nota == 8 or nota ==7:
	if nota == 8:
		print "es: ",nota
	elif nota == 7:
		print "Es: ",nota
else:
	print "No es ni 8 ni 7"