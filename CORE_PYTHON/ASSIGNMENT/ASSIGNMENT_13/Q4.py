# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

def genNum(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = i * i
    return d

n = int(input('Enter numeber : '))

res = genNum(n)

print(res)
    




