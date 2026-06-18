## Write a program to calculate area of rectangle

def rect(len , bre):
    area = len * bre
    return area

len = int(input('Enter length : '))
bre = int(input('Enter breadth : '))

res = rect(len, bre)

print(f'Area of rectangle is {res}')