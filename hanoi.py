#Torres de Hanoi en Python JGT(MIT)
 
class Hanoi:
         #atributos de la clase.
        tot = 0
        discos = 0
        origen = ""
        intermedio = ""
        destino = ""
       
        #Constructor de la clase que inicializa los atributos de la clase con
        #los valores recibidos.
        def __init__(self,discos, origen, intermedio, destino):
                self.discos = discos
                self.origen = origen
                self.intermedio = intermedio
                self.destino = destino
 
        #Metodo que imprime los movimientos.
        def moverHanoi(self,discos,origen, intermedio, destino):
                print "Moviendo ", discos," disco de torre: " , origen , " a la " , "torre: " , destino
                self.tot +=1
               
        #Metodo en que recorremos el numero de discos recibidos para poder
        #posteriormente ordenarlos.
        def doHanoi(self):     
                for i in range(1, self.discos+1):
                        if i == 1:
                                self.moverHanoi(i, self.origen, self.destino, self.intermedio)
                        else:
                                self.moverHanoi(i, self.origen, self.destino, self.intermedio) 
                                self.moverHanoi(i, self.intermedio, self.origen, self.destino)
 
                                                               
 
print'hola,bienvenido al juego de las torres de Hanoi desde python'
discos=int(raw_input("ingresa num de discos..."))
 
#Creamos un nuevo objeto de la clase Hanoi llamado: mi_hanoi, le pasamos
#el numero de discos recibidos y los valores A B y C.
mi_hanoi = Hanoi(discos,'A','B','C')
 
if discos>0:
#llamamos el metodo doHanoi() de nuestro objeto mi_hanoi
    mi_hanoi.doHanoi()
else:
    print'las torres de hanoi no se pueden jugar sin discos'
 
#Accedemos al numero total de mon
print'hiciste ',mi_hanoi.tot,'movimientos'
raw_input()