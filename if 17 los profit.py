actual_cost=int(input("enter actual_cost"))
selling_cost=int(input("enter selling_cost"))
if actual_cost<selling_cost:
    print(selling_cost,"profit")
elif actual_cost>selling_cost:
    print(actual_cost,"loss")    
else:
    print("no lost no profit")    