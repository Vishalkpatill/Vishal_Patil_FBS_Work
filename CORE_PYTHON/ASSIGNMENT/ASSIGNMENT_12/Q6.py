#  Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

def replaceStr(string):
    string = string.replace(' ','_')
    return string


string = input('Enter string : ')

res = replaceStr(string)

print(res)