import os
import random
archivo=open('100000 números aleatorios.txt','w')
lista_aleatorios=[]
 
 
for i in range(1,100000):
  i=random.randint(1,100000)
  lista_aleatorios.append(i)

archivo.write(str(lista_aleatorios))
archivo.close()