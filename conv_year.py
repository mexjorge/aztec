# -*- coding: utf-8 -*-
def ly(valor):
    pot= 9.46 * 12**10
  return valor * 9.46 * 10**12 
  
  
  
valor = input("Ingrese la cantidad de años luz:")
print "Usted ingreso: %f" % valor
valor=ly(valor)


print ("%f"%valor) 
print valor
