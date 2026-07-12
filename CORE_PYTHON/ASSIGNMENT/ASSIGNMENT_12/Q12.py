# Python Program to count number of lowercase characters in a string.

def countLower(string):
    count = 0

    for i in string:
        if i.islower():
            count = count + 1

    return count

string = input('Enter string :')

res = countLower(string)

print('total lowercase in string are',res)