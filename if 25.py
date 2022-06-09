attendence=int(input("enter attendence"))
classes=int(input("enter classes"))
percentage=attendence/classes*100
if percentage>=75:
    print(percentage,"student allow to sit the exam")
else:
    print(percentage,"student not allow to sit the exam ")        