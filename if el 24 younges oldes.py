age1=int(input("enter age1"))
age2=int(input("enter age2"))
age3=int(input("enter age3"))
if age1>age2 and age1>age3:
    print("age1 oldest")
elif age2>age1 and age2>age3:
    print("age2 oldest") 
elif age3>age1 and age3>age2:
    print("age3 oldest") 
if age1<age2 and age1<age3:
    print("age1 youngest") 
elif age2<age1 and age2<age3:
    print("age2 youngest") 
elif age3<age1 and age3<age2:
    print("age3 youngest")
else:
    print("all are equal")                    