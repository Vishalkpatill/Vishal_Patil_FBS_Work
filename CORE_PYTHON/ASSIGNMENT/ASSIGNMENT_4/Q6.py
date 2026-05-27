## WAP to check if a given number is prime number or not.

n = int(input('enter number : '))

i = 1
count = 0

while (i <= n):
    if n % i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print('It is a prime number')

else:
    print('it is not prime number')