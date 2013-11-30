# -*- coding: utf-8 -*-
def factorial(n):
        if n==0:
                return 1
        resultado=n*factorial(n-1)
        return resultado
 
cont=0
while cont==0:
        numero= int(input('Inserte el número al cual desea calcular el factorial: '))
        print(factorial(numero))
        pregunta=int(input('¿Desea calcular otro factorial? Si = (1) No = (2) : '))
        if pregunta==2:
                cont=1