basic_salary=int(input("enter basic_salary"))
if basic_salary<=10000:
    HRA=basic_salary*20/100
    DA=basic_salary*80/100
    gross_salary=basic_salary+HRA+DA
    print("gross_salary",gross_salary)
elif basic_salary<=20000:
    HRA=basic_salary*25/100
    DA=basic_salary*90/100
    gross_salary=basic_salary+HRA+DA
    print("gross_salary",gross_salary)
elif basic_salary>20000:
    HRA=basic_salary*30/100
    DA=basic_salary*95/100
    gross_salary=basic_salary+HRA+DA
    print("gross_salary",gross_salary) 
else:
    print("none")           