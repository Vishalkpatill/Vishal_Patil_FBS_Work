## Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter the number : '))

d1 = num % 10

d2 = num // 10

d3 = d2 % 10

d4 = d2 // 10

num1 = (d1 * 100) + (d3 *10) + (d4)

if num == num1:
    print('it is palindrome')
else:
    print('it is not palindrome')