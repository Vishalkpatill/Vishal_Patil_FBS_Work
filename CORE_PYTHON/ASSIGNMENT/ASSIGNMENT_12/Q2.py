# Python Program to Remove the nth Index Character from a Non-Empty string

def removeChar(string, n):
    if n < 0 or n >= len(string):
        return 'invalid index'
    
    return string[:n] + string[n + 1:]

string = 'Vishal'

n = int(input('Enter index number : '))

res = removeChar(string, n)

print(res)

