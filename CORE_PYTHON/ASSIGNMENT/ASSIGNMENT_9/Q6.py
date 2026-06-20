# Write a program to print Fibonacci series using recursion.

def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)
    
num = int(input('Enter number : '))

for i in range(num):
    print(fibb(i), end = ' ')