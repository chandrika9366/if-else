age=int(input("enter age"))
gender=input("enter age")
day=int(input("enter day"))
if age>=18 and age<30 and gender=="m":
   wage=day*700
   print("wage",wage)
elif age>=18 and age<30 and gender=="f":
   wage=day*750
   print("wage",wage)
elif age>=30 and age<=40 and gender=="m":
   wage=day*800
   print("wage",wage)
elif age>=30 and age<=40 and gender=="f":
   wage=day*850
   print("wage",wage)
else:
   print("none")                  