# ## 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n



# a. 1+ 2 + 3 + 4+..... + n

def num(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

n = int(input('Enter how many numbers you want : '))

res = num(n)

print(f'sum First {n} number is {res}')
                    

