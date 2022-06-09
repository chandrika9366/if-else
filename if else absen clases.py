classes=int(input("enter classes"))
absent_day=int(input("enter absent_day"))
working_day=classes-absent_day
percentage=working_day/classes*100
if percentage>=75:
    print("allow",percentage)
else:
    print("not allow",percentage)