## 4. WAP to print factorial of a number .

num = int(input('enter number : '))

i = 1
fact = 1

while(i <= num):
    fact = fact * i
    i = i + 1
print(f'factorial of {num} is {fact}')
