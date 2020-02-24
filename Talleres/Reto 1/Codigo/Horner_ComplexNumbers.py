##Codigo del reto horner 1

import math
import cmath
import random

def horner(x, listaCoeficientes):
  resultado = 0
  for i in range(len(listaCoeficientes)):
    resultado = resultado * x + listaCoeficientes[i]
  #end for
  return resultado
    
#enddef

def derivar(listaCoeficientes):
  derivada= []
  coeficiente=0
  for i in range (0,len(listaCoeficientes)):
    coeficiente = listaCoeficientes[i]*(len(listaCoeficientes)-i-1)
    derivada.append(coeficiente)
  #endfor
  return derivada
#enddef


coeficientes = []
for i in range (10):
  coeficientes.append(random.randint(0,10))
#endfor

print("Arreglo de coeficientes de f(x): ",coeficientes)
print("Funcion F(x) evaluada en x = raiz(-1): ",horner(complex(0,1), coeficientes))
derivada = derivar(coeficientes)
derivada.pop()
print("Arreglo de coeficientes de f'(x): ", derivada)
print("Funcion F'(x) evaluada en x = raiz(-1): ",horner(complex(0,1), derivada))