 
def paltolist(pal):
    aux = []
    for i in pal:
        aux.append(i)
    return aux
 
def ana(pallist):
    laux = []
    if (len(pallist) == 1):
        laux.append(pallist.pop())
    else:
        for i in pallist:
            laux1=[]
            laux1=pallist[:]
            laux1.remove(i)
            laux2=ana(laux1)
            for j in laux2:
                laux.append(i+j)
    return laux
 
def main():
    pal = raw_input("Ingrese palabra: ")
    anas = ana(paltolist(pal))
    print "Los anagramas posibles son: \ ",anas
    print "La cantidad es: ",len(anas)
 
main()