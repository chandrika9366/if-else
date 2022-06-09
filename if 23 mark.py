percentage=int(input("enter percentage"))
if percentage>=80 and percentage<=100:
    print("grade a")
elif percentage>=60 and percentage<80:
    print("grade b")
elif percentage>=50 and percentage<60:
    print("grade c")
elif percentage>=45 and percentage<50:
    print("grade d")  
elif percentage>=25 and percentage<45:
    print("grade e")  
else:
    print("grade f")                