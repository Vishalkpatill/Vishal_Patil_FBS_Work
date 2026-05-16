###  Write a program to calculate the percentage of student based on marks of any 5 subjects

num1 = int(input('Marathi: '))
num2 = int(input('Hindi: '))
num3 = int(input('English: '))
num4 = int(input('Math: '))
num5 = int(input('Drawing: '))

Total_marks = num1 + num2 + num3 + num4 + num5 

Total_percent = Total_marks / 5

print(f'{Total_percent} % ')