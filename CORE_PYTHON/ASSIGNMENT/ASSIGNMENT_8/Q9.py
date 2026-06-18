## Write a program to check if entered number is a palindrome or
# not

def palindrome(n):
    original = n
    rev = 0

    while (n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    if original == rev:
        print('number is palindrome')
    else:
        print('number is not palindrome')

n = int(input('enter number : '))

palindrome(n)