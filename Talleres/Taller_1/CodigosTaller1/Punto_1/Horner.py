import math
import random

def horner(x, listaCoeficientes):
  resultado = 0
  contador = 0
  for i in range(len(listaCoeficientes)):
    resultado = resultado * x + listaCoeficientes[i]
    contador = contador + 1
  #end for
  return resultado, contador
    
#enddef

coeficientes = []
for i in range(0, 10):
  print(coeficientes)
  print("resultado evaluado" ,horner(2, coeficientes),len(coeficientes))
  coeficientes.append(random.randint(0,15))



#endfor
