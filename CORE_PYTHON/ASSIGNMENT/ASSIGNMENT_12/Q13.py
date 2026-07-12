# Python Program to count number of digits and letters in a string.

def countDigitNum(string):

    alpha = 0
    digit = 0
    

    for i in string:
        if i.isalpha():
            alpha = alpha + 1
        elif i.isdigit():
            digit = digit + 1

    return alpha,digit


string = (input('Enter your string :'))

alpha,digit = countDigitNum(string)

print('digit in string are',digit)

print('alphabets in string',alpha)
