## Write a program to check whether the triangle is equilateral, isosceles or scalene triangle

side1 = int(input('Enter A : '))
side2 = int(input('Enter B : '))
side3 = int(input('Enter C : '))

if side1 == side2 == side3 :
    print('it is equilateral triangle')
elif side1 == side2 or side2 == side3 or side3 == side1 :
        print('it is isosceles triangle')
else :
    print('it is scalene triangle')        