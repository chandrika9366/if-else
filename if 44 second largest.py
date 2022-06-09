a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a<b and a>c:
    print("a is second largest")
elif b<a and b>c:
    print("b is second largest") 
elif c>a and c<b:
    print("c is second largest")
else:
    print("not second largest")