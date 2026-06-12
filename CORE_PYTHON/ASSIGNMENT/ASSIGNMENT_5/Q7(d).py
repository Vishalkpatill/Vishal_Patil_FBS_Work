## d. S = a + a2/2 + a3/3 + ...... + a10/10

a = 2 
sum = 0

for i in range(1, 11):
    x = a * (i//i)
    sum = sum + x

print(sum)