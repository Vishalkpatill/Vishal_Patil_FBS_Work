## Sum of all odd numbers between 1 to n

def odd(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            sum = sum + i
    return sum

n = int(input('Enter number : '))

res = odd(n)

print(f'Addition of First {n} odd number is {res}')
