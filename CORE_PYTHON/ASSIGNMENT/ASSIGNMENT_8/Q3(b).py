## 1^1 + 2^2 + 3^3+ ...... n^n

def chk_pwr(n):
    power = 1
    for i in range(1, n+1):
        power = i ** i
    return power

def sum_pwr(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + chk_pwr(i)
    return sum

num = int(input('Enter number : '))

res = sum_pwr(num)

print(res)