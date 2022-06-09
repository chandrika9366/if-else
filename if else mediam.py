a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
if a<=b and a>=c:
   print("it is median num",a) 
elif b>=a and b<=c:
   print("it is median num",b) 
elif c<=a and c>=b:
   print("it is median num",c)
else:
   print("not median")  