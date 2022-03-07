from bintreeFile import Bintree
from linkedQFile import LinkedQ


gamla= Bintree()
ordlistan = Bintree()
q=LinkedQ()
s=LinkedQ()

class Klar(Exception):
    def __init__ (self):
        pass
class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
    
    def getword(self):
        return self.word
        
    def getparent(self):
        return self.parent
    
    def __str__(self):
        return self.word

def makechildren(startord,slutord):
        alfabetet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
        for i in range(len(alfabetet)):
            startordet=ParentNode.getword(startord)
            förstabokstav= alfabetet[(i)] + startordet[1] + startordet[2]
            if förstabokstav in ordlistan:
                if förstabokstav not in gamla:
                    gamla.put(förstabokstav)
                    objekt_ett=ParentNode(förstabokstav, startord)
                    q.enqueue(objekt_ett)
                    if förstabokstav == slutord:						
                        writechain(objekt_ett)
                        raise Klar
                

            andrabokstav= startordet[0]+ alfabetet[i]+ startordet[2]
            if andrabokstav in ordlistan:
                if andrabokstav not in gamla:
                    gamla.put(andrabokstav)
                    objekt_två=ParentNode(andrabokstav, startord)
                    q.enqueue(objekt_två)
                    if andrabokstav ==slutord:						
                        writechain(objekt_två)
                        raise Klar

            tredjebokstav= startordet[0] + startordet[1] + alfabetet[i]
            if tredjebokstav in ordlistan:
                if tredjebokstav not in gamla:
                    gamla.put(tredjebokstav)
                    objekt_tre=ParentNode(tredjebokstav, startord)
                    q.enqueue(objekt_tre)
                    if tredjebokstav == slutord:						
                        writechain(objekt_tre)
                        raise Klar



#När makechildren finner slutordet ska den skriva ut hela kedjan genom ett anrop writechain(slutordsnod).
# Metoden writechain() ska skrivas rekursivt, så att man får ut kedjan med slutordet sist.

def writechain(slutord):
    if slutord.parent is None:
        print(slutord.word)
    else:
        writechain(slutord.parent)
        print(slutord.word)


def main():
    with open("/Users/Fabian/Documents/DataOptimering/Labb4/word3.txt", "r", encoding = "utf-8") as ordfil:
        for rad in ordfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet not in ordlistan:
                ordlistan.put(ordet)           # in i sökträdet
    
    start_ord=input("Välj ditt startord: ")
    slutord= input("välj ditt slutord: ")
    startord=ParentNode(start_ord,None)
    q.enqueue(startord)
    try:
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod, slutord)
        print("Det finns tyvär ingen väg")
    except Klar:
        print(" ")

main()
            
