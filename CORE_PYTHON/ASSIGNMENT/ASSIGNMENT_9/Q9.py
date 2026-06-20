## Write a program to calculate the m to the power n using recursion.


def pow(m, n):
    if n == 0:
        return 1
    return m * pow(m, n - 1)

m = int(input('Enter (m): '))
n = int(input('Enter (n): '))

print(pow(m,n))