# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

def wordChar(string):
    words = len(string.split())
    char = len(string)

    return words, char

string = input('Enter string : ')

words, char = wordChar(string)

print('words : ',words)
print('charaters : ',char)