def problema2(n,E,x):
  y= (1/2)*(x+(n/x))
  while(abs(x-y)>E):
    x=y
    y= (1/2)*(x+ (n/x))
  return y 
print(problema2(7,0.210,2.6))
  
