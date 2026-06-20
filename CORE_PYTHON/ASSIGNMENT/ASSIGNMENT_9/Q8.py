## 8. Write a program to check whether a number is prime or not using recursion.

def chkprime(n, i = 2):
    if n <= 1:
        return False
    
    if i == n:
        return True
    
    if n % i == 0:
        return False
    
    return chkprime(n, i + 1)

num = int(input('Enter number : '))

if chkprime(num):
    print('Prime number')
else:
    print('Not prime number')