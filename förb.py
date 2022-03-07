
def utskrift(lista):
    if len(lista) > 0:
        print(lista[0])
        utskrift(lista[1:])
        

list = [1,2,3,4,5]
utskrift(list)
------------------------------------------------------------------------------------------------------------
def utskrift([1,2,3,4,5]):                                  
    if len(lista) > 0:                                                                      
        print(lista[0])                                                  
        utskrift(lista[1:])

"Print ordning":
print(1)

def utskrift([2,3,4,5]):                                  
    if len(lista) > 0:                                                                      
        print(lista[0])                                                  
        utskrift(lista[1:])    
"Print ordning":                                    
print(1)
print(2)


def utskrift([3,4,5]):                                  
    if len(lista) > 0:                                                                      
        print(lista[0])                                                  
        utskrift(lista[1:])
"Print ordning":
print(1)
print(2)
print(3)

def utskrift(4,5]):                                  
    if len(lista) > 0:                                                                      
        print(lista[0])                                                  
        utskrift(lista[1:])
"Print ordning":
print(1)
print(2)
print(3)
print(4)
def utskrift([5]):                                  
    if len(lista) > 0:                                                                      
        print(lista[0])                                                  
        utskrift(lista[1:])
"Print ordning":
print(1)
print(2)
print(3)
print(4)
print(5)