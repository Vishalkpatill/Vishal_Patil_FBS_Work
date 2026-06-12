## # c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# 2 + 4 + 8 + 16
n = int(input('Enter number : '))

sum = 0
for i in range(0, n):
    sum = sum + 2 ** i

print(sum)    