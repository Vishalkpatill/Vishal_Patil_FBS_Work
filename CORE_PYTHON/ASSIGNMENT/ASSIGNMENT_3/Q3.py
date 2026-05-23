## Write a program to input angles of a triangle and check whether triangle is valid or not.

a1 = int(input('Enter 1st angle : '))
a2 = int(input('Enter 2nd angle : '))
a3 = int(input('Enter 3rd angle : '))

if a1 + a2 + a3 == 180 :
    print('Triangle is valid')
else :
    print('Triangle is not valid')
