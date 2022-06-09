month=input("enter month")
day=int(input("enter day"))
if month in ("dec","jan","feb"):
   if day>=28 or day<=31:
      print("winter")
elif month in ("mar","apr","may"):
   if day>=30 or day<=31:
      print("spring")
elif month in ("june","july","aug"):
    if day>=30 or day<=31:
       print("summer")
elif month in ("sep","oct","nov"):
    if day>=30 or day<=31:
       print("autumn")
else:
    print("none")      