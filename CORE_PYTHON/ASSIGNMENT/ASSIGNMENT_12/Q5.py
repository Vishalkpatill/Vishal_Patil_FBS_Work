# Python Program to Count the Number of Vowels in a String

def vowels(string):

    count = 0

    for i in string:
        if i in 'aeiouAEIOU':
            count = count + 1

    return count

string = input('Enter string : ') 

res = vowels(string)

print('number of vowels',res)
