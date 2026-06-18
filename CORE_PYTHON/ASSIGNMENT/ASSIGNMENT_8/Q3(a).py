# 1!+ 2! + 3! + 4!+..... + n!

def chk_fact(n):

    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def sum_fact(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + chk_fact(i)
    return sum

num = int(input('Enter number : '))

res = sum_fact(num)

print(f'The sum of first {num} factorial is {res}')