## 2. Write a program to check if given number is Armstrong or not using recursive
## function.

def chkarmstrong(n,pow):
    if n == 0:
        return 0
    
    d = n % 10
    return (d ** pow) + chkarmstrong(n // 10, pow)

num = int(input('Enter number : '))

pow = len(str(num))

if chkarmstrong(num, pow) == num:
    print('Armstrong number')
else:
    print('Not an Armstrong number')