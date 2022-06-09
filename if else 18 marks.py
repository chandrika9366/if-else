physis=int(input("enter physis"))
chemistry=int(input("enter chemistry"))
biology=int(input("enter biology"))
mathematics=int(input("enter mathematics"))
computer=int(input("enter compur"))
total=physis+chemistry+biology+mathematics+computer
percentage=total/500*100
if percentage>=90 and percentage<=100:
    print("grade a")
elif percentage>=80 and percentage<=90:
    print("grade b") 
elif percentage>=70 and percentage<=80:
    print("grade c") 
elif percentage>=60 and percentage<=70:
    print("grade d")
elif percentage>=40 and percentage<=60:
    print("grade e")
else:
    print("grade f")                  