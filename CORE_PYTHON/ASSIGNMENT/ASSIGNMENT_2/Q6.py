#### WAP to calculate total salary of employee based on basic, da=10% of basic,
## ta=12% of basic, hra=15% of basic.

basic_salary = int(input('Enter the basic salary : '))

da = basic_salary * 0.10
ta = basic_salary * 0.12
hra = basic_salary * 0.15

Total_salary = basic_salary + ta + hra + da

print(f'Total salary of employee is {Total_salary} rs.')