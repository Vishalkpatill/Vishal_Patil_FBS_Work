## Write a program to calculate area of circle

def circle(rad):
    area = 3.14 * (rad)**2
    return area

rad = int(input('Enter radius of circle : '))

res = circle(rad)

print(f'Area of circle is {res}')
