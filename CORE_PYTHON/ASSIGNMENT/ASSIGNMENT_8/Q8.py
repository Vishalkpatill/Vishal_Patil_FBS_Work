## Write a program find reverse of a number

def rev(n):
    temp = n
    sum = 0 
    while temp > 0:
        d = temp % 10
        sum = sum * 10 + d
        temp = temp // 10
    return sum

n = int(input('Enter number : '))

res = rev(n)

print(f'Reverse number is {res}')

