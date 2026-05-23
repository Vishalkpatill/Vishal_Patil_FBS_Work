## Write a program to calculate profit or loss

cp = int(input('Enter cost price : '))
sp = int(input('Enter sellilng price : '))

profit = (sp - cp)

loss = (cp - sp)

if cp < sp :
    print(f'Profit is {profit}')
else :
    print(f'Loss is {loss}')