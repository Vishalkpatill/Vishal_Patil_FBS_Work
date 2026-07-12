# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

def swapChar(string):
    if len(string) <= 1:
        return string
    
    string1 = string[-1] + string[1:-1] + string[0]
    return string1

string = input('enter string : ')

res = swapChar(string)

print(res)

