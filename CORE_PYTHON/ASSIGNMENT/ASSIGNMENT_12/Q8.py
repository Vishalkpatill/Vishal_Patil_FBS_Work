# Python Program to Remove the Characters of Odd Index Values in a
# String

def removeOdd(string):

    temp = ''

    for i in range(len(string)):
        if i % 2 == 0:
            temp = temp + string[i]

    return temp

string = input('enter string : ') 

res = removeOdd(string)

print(res)
