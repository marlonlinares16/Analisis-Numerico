import math
import mpmath


#DEFINE VARIABLES (sin(x) and it's derivatives)
def f1(x):
  return math.sin(x)

def f2(x):
  return math.cos(x)

def f3(x):
  return -math.sin(x)

def f4(x):
  return -math.cos(x)

#define iterator for entering while
i=0
n = 1
result = 0
#define level of tolerance
tolerancy = 0.0000000000000001
#define theoric value of function desired
teoric = math.sin(math.pi/64)
#initialize lists
results = []
absError = []
relError = []
value = -math.pi/64

#start while loop
while (abs(teoric-result)) > tolerancy:
  
  results.insert(i,result)
  absError.insert(i,abs(teoric-result))
  if result != 0:
    relError.insert(i,(absError[i]/result)*100)
  else:
    relError.insert(i, 0)
  if n%4 == 3:
    result = result + f2(0) * pow(value, n)/math.factorial(n)  
  
  if n%4 == 2:
    result = result + f3(0) * pow(value, n)/math.factorial(n)
  
  if n%4 == 1:
    result = result + f4(0) * pow(value, n)/math.factorial(n) 
  
  if n%4 == 0:
    result = result + f1(0) * pow(value, n)/math.factorial(n) 
  i+=1
  n+=1
  print(abs(teoric-result))


results[i-1]=result
absError[i-1]=abs(teoric-result)
relError[i-1]=(absError[i-1]/result)*100
relError[0]=1



print ("teorico \t\t\t\tresultados \t\t\t\terror relativo")
for x,y in zip(results, relError):
  print (teoric, x, y)
print("# iteraciones:", n-1)
