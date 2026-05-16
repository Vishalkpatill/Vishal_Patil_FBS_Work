## Find the sum of three-digit number.

num = int(input("Enter the number :"))

d1 = num // 100
num = num % 100

d2 = num // 10
num = num % 10

Total = d1 + d2 + num 

print(f'The addition of given number is {Total}.')