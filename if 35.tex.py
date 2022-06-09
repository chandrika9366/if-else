cost_price=int(input("enter num"))
if cost_price>100000:
    tex=cost_price*15/100
    print("tex",tex)
elif cost_price>50000 and cost_price<=100000:
    tex=cost_price*10/100
    print("tex",tex)
elif cost_price<=50000:
    tex=cost_price*5/100
    print("tex",tex)  
else:
    print("not tex")      