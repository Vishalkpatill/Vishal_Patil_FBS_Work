## Sum of all prime numbers between 1 to n

def chk_prime(n):
    if n <= 1:
     return False
         
    for i in range(2, n // + 1):
        if n % i == 0:
            return False
    else:
        return True

def sum_prime(num):
    sum = 0
    for i in range(1, num + 1):
        if chk_prime(i):
            sum = sum + i

    return sum

num = int(input('Enter number : '))

res = sum_prime(num)

print(f'Addition of first {num} prime number is {res}')
