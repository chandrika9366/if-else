i=int(input("enter num"))
j=int(input("enter num"))
k=int(input("enter num"))
if i<j:
  if j<k:
    i=j
  else:
      j=k
else:
    if j>k:
        j=i
    else:
        i=k
print(i,j,k)                        