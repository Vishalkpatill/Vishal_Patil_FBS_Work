## 11. WAP to check if given number Strong Number.

n = int(input('enter number : '))

temp = n
sum  = 0

while(temp > 0):
    d = temp % 10

    fact = 1 
    i = 1 

    while(i <= d):
        fact = fact * i
        i = i + 1
    
    sum = sum + fact
    temp = temp // 10

if sum == n:
    print(f'{n} is a strong number')

else:
    print(f'{n} is not a strong number')
    