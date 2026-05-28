## 12. Write a program to check if given number is Armstrong number or not.
## (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
## 4*4*4*4)

num = int(input('enter number : '))

temp = num 
arm = 0
pow = len(str(num))

while(num > 0):
    rem = num % 10
    arm = arm + (rem**pow)
    num = num // 10

if temp == arm:
    print(f'{temp} is a armstrong number')

else:
    print('number is not armstrong number')
