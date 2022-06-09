month=input("enter month")
a=("january","march","may","july","august","october","december")
b=("april","june","september","november")
if month in (a):
   print("31days in month",month)
elif month in (b):
   print("30days in month",b) 
elif month in ("february"):
   print("28days in month","february")       
else:
   print("not month")      