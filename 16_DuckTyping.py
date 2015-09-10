
#Ejemplo 1 wikipedia

class Pato:
    def parpar(self): 
        print "Cuac!"
    def plumas(self): 
        print "El pato tiene plumas blancas y grises."
 
class Persona:
    def parpar(self):
        print "La persona imita el sonido de un pato."
    def plumas(self): 
        print "La persona toma una pluma del suelo y la muestra."
 
def en_el_bosque(pato):
    pato.parpar()
    pato.plumas()
 
def juego():
    donald = Pato()
    juan = Persona()
    en_el_bosque(donald)
    en_el_bosque(juan)

juego()

print "\n\n"

# Ejemplo 2 Tutorial

class Bomb:
    def __init__(self):
        ""

    def talk(self):
        self.explode()

    def explode(self):
        print "BOOM!,the bomb explodes"


class Duck:
    
    def __init__(self):
        ""

    def talk(self):
        print " i am a duck , i will not blow up if you ask me to talk."


class Kid:
    Kids_ducks = None

    def __init__(self):
        print "kid comes around a corner and asks you for money so he could buy a duck"

    def takeDuck(self,duck):
        self.Kids_ducks = duck
        print "the kid accepts the duck, and happily skips along"

    def doYourThing(self):
        print "the kid trie to get the duck to talk"
        self.Kids_ducks.talk()


myKid= Kid()

myBomb = Bomb()
myDuck = Duck()
myKid.takeDuck(myDuck)
#myKid.takeDuck(myBomb)
myKid.doYourThing()