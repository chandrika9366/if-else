a=int(input("enter a"))
b=int(input("enter b"))
operator=input("enter operator")
if operator=="+":
    print(a+b,"it is addition num")
elif operator=="-":
    print(a-b,"it is subtraction num") 
elif operator=="*":
    print(a*b,"it is multiply num") 
elif operator=="/":
    print(a/b,"it is devide num") 
elif operator=="**":
    print(a**b,"it is exponents num") 
elif operator=="%":
    print(a%b,"it is modulus num")
elif operator=="//":
    print(a//b,"it is floor num")
else:
    print("it is not operator")                        