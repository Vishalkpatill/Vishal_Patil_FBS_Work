## b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n = int(input('Enter number : '))
sum = 0


for i in range(1, n + 1):
    x = n ** i
    sum = sum + x

print(sum)