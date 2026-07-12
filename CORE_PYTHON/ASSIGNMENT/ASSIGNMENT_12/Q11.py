# 11. Python Program to replace every blank space with hyphen in a string.

def replaceString(string):
        
    string = string.replace(' ','-')
    return string

string = 'my name is vishal'

res = replaceString(string)

print(res)

