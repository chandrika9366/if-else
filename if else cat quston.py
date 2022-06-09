cat1=int(input("enter cat1"))
mouse=int(input("enter mouse"))
cat2=int(input("enter cat2"))
if cat1<mouse and mouse<cat2:
   print("cat1")
elif cat2<mouse and mouse<cat1:
   print("cat2")
elif cat1>mouse and cat2>mouse:
   print("mouse")
else:
   print("none")    