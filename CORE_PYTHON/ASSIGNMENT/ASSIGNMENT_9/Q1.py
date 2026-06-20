# write a program to find sum of following series using recursive function
## 1! + 2! + 3! + 4! ..... + n!

def chkfact(n):
    if n == 0 or n == 1:
        return 1
    return n * chkfact(n - 1)

def sum_fact(n):
    if n == 1:
        return 1
    return chkfact(n) + sum_fact(n - 1)

n = int(input('Enter Number: '))

print(sum_fact(n))