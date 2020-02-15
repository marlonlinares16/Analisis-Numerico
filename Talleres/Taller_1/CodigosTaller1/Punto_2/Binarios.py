
import math 
def base10abinario(numero, numeroBits):
  entero= int(numero)
  decimal=abs(numero) - abs(int(numero))
  contador=0
  #decimal=(float("{0:.2f}".format(decimal)))
  binarioParteentera="."
  binarioParteDecimal=""
  while entero!=0 and contador!=numeroBits:
    if entero % 2 == 0:
      binarioParteentera='0'+binarioParteentera
    else:
      binarioParteentera= '1'+ binarioParteentera
    entero= entero//2
    contador+=1
  while contador!=numeroBits:
    decimal=decimal*2
    contador+=1
    if decimal>1:
      decimal=decimal-1
      binarioParteDecimal=binarioParteDecimal+'1'
    else:
      binarioParteDecimal=binarioParteDecimal+'0'
  print(binarioParteentera+ binarioParteDecimal)

def binarioabase10(numero):
  numero= str(numero)
  numeroB=0
  parteEntera, partedecimal= numero.split('.')
  max=len(parteEntera)-1
  for i in parteEntera:
    num= int(i)* 2**max
    max-=1
    numeroB+=num
  max=1
  for u in partedecimal:
    numeroB+= int(u)*(1/ 2**max)
    max+=1
  print(numeroB)
  print(parteEntera+"brber"+partedecimal)
  return 0
base10abinario(math.pi,15)
binarioabase10(1101.1011)