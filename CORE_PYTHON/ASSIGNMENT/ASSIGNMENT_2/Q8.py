## Write a program to swap two numbers using third variable.

num1 = int(input('Enter Number x :'))
num2 = int(input('Enter Number y :'))
num3 = num2
num2 = num1
num1 = num3


print(f'''New value of x is {num1}
New value of y is {num2}''')
