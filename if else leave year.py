year=int(input("enter year"))
if year%4==0:
    if year%100!=0 or year%400==0:
     print("it is leap year")
    else:
        print("not leap year")
else:
   print("simple year")  