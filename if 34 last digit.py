num=int(input("enter num"))
last_digit=num%10
if last_digit%3==0:
    print(last_digit,"last_digit")
else:
    print(last_digit,"not last_digit")    