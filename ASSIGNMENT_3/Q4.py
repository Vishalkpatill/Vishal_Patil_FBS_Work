## Write a program to input all sides of a triangle and check whether triangle is valid or not

side1 = int(input('Enter side 1 : '))
side2 = int(input('Enter side 2 : '))
side3 = int(input('Enter side 3 : '))

if (side1 + side2) > side3 and (side2 + side3) > side1 and (side3 + side1) > side2 :
    print('triangle is valid')
else :
    print('triangle is not valid')            


