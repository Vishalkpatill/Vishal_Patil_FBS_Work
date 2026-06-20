## Write a program to reverse a number using recursion.

def rev(n, r = 0):
    if n == 0:
        return r

    d = n % 10
    return rev(n // 10, r * 10 + d)

n = int(input("Enter number: "))
print(rev(n))
