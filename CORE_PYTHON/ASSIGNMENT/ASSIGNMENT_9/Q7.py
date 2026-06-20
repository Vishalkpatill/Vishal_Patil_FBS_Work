## Write a program to print Fibonacci series using recursion.

def sum(n,l=0):
    if n == 0:
        return l
    d = n % 10
    return sum(n // 10, l + d)

n = int(input('Enter number : '))

print(sum(n))

