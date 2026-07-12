# Python Program to Calculate the Length of a String Without Using a
# Library Function

def calLength(string):
    count = 0

    for i in string:
        count = count + 1
    return count
    

string = input('Enter string : ')

res = calLength(string)

print(f'length of string is {res}')