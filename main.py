import math
a=int(input("ingresa el primer numero"))
b=int(input("ingresa el segundo numero"))
c=int(input("ingresa el tercer numero"))

d=(b*b-4*a*c)
if a!=0:
     if d<0:
         print(" las raices son imaginarias")
     else:
         x1=(-b+(math.sqrt(d)))/(2*a)
         x2=(-b-(math.sqrt(d)))/(2*a)
         print("x1 = {} x2= {}".format(x1,x2))
else:
    print("coefeiciente a debe ser diferente de 0")
    
               
               
