## Write a program to find sum of digits of a number.

def sum_digit(n):
    temp = n
    sum = 0
    while temp > 0:
        d = temp % 10
        sum = sum + d
        temp = temp // 10
    return sum 

n = int(input('Enter number : ')) 

res = sum_digit(n)

print(f'Sum of {n} is {res}')