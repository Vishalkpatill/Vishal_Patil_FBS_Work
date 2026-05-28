## WAP to check if given number is Perfect Number.

num = int(input('enter a number : '))

i = 1
sum = 0

while(i < num ):
    if num % i == 0:
        sum = sum + i
    i = i + 1

if sum == num:
    print(f'{num} is a perfect number ')
else:
    print(f'{num} is not perfect number ')        